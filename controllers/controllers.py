# -*- coding: utf-8 -*-
from odoo import http

# class WorkppReport(http.Controller):
#     @http.route('/workpp_report/workpp_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/workpp_report/workpp_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('workpp_report.listing', {
#             'root': '/workpp_report/workpp_report',
#             'objects': http.request.env['workpp_report.workpp_report'].search([]),
#         })

#     @http.route('/workpp_report/workpp_report/objects/<model("workpp_report.workpp_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('workpp_report.object', {
#             'object': obj
#         })