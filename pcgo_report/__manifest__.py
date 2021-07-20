# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) Optesis 2018 www.optesis.com

{
    'name': 'Pcgo Report',
    'version': '2.0.2',
    'author': 'Optesis',
    'category': 'Localization',
    'description': """
                    Ce module permet de gérer le nouveau plan compable SYSCOHADA Révisé.
                    Ce module permet de gérer le nouveau plan compable SYSCOHADA Révisé
                    applicable à partir du 1er janvier 2018 pour tous les pays faisant partie de l'espace OHADA.
                    **Credits:** cabinet d'expertise comptable www.kyriex.com.
                    """,
    'website': 'http://www.optesis.com',
    'depends': ['account','account_accountant','account_reports'],
    'data': [
        'views/menu_view.xml',
        'data/account_financial_html_report_data.xml',
    
    ],

}
