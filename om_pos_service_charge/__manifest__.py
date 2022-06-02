# -*- coding: utf-8 -*-

{
    'name': 'Pos Service Charge',
    'version': '13.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Service Charges In POS',
    'description': """Service charges in pos""",
    'depends': ['point_of_sale'],
    'author': 'ERPGO',
    'company': 'ERPGO',
    'maintainer': 'ERPGO',
    'website': 'http://erpgo.az',
    'support': 'support@erpgo.az',
    'data': [
        'views/pos.xml',
        'views/pos_templates.xml'
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
