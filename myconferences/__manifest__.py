# -*- coding: utf-8 -*-
{
    'name': "myconferences",

    'summary': """
        My Conference is an applucation to ease the management of conferences
        you can manage registeration of guests as well as resources...""",

    'description': """
        If you have the time to write a long description, please do !
    """,

    'author': "TranTrong",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
        'views/mymenu.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
    'application':True,
}
