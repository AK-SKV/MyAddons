# -*- coding: utf-8 -*-
from openerp import models, fields, api
class se_category(models.Model):
    _inherit = 'product.category'
    ef_grpt = fields.Integer('Группа продукта')
    ef_kat_vidt = fields.Integer('Категория продукта')
    ef_kat_vidt_kat_grpt_kod = fields.Integer('Родительская категория продукта')
class se_template(models.Model):
    _inherit = 'product.template'
    ef_id = fields.Integer('Код продукта из ЛО')
class se_product(models.Model):
    _inherit = 'product.product'
    ef_id = fields.Integer('Код продукта из ЛО')
class se_partner(models.Model):
    _inherit = 'res.partner'
    ef_id = fields.Integer('Код контрагента из ЛО')
    ef_id_adr = fields.Integer('Код адреса из KLN_ADK')
    ef_id_sot = fields.Integer('Код сотрудника из ЛО')
class product_pricelist(models.Model):
    _inherit = 'product.pricelist'
    ef_is_comp = fields.Boolean('ЭтоАкция')
    ef_PartnerId = fields.Many2one('res.partner', ondelete='set null', string='Контрагент',)
class hr_department(models.Model):
    _inherit = 'hr.department'
    ef_id = fields.Integer('Код отдела из ЛО')
class hr_employee(models.Model):
    _inherit = 'hr.employee'
    ef_id = fields.Integer('Код сотрудника из ЛО')
class res_users(models.Model):
    _inherit = 'res.users'
    ef_id_sot = fields.Integer('Код сотрудника из ЛО')
class resource_resource(models.Model):
    _inherit = 'resource.resource'
    ef_id_sot = fields.Integer('Код сотрудника из ЛО')


