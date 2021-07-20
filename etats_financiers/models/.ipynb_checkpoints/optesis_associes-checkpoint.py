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
from odoo import models, fields


class OptesisAssocies(models.Model):
    _name = 'optesis.associes'
    _description = "Associés"

    nom_associes = fields.Char('Nom')
    prenom_associes = fields.Char('Prenom')
    nationalites_associes = fields.Char('Nationalité')
    qualite_associes = fields.Char('Qualité')
    nombre_titre = fields.Integer('Nombre Titre')
    pourcent_detenue = fields.Float('% Detenue')
    adresse_associes = fields.Char('Adresse')
    company_id_associes = fields.Many2one('res.company')

    



 