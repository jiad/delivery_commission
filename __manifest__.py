{
    'name'      : 'Delivery Commission',
    'version'   : '1.0',
    'author'    : 'Prince',
    'category'  : 'Sales',
    'depends'   : ['sale_management'],
    'description': """
        This module calculate the commision based on product
    """,
    'data'      : [
        'views/res_partner_views.xml',
        'views/product_views.xml',
        'views/sale_order_views.xml',
        # 'views/assets.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}