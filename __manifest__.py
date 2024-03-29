# -*- coding: utf-8 -*-
{
    'name': "Flotte",

    'summary': """  Gardez votre parc autombile sous votre propre controle.
        """,

    'description': """
        Gardez votre parc autombile sous votre propre controle.
    """,

    'author': "vetrasoft",
    'website': "hhttp://www.vetrasoft.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'fleet',
    'version': '0.2',
    'application':'True',
    'images': ['static/description/icon.png'],

    # any module necessary for this one to work correctly
    'depends': [
        'hr',
        'base',
        'mail',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/fleet_list.xml',
        'views/tank.xml',
        'views/tank_reference.xml',
        #'static/src/css/sheet.css',
        'views/type_ve.xml',
        'views/report.xml',
        'views/Marque.xml',
        'views/EMI.xml',
       
        #'views/reference.xml',
    ],

    #'css': ['static/src/css/sheet.css'],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,

}
