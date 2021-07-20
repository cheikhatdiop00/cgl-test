{
    'name': 'Etats Financiers',
    'author': 'Optesis',
    'version': '5.4.3',
    'category': 'accounting',
    'description': """
    permet de faire des états financiers ...
""",
    'summary': 'Module de ...',
    'sequence': 9,
    'depends': ['base','l10n_pcgo','account_accountant'],
    'data': [
        'security/ir.model.access.csv',
        'wizards/wizard_view.xml',
        'views/sequence_note.xml',
        'views/menu_view.xml',
        'views/optesis_note_view.xml',
        'views/company_inherit.xml',
        'report/report_bilan.xml',
        'report/report_notes.xml',
        'report/report_compte_resultat.xml',
        'report/report_tab_flux_treso.xml',
        'report/custom_format.xml',
        'report/report.xml'
     ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
