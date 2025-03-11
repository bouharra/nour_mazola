# -*- coding: utf-8 -*-
# from odoo import http


# class Syndic(http.Controller):
#     @http.route('/syndic/syndic', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/syndic/syndic/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('syndic.listing', {
#             'root': '/syndic/syndic',
#             'objects': http.request.env['syndic.syndic'].search([]),
#         })

#     @http.route('/syndic/syndic/objects/<model("syndic.syndic"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('syndic.object', {
#             'object': obj
#         })

