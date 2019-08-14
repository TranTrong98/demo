# -*- coding: utf-8 -*-
{
    'name': "School Manager",
    'summary': 'School Imformation',
    'description': 'Manager All School around the world',
    'author': "Tran Trong - TMT",
    'website': "http://www.google.com",
    'category': 'Uncategorized',
    'version': '12.0.1',
    'depends': ['base'],
    'data': [
	#'security/student_security.xml',
        'views/views_student.xml',
	'views/templates.xml',
	'security/ir.model.access.csv',	
    ],
    'images':[],
    'license':'AGPL-3',
    'installable':True,
    'application':True,
    'auto_install':False,
}
