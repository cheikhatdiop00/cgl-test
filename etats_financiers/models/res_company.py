from odoo import api, fields, models, _


class company_inherit(models.Model):

    _name = "res.company"
    _inherit = ['res.company']

    resume_entreprise = fields.Char('Résumé de la Société')
    type_societe = fields.Selection([('sa', 'SA'), ('sas', 'SAS'),
                              ('sarl', 'SARL')], string='Type de société')
    regime_fiscal = fields.Selection([('fixe', 'Fixe')], string='Régime Fiscale')
    code_activite = fields.Selection([('code_forme_juridique', '1 - Code forme juridique'), 
                                      ('code_regime_fiscale', '2 - Code régime fiscal'),
                                      ('code_pays_du_siege_social', '3 - Code pays du siége social')], string='Code Activité')
    code_pays = fields.Selection([('autres_pays_africain', ' 2-1 '),
                                 ('france',' 2-3 '), 
                                 ('autres_pays_de_l_union_europeene', ' 3-9 '), 
                                 ('usa', ' 4-0 '),
                                 ('canada', ' 4-1 '),
                                 ('autres_pays_americain', ' 4-9'),
                                 ('pays_asiatiques', ' 5-0 '),
                                 ('autres_pays', ' 9-9 ')], string='Code Pays')
    nom_pays = fields.Selection([('autres_pays_africain', 'Autres pays africains '),
                                 ('france','France '), 
                                 ('autres_pays_de_l_union_europeene', 'Autres pays de l\'Union Européenne '), 
                                 ('usa', 'U.S.A '),
                                 ('canada', 'Canada '),
                                 ('autres_pays_americain', 'Autres pays américains '),
                                 ('pays_asiatiques', 'Pays asiatiques '),
                                 ('autres_pays', 'Autres pays ')], string='Pays')
    company_name =  fields.Many2one("res.company", "Company" )
    raison_social = fields.Char(compute='get_name_company', string='Raison Social')
    activite = fields.Char('Activité')
    activite_1 = fields.Selection([('societe_anonyme_a_participation_publique', 'Société Anonyme (SA) à participation publique'),
                                 ('societe_anonyme','Société Anonyme (SA) '), 
                                 ('societe_a_responsabilite_limite', 'Société à Responsabilité Limité (SARL) '), 
                                 ('societe_a_commandite_simple', 'Société en Commandite Simple (SCS) '),
                                 ('societe_en_nom_collectif', 'Société en Nom Collectif (SNC) '),
                                 ('societe_en_participation', 'Société en Participation (SP) '),
                                 ('groupement_dinteret_economique', 'Groupement d\'Intérêt Economique (GIE) '),
                                 ('association', 'Association'),
                                 ('societe_par_action_simplifiee', 'Société par Action Simplifiée (SAS) '),
                                 ('autres_formes_juridiques_a_preciser', 'Autres forme juridique ( à préciser) ')], string='Nom Activité')  
    activite_2 = fields.Selection([('reel_normal', 'Réel normal '),('synthetique','Synthétique '),('forfait', 'Forfait ')], string='Nom Activité')
    activite_3 = fields.Selection([('autres_pays_africain', 'Autres pays africains '),
                                 ('france','France '), 
                                 ('autres_pays_de_l_union_europeene', 'Autres pays de l\'Union Européenne '), 
                                 ('usa', 'U.S.A '),
                                 ('canada', 'Canada '),
                                 ('autres_pays_americain', 'Autres pays américains '),
                                 ('pays_asiatiques', 'Pays asiatiques '),
                                 ('autres_pays', 'Autres pays ')], string='Nom Activité')

    sigle_usuel = fields.Char('Sigle Usuel')
    capital = fields.Integer('Capital')
    nbre_de_titre = fields.Integer('Nombre De Titre')
    @api.onchange("capital","nbre_de_titre")   
    def get_value_division(self):
        if self.nbre_de_titre!=0:
             self.val_nominal = self.capital // self.nbre_de_titre
        else:
           self.val_nominal = 0
    @api.depends("name")   
    def get_name_company(self):
          self.raison_social=self.name
    num_caisse_securite = fields.Char('Numéro CSS')
    complement = fields.Integer('Complément')
    code_postal =fields.Char('Code Postal')
    region = fields.Char('Region')
    ville = fields.Char('Ville')
    val_nominal = fields.Integer(compute='get_value_division', string='Val.nominal')
    num_id_fiscal =fields.Integer('N° ID.Fiscal')
    num_rc = fields.Integer('Numéro R.C')
    greffe = fields.Char('Greffe')
    pays_siege = fields.Many2one('res.country', string='Pays du Siége')
    nombre_etab_dans_le_pays = fields.Integer('Nombre Etab dans le pays')
    nombre_etab_hors_pays = fields.Integer('Nb EtS hors pays')
    num_code_importateur = fields.Integer('N° Code Importateur ')
    code_activite_principale = fields.Integer('Code Activité Principale ')
    premiere_annee_exercice = fields.Integer('Premiere Année Exercice ')
    num_repertoire_entreprise = fields.Integer('N° repertoire entreprise')
    nom_contacter = fields.Char('Nom')
    qualite_contacter = fields.Char('Qualité')
    adresse_contacter = fields.Char('Adresse')
    nom_signature = fields.Char('Nom')
    qualite_signature = fields.Char('Qualité')
    controle_entete = fields.Selection([('entite_sous_controle_publique', 'Entité Sous Contrôle publique'),       ('entite_sous_controle_privee_national', 'Entité Sous Contrôle privée national'),
                              ('entite_sous_controle_privee_etranger', 'Entité Sous Contrôle privée etranger')],
                                       string='Contrôle de Entête')
    bank_ids = fields.One2many('optesis.bank', 'company_id_bank', 'Bank')
    activity_ids = fields.One2many('optesis.activity', 'company_id_activity', 'Activité')
    associes_ids = fields.One2many('optesis.associes', 'company_id_associes', 'Associés')
    dirigeants_ids = fields.One2many('optesis.dirigeant', 'company_id_dirigeant', 'Dirigeants')
    conseil_ids = fields.One2many('optesis.conseil', 'company_id_conseil', 'Membres du Conseil')
        
    @api.onchange("activity_ids")   
    def get_percent_ca(self):
        if self.activity_ids:
            for line in self.activity_ids:
                line.pourcent_ca_ht_vt = line.ca_ht_vt / 100