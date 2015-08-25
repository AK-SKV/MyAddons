# -*- coding: utf-8 -*-
from openerp import http

# class SePartnerTst1(http.Controller):
#     @http.route('/se_partner_tst1/se_partner_tst1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/se_partner_tst1/se_partner_tst1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('se_partner_tst1.listing', {
#             'root': '/se_partner_tst1/se_partner_tst1',
#             'objects': http.request.env['se_partner_tst1.se_partner_tst1'].search([]),
#         })

#     @http.route('/se_partner_tst1/se_partner_tst1/objects/<model("se_partner_tst1.se_partner_tst1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('se_partner_tst1.object', {
#             'object': obj
#         })