{
    'name':'School Manager',
    'description':'Manager School _ Student and Teacher.',
    'author':'Tran Trong',
    'license':'AGPL-3',
    'version':'12.0.1.0',
    'category':'Uncategorized',
    'depends':['base'],
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
	'views/Manager_view.xml',
        ],
    'application': True,
    'installable': True,
}
