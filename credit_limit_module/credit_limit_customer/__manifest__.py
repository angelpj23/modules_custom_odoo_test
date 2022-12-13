# -*- coding: utf-8 -*-
{
    'name': "Credit limit from customer",
    'summary': """Module to add credit limit to customers. """,
    'description': """Module to add credit limit to customers.""",
    'author': "Angel_pj23",
    'website': "",
    'category': 'Customizations',
    'version': '14.0.0.1',

    'depends': [
        'base',
        'contacts',
        'sale',
        'account',
    ],

    'data': [
        'views/res_partner_view.xml',
        'views/sale_order_view.xml',
        'views/account_move_view.xml'
    ],
}
