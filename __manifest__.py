# -*- coding: utf-8 -*-
{
    'name': "ESI Recommandations",

    'summary': """Gestion des demandes de lettre de recommandation""",

    'description': """
        Module ESI Recommandations pour  la gestion des demandes de lettre de recommandation:
            - ajout de la demande de lettre de recommandation 
            - validation de la demande            
    """,

    'author': "SIT4",
    'website': "https://www.esi.dz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'templates.xml',
        'views/esirecommandation.xml',
        'reports.xml'
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
