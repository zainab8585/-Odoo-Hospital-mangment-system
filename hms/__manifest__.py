# -*- coding: utf-8 -*-
{
    'name': "hms",

    'summary': """
        Hospital Management system extend """,

    'description': """
        Hospital Management system extend
    """,

    'author': "odoo class 2020",
    'website': "http://www.mah007.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'hospital',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','basic_hms'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/Reception_view.xml',
        'views/patient_mainscreen_inherit_view.xml',
        'views/Logout.xml',
        'views/transfer.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}