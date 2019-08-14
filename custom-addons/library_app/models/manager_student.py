from odoo import api, fields, models
from odoo.exceptions import Warning

class Student(models.Model):
    _Name = 'manager.student'
    _description='a model for Student'
    name = fields.Char('Name',30,required=True)
    age = fields.Char('Age',required=True)

    @api.multi
    def _check_name(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check

    @api.multi
    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise Warning('Please provide an ISBN for %s' % book.name)
            if book.isbn and not book._check_isbn():
                raise Warning('%s is an invalid ISBN' % book.isbn)
        return True

