# -*- coding: utf-8 -*-
from openerp import models, fields, api
class se_category(models.Model):
    _inherit = 'product.category'
    ef_grpt = fields.Integer('Группа продукта', select=True)
    ef_kat_vidt = fields.Integer('Категория продукта', select=True)
    ef_kat_vidt_kat_grpt_kod = fields.Integer('Родительская категория продукта', select=True)
class se_template(models.Model):
    _inherit = 'product.template'
    ef_id = fields.Integer('Код продукта из ЛО', select=True)
class se_product(models.Model):
    _inherit = 'product.product'
    ef_id = fields.Integer('Код продукта из ЛО', select=True)
class se_partner(models.Model):
    _inherit = 'res.partner'
    ef_id = fields.Integer('Код контрагента из ЛО', select=True)
    ef_id_adr = fields.Integer('Код адреса из KLN_ADK', select=True)
    ef_id_sot = fields.Integer('Код сотрудника из ЛО', select=True)
class product_pricelist(models.Model):
    _inherit = 'product.pricelist'
    ef_is_comp = fields.Boolean('ЭтоАкция', select=True)
    ef_PartnerId = fields.Many2one('res.partner', ondelete='set null', string='Контрагент', select=True)
class hr_department(models.Model):
    _inherit = 'hr.department'
    ef_id = fields.Integer('Код отдела из ЛО', select=True)
class hr_employee(models.Model):
    _inherit = 'hr.employee'
    ef_id = fields.Integer('Код сотрудника из ЛО', select=True)
class res_users(models.Model):
    _inherit = 'res.users'
    ef_id_sot = fields.Integer('Код сотрудника из ЛО', select=True)
class resource_resource(models.Model):
    _inherit = 'resource.resource'
    ef_id_sot = fields.Integer('Код сотрудника из ЛО', select=True)
class res_company(models.Model):
    _inherit = 'res.company'
    ef_id = fields.Integer('Код клиента из KAT_KLN ЛО', select=1)
class account_bank_statement(models.Model):
    _inherit = 'account.bank.statement'
    rch_b = fields.Char('Расчетный счет из ЛО',size=20, select=True)
class account_invoice(models.Model):
    _inherit = 'account.invoice'
 #   ef_id = fields.Integer('Код строки из LIST_SKL ЛО')
  #  ставим вручную bigint
class account_invoice_line(models.Model):
    _inherit = 'account.invoice.line'
  #  ef_id = fields.Integer('Код строки из HIST_SKL ЛО')
  #  ef_list_id = fields.Integer('Код строки из LIST_SKL ЛО')
  #  ставим вручную bigint
class stock_warehouse(models.Model):
    _inherit = 'stock.warehouse'
    ef_id = fields.Integer('Код строки из KAT_SKL ЛО', select=True)
    