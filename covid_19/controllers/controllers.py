# -*- coding: utf-8 -*-
from odoo import http

# class Covid19(http.Controller):
#     @http.route('/covid_19/covid_19/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/covid_19/covid_19/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('covid_19.listing', {
#             'root': '/covid_19/covid_19',
#             'objects': http.request.env['covid_19.covid_19'].search([]),
#         })

#     @http.route('/covid_19/covid_19/objects/<model("covid_19.covid_19"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('covid_19.object', {
#             'object': obj
#         })