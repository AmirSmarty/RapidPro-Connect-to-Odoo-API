# -*- coding: utf-8 -*-
{
    'name': "Rumors Tracking Module via RapidPro",

    'summary': "A Module for tracking rumors via Telegram or SMS or WhatsApp",

    'description': "A POC for connect RapidPro to Odoo 16",

    'author': "ZAKE",
    'website': "https://www.zake.pro",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu.xml',
        'views/patient.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
