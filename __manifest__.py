# -*- coding: utf-8 -*-
{
    'name': "workpp_report",

    'summary': """
        WorkPP Report""",

    'description': """
        Report for WorkPP module.
    """,

    'author': "Satusoft",
    'website': "https://satusoft.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['workpp'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'reports/workpp.xml',
        'reports/workpp_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}