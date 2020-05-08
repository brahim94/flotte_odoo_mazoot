# -*- coding: utf-8 -*-
from odoo import http

# class Flotte(http.Controller):
#     @http.route('/flotte/flotte/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/flotte/flotte/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('flotte.listing', {
#             'root': '/flotte/flotte',
#             'objects': http.request.env['flotte.flotte'].search([]),
#         })

#     @http.route('/flotte/flotte/objects/<model("flotte.flotte"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('flotte.object', {
#             'object': obj
#         })