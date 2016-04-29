# -*- coding: utf-8 -*-
#
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

import logging
import xmlrpclib
from openerp import models, fields
from openerp.addons.connector.queue.job import job
from openerp.addons.connector.exception import MappingError
from openerp.addons.connector.unit.mapper import (mapping,
                                                  ImportMapper
                                                  )
from openerp.addons.connector.exception import IDMissingInBackend
from ..unit.backend_adapter import (GenericAdapter)
from ..unit.import_synchronizer import (DelayedBatchImporter, YmkImporter)
from ..connector import get_environment
from ..backend import Ymk
_logger = logging.getLogger(__name__)


class YmkProductCategory(models.Model):
    _name = 'Ymk.product.category'
    _inherit = 'Ymk.binding'
    _inherits = {'product.category': 'openerp_id'}
    _description = 'Ymk product category'

    _rec_name = 'name'

    openerp_id = fields.Many2one(comodel_name='product.category',
                                 string='category',
                                 required=True,
                                 ondelete='cascade')
    backend_id = fields.Many2one(
        comodel_name='wc.backend',
        string='Ymk Backend',
        store=True,
        readonly=False,
    )

    slug = fields.Char('Slung Name')
    Ymk_parent_id = fields.Many2one(
        comodel_name='Ymk.product.category',
        string='Ymk Parent Category',
        ondelete='cascade',)
    description = fields.Char('Description')
    count = fields.Integer('count')


@Ymk
class CategoryAdapter(GenericAdapter):
    _model_name = 'Ymk.product.category'
    _Ymk_model = 'products/categories'

    def _call(self, method, arguments):
        try:
            return super(CategoryAdapter, self)._call(method, arguments)
        except xmlrpclib.Fault as err:
            # this is the error in the YmkCommerce API
            # when the customer does not exist
            if err.faultCode == 102:
                raise IDMissingInBackend
            else:
                raise

    def search(self, filters=None, from_date=None, to_date=None):
        """ Search records according to some criteria and return a
        list of ids

        :rtype: list
        """
        if filters is None:
            filters = {}
        Ymk_DATETIME_FORMAT = '%Y/%m/%d %H:%M:%S'
        dt_fmt = Ymk_DATETIME_FORMAT
        if from_date is not None:
            filters.setdefault('updated_at', {})
            filters['updated_at']['from'] = from_date.strftime(dt_fmt)
        if to_date is not None:
            filters.setdefault('updated_at', {})
            filters['updated_at']['to'] = to_date.strftime(dt_fmt)
        return self._call('products/categories/list',
                          [filters] if filters else [{}])


@Ymk
class CategoryBatchImporter(DelayedBatchImporter):

    """ Import the YmkCommerce Partners.

    For every partner in the list, a delayed job is created.
    """
    _model_name = ['Ymk.product.category']

    def _import_record(self, Ymk_id, priority=None):
        """ Delay a job for the import """

        super(CategoryBatchImporter, self)._import_record(
            Ymk_id, priority=priority)

    def run(self, filters=None):
        """ Run the synchronization """
        from_date = filters.pop('from_date', None)
        to_date = filters.pop('to_date', None)
        record_ids = self.backend_adapter.search(
            filters,
            from_date=from_date,
            to_date=to_date,
        )
        _logger.info('search for Ymk Product Category %s returned %s',
                     filters, record_ids)
        for record_id in record_ids:
            self._import_record(record_id)
CategoryBatchImporter = CategoryBatchImporter


@Ymk
class ProductCategoryImporter(YmkImporter):
    _model_name = ['Ymk.product.category']

    def _import_dependencies(self):
        """ Import the dependencies for the record"""
        record = self.Ymk_record
        # import parent category
        # the root category has a 0 parent_id
        record = record['product_category']
        if record['parent']:
            parent_id = record['parent']
            if self.binder.to_openerp(parent_id) is None:
                importer = self.unit_for(YmkImporter)
                importer.run(parent_id)
        return

    def _create(self, data):
        openerp_binding = super(ProductCategoryImporter, self)._create(data)
        return openerp_binding

    def _after_import(self, binding):
        """ Hook called at the end of the import """
        return

ProductCategoryImport = ProductCategoryImporter


@Ymk
class ProductCategoryImportMapper(ImportMapper):
    _model_name = 'Ymk.product.category'

    @mapping
    def name(self, record):
        if record['product_category']:
            rec = record['product_category']
            return {'name': rec['name']}

    @mapping
    def backend_id(self, record):
        return {'backend_id': self.backend_record.id}
#

    @mapping
    def parent_id(self, record):
        if record['product_category']:
            rec = record['product_category']
            if not rec['parent']:
                return
            binder = self.binder_for()
            category_id = binder.to_openerp(rec['parent'], unwrap=True)
            Ymk_cat_id = binder.to_openerp(rec['parent'])
            if category_id is None:
                raise MappingError("The product category with "
                                   "Ymk id %s is not imported." %
                                   rec['parent'])
            return {'parent_id': category_id, 'Ymk_parent_id': Ymk_cat_id}


@job(default_channel='root.Ymk')
def category_import_batch(session, model_name, backend_id, filters=None):
    """ Prepare the import of category modified on YmkCommerce """
    env = get_environment(session, model_name, backend_id)
    importer = env.get_connector_unit(CategoryBatchImporter)
    importer.run(filters=filters)
