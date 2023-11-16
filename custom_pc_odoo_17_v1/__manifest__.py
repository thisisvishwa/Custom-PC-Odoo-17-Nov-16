{
    'name': 'Custom PC Builder',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Custom PC Building Module',
    'sequence': 1,
    'description': """
    This module allows users to build a custom PC by selecting components from a product catalog. 
    It automatically calculates the total cost and checks for compatibility between components.
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'product', 'sale', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'data/custom_pc_data.xml',
        'views/custom_pc_view.xml',
        'static/src/css/custom_pc.css',
        'static/src/js/custom_pc.js',
        'static/src/xml/custom_pc_template.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}