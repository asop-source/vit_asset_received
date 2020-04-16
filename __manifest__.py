# -*- coding: utf-8 -*-
{
    'name': "vit asset received",

    'summary': """
        Penambahan Tombol state Received
        """,

    'author': "asopkarawang@gmail.com",
    'website': "http://www.vitraining.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list

    # any module necessary for this one to work correctly
    'depends': ['base','vit_asset'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',

    ],

}