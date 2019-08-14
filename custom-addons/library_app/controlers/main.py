from odoo import http

class Students(http.Controller):
    @http.route('/manager/students', auth='user')
    def list(self, **kwargs):
        Student = http.request.env['manager.student']
        students = Student.search([])
        return http.request.render('manager_app.manager_list_template', {'students': students})
