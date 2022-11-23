# -*- coding: utf-8 -*-
{
    'name': 'EZcare Agency',
    'description': '''This is not used to create the agency''',
    'author': 'MyEZcare',
    'website': 'https://www.myezcare.com',
    'category': 'None',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/m_core_agency_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'static/src/scss/*.scss',
        ],
    },
}
