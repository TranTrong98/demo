# -*- coding: utf-8 -*-
from odoo import http

class Managerschool(http.Controller):
    @http.route('/managerschool/', auth='public')
    def index(self, **kw):
        return "Hello, everybody"
    @http.route('/managerschool/students/', auth='public')
    def list(self, **kw):
        return http.request.render('managerschool.student', {
            'students': http.request.env['managerschool.student'].search([]),
            })
    #@http.route('/managerschool/managerschool/objects/<model("managerschool.student"):obj>/', auth='public')
    #def object(self, obj, **kw):
    #   return http.request.render('managerschool.object', {'object': obj })
