# -*- coding: utf-8 -*-

from odoo import models, fields, api

class managerschool(models.Model):
    _name = 'managerschool.student'
    _description='a model for School'
    name = fields.Char(string='Name',size=30 ,required='True')
    age = fields.Integer(string='Age')
    
#    @api.depends('value')
#    def _check_length(self):
#        if len(record.name) > 30:
#            return fasle
#        return true
#        	self.name = len(self.value)
