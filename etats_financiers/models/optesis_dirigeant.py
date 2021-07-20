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


class OptesisDirigeants(models.Model):
    _name = 'optesis.dirigeant'
    _description = "dirigeant"

    nom_dirigeant = fields.Selection([('pdg', 'Président Directeur Général'), ('dg', 'Directeur Général'),
                              ('ag', 'administrateur Général'),('gr', ' Gérant'),('at', ' Autres ')], string='Dirigeant')
    adresse_dirigeant = fields.Char('Adresse')
    qualite_dirigeant = fields.Char('Qualité')
    id_fiscal = fields.Char('Id Fiscal')
    company_id_dirigeant = fields.Many2one('res.company')