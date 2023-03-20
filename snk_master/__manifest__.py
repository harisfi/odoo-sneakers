# -*- coding: utf-8 -*-

{
    'name': 'Master Data',
    'version': '1.0',
    'category': 'Master Data',
    'author': 'livai',
    'sequence': -110,
    'summary': 'Master Data',
    'description': """Modul Master Data For Sneakers""",
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/product_view.xml',
        'views/suplier_view.xml',
    ],
    'demo': [],
    'application':True,
    'installable': True,
    'auto_install': False,
    # 'assets': {},
    'license': 'LGPL-3',
}
