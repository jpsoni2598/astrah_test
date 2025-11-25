{
    'name': "Astrah Test",
    'version': '1.0',
    'depends': [],
    'author': "Jayesh Pamnani",
    'category': 'CRM',
    'description': """
        Test task module for Astrah OS evaluation.
        Demonstrates ORM, custom views, Tailwind integration,
        and an OWL component in Odoo 19.
    """,

    'data': [
        'security/ir.model.access.csv',
        'views/lead_form.xml',
        'views/menus.xml',
    ],

    'demo': [
    ],

    'assets': {
        'web.assets_backend': [
            'astrah_test/static/src/css/tailwind.bundle.css',
            'astrah_test/static/src/js/test_component.js',
            'astrah_test/static/src/xml/test_component.xml',
        ],
    },

    'installable': True,
    'application': False,
}
