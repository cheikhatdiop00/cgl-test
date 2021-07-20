# -*- coding: utf-8 -*-
###################################################################################
#    A part of OpenHRMS Project <https://www.openhrms.com>
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2018-TODAY Cybrosys Technologies (<https://www.cybrosys.com>).
#    Author: Treesa Maria Jude (<https://www.cybrosys.com>)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################
from odoo import models, fields,api


class OptesisActivity(models.Model):
    _name = 'optesis.activity'
    _description = "Activité"

    designation_activite = fields.Selection([
                                 ('societe_anonyme_a_participation_publique', 'Société Anonyme (SA) à participation publique'),
                                 ('societe_anonyme','Société Anonyme (SA) '), 
                                 ('societe_a_responsabilite_limite', 'Société à Responsabilité Limité (SARL) '), 
                                 ('societe_a_commandite_simple', 'Société en Commandite Simple (SCS) '),
                                 ('societe_en_nom_collectif', 'Société en Nom Collectif (SNC) '),
                                 ('societe_en_participation', 'Société en Participation (SP) '),
                                 ('groupement_dinteret_economique', 'Groupement d\'Intérêt Economique (GIE) '),
                                 ('association', 'Association'),
                                 ('societe_par_action_simplifiee', 'Société par Action Simplifiée (SAS) '),
                                 ('autres_formes_juridiques_a_preciser', 'Autres forme juridique ( à préciser)'),
                                 ('reel_normal', 'Réel normal '),('synthetique','Synthétique '),('forfait', 'Forfait '),
                                 ('autres_pays_africain', 'Autres pays africains '),
                                 ('france','France '), 
                                 ('autres_pays_de_l_union_europeene', 'Autres pays de l\'Union Européenne '), 
                                 ('usa', 'U.S.A '),
                                 ('canada', 'Canada '),
                                 ('autres_pays_americain', 'Autres pays américains '),
                                 ('pays_asiatiques', 'Pays asiatiques '),
                                 ('autres_pays', 'Autres pays ')], 
                                 string='Désignation')  
    code_activite = fields.Char('Code')
    ca_ht_vt = fields.Float('CA HT ou VA ')
    pourcent_ca_ht_vt = fields.Float('% CA HT ou VA ')
    nb_ca = fields.Float('Total')
    company_id_activity = fields.Many2one('res.company')
    

    



 