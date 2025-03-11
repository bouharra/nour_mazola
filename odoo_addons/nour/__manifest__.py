# -*- coding: utf-8 -*-
{
    'name': "Noura",
    'version': '0.1',
    'category': 'Uncategorized',
    'installable': True,
    'application': True,
    'icon': '/nour/static/description/puce.png',
    'summary': 'Gestion des résidents et cotisations',
    'author': "BOUHARRA mohamed",
    'website': "https://www.bob.com",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
      # 'security/n_resident_securite.xml',
        'views/n_resident2view.xml',
        'views/n_0_action.xml',

        'views/n_residenceview.xml',
        'reports/mensuelle_report.xml',
        'reports/globale_report.xml',
        'views/n_anview.xml',
        'views/n_moisview.xml',
        'views/n_depenseview.xml',
        'views/n_cotisationview.xml',
        'views/n_desispecialeview.xml',
        'views/n_desidepenseview.xml',
        'views/n_detailspecialeview.xml',
        'views/n_specialeview.xml',
        'views/n_moisview.xml',
        'views/n_helpview.xml',
        'reports/resident_report.xml',
        'reports/annuelle_report.xml',
        'reports/recu_report.xml',
        'views/n_residentview.xml',

    ],
        'demo': [],
        'assets': {
        'web.assets_backend': [
        'nour/static/src/css/style.css',
    ],
}
}

