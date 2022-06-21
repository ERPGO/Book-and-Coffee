# -*- coding: utf-8 -*-

{
    'name': 'Pos Service Charges',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'author': 'ErpMstar Solutions',
    'summary': 'Allows you to take service charges in Point of sale.',
    'description': "Allows you to take service charges in Point of sale.",
    'depends': ['point_of_sale'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_service_charges/static/src/js/pos.js',
        ],
        'web.assets_qweb': [
            'pos_service_charges/static/src/xml/**/*',
        ],
    },
    'images': [
        'static/description/numpad.jpg',
    ],
    'installable': True,
    'website': '',
    'auto_install': False,
    'price': 9,
    'currency': 'EUR',
}
