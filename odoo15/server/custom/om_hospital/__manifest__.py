# -*- coding: utf-8 -*-

{
    'name': 'Hospital Management',
    'version': '1.0',
    'summary': 'Hospital Management Software',
    'sequence': -100,
    'description': """Hospital Management Software""",
    'category': 'Productivity',
    'website': 'https://www.hanzawnyine.com',
    'depends': [
        'sale'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/sale.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
