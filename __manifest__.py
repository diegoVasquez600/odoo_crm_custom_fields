{
    'name': 'Custom Fields Colombia Care',
    'version': '1.0',
    'category': 'Sales',
    'author': 'Diego Rios Vasquez',
    'website': 'https://www.linkedin.com/in/diegovasquez600/',
    'depends' : ['base','crm'],
    'data': [
        'views/crm_lead_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'odoo_crm_customfields/static/src/js/conditional_field.js',
        ],
    },
    'installable': True,
    'application': False,
}