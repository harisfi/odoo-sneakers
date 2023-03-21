# -*- coding: utf-8 -*-

{
    'name': 'Simple Sales Order',
    'version': '1.0',
    'category': 'Sales order',
    'author': 'livai',
    'sequence': -100,
    'summary': 'Simple Sales Order',
    'description': """Simple Sales Order System""",
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/menu.xml',
        'views/salesorder_view.xml'
    ],
    'demo': [],
    'application':True,
    'installable': True,
    'auto_install': False,
    # 'assets': {},
    'license': 'LGPL-3',
}
