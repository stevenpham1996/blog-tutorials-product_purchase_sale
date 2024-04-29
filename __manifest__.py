# -*- coding: utf-8 -*-
{
    'name': "product_purchase_sale",

    'summary': "Product-Purchase-Sales Addon",

    'description': """
    Customized Product's Attribute, Purchase's Order, and Sales's Order models for Cat Cattery
    """,

    'author': "Phamorphosis",
    'website': "www.odoo-optimo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase', 'product', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

