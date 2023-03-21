# -*- coding: utf-8 -*-
{
    'name': 'Sneaker Purchase',
    'version': '1.0.0',
    'category': 'Purchase',
    'author': 'Haris',
    'summary': 'Sneaker Purchase System',
    'description': """Sneaker purchase system""",
    'depends': ['snk_master'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/order_views.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3',
    'sequence': -1
}