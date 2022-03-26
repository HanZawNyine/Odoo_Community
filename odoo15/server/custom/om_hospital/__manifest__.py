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
        'sale', 'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',

        'wizard/create_appointment_view.xml',

        'views/patient_view.xml',
        'views/sale.xml',
        'views/kid_view.xml',
        'views/patient_gender_view.xml',
        'views/appointment_view.xml',

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
