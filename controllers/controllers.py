# -*- coding: utf-8 -*-
# from odoo import http


# class Rumors(http.Controller):
#     @http.route('/rumors/rumors', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rumors/rumors/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rumors.listing', {
#             'root': '/rumors/rumors',
#             'objects': http.request.env['rumors.rumors'].search([]),
#         })

#     @http.route('/rumors/rumors/objects/<model("rumors.rumors"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rumors.object', {
#             'object': obj
#         })
