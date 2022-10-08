# -*- coding: utf-8 -*-
{
    'name': "res_partner_custom",

    'summary': """Este modulo personaliza el modulo de contactos""",

    'description': """
        Personaliza tus contactos
    """,

    'author': "Angel Perez",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'contacts'
    ],

    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/res_partner_custom.xml',
    ],
    'installable': True,
}
