from odoo import api, fields, models, _
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class OptesisNote(models.Model):
    _name = "optesis.note"

    name = fields.Char("Nom", required="True")
    sequence = fields.Char("Sequence")
    date_debut = fields.Date("Date de debut", required="True")
    date_fin = fields.Date("Date de debut", required="True")
    company_id = fields.Many2one('res.company', 'Company', copy=False, readonly=True, default=lambda self: self.env.user.company_id)
    all_on = fields.Boolean("Tout Cocher")
    all_off = fields.Boolean("Tout decocher")
    note1 = fields.Boolean("Note 1")
    note3A = fields.Boolean("Note 3A")
    note3B = fields.Boolean("Note 3B")
    note3C = fields.Boolean("Note 3C")
    note3D = fields.Boolean("Note 3D")
    note3E = fields.Boolean("Note 3E")
    note4 = fields.Boolean("Note 4")
    note5 = fields.Boolean("Note 5")
    note6 = fields.Boolean("Note 6")
    note7 = fields.Boolean("Note 7")
    note8 = fields.Boolean("Note 8")
    note8A = fields.Boolean("Note 8A")
    note9 = fields.Boolean("Note 9")
    note10 = fields.Boolean("Note 10")
    note11 = fields.Boolean("Note 11")
    note12 = fields.Boolean("Note 12")
    note13 = fields.Boolean("Note 13")
    note14 = fields.Boolean("Note 14")
    note15A = fields.Boolean("Note 15A")
    note15B = fields.Boolean("Note 15B")
    note16A = fields.Boolean("Note 16A")
    note16B = fields.Boolean("Note 16B")
    note16B_BIS = fields.Boolean("Note 16B BIS")
    note16C = fields.Boolean("Note 16C")
    note17 = fields.Boolean("Note 17")
    note18 = fields.Boolean("Note 18")
    note19 = fields.Boolean("Note 19")
    note20 = fields.Boolean("Note 20")
    note21 = fields.Boolean("Note 21")
    note22 = fields.Boolean("Note 22")
    note23 = fields.Boolean("Note 23")
    note24 = fields.Boolean("Note 24")
    note25 = fields.Boolean("Note 25")
    note26 = fields.Boolean("Note 26")
    note27A = fields.Boolean("Note 27A")
    note27B = fields.Boolean("Note 27B")
    note28 = fields.Boolean("Note 28")
    note29 = fields.Boolean("Note 29")
    note30 = fields.Boolean("Note 30")
    note31 = fields.Boolean("Note 31")
    note32 = fields.Boolean("Note 32")
    note33 = fields.Boolean("Note 33")
    note34 = fields.Boolean("Note 34")
    note35 = fields.Boolean("Note 35")
    note36 = fields.Boolean("Note 36")
    note37 = fields.Boolean("Note 37")

    note1_lines1 = fields.One2many("optesis.note1.tab1", "note_id")
    note1_lines2 = fields.One2many("optesis.note1.tab2", "note_id")
    commentaire_note1 = fields.Text("Commentaire")

    note3A_lines = fields.One2many("optesis.note3a", "note_id")
    commentaire_note3A = fields.Text("Commentaire")

    note3B_lines = fields.One2many("optesis.note3b", "note_id")
    commentaire_note3B = fields.Text("Commentaire")

    note3C_lines = fields.One2many("optesis.note3c", "note_id")
    commentaire_note3C = fields.Text("Commentaire")

    note3D_lines = fields.One2many("optesis.note3d", "note_id")
    commentaire_note3D = fields.Text("Commentaire")

    note3E_lines = fields.One2many("optesis.note3e", "note_id")
    commentaire_note3E = fields.Text("Commentaire")

    note4_lines1 = fields.One2many("optesis.note4.tab1", "note_id")
    note4_lines2 = fields.One2many("optesis.note4.tab2", "note_id")
    commentaire_note4 = fields.Text("Commentaire")

    note5_lines1 = fields.One2many("optesis.note5.tab1", "note_id")
    commentaire1_note5 = fields.Text("Commentaire")
    note5_lines2 = fields.One2many("optesis.note5.tab2", "note_id")
    commentaire2_note5 = fields.Text("Commentaire")

    note6_lines = fields.One2many("optesis.note6", "note_id")
    commentaire_note6 = fields.Text("Commentaire")

    note7_lines = fields.One2many("optesis.note7", "note_id")
    commentaire_note7 = fields.Text("Commentaire")

    note8_lines = fields.One2many("optesis.note8", "note_id")
    commentaire_note8 = fields.Text("Commentaire")

    note8A_lines1 = fields.One2many("optesis.note8a.tab1", "note_id")
    note8A_lines2 = fields.One2many("optesis.note8a.tab2", "note_id")

    note9_lines = fields.One2many("optesis.note9", "note_id")
    commentaire_note9 = fields.Text("Commentaire")

    note10_lines = fields.One2many("optesis.note10", "note_id")
    commentaire_note10 = fields.Text("Commentaire")

    note11_lines = fields.One2many("optesis.note11", "note_id")
    commentaire_note11 = fields.Text("Commentaire")

    note12_lines1 = fields.One2many("optesis.note12.tab1", "note_id")
    commentaire1_note12 = fields.Text("Commentaire")
    note12_lines2 = fields.One2many("optesis.note12.tab2", "note_id")
    commentaire2_note12 = fields.Text("Commentaire")

    note13_lines = fields.One2many("optesis.note13", "note_id")
    commentaire_note13 = fields.Text("Commentaire")

    note14_lines = fields.One2many("optesis.note14", "note_id")
    commentaire_note14 = fields.Text("Commentaire")

    note15A_lines = fields.One2many("optesis.note15a", "note_id")
    commentaire_note15A = fields.Text("Commentaire")

    note15B_lines = fields.One2many("optesis.note15b", "note_id")
    commentaire_note15B = fields.Text("Commentaire")

    note16A_lines = fields.One2many("optesis.note16a", "note_id")
    commentaire_note16A = fields.Text("Commentaire")

    note16BTab1_lines = fields.One2many("optesis.note16b.tab1", "note_id")
    commentaire_note16BTab1 = fields.Text("Commentaire")

    note16BTab2_lines = fields.One2many("optesis.note16b.tab2", "note_id")
    commentaire_note16BTab2 = fields.Text("Commentaire")

    note16BTab3_lines = fields.One2many("optesis.note16b.tab3", "note_id")
    commentaire_note16BTab3 = fields.Text("Commentaire")

    note16BBISTab1_lines = fields.One2many("optesis.note16bbis.tab1", "note_id")
    commentaire_note16BBISTab1 = fields.Text("Commentaire")

    note16BBISTab2_lines = fields.One2many("optesis.note16bbis.tab2", "note_id")
    commentaire_note16BBISTab2 = fields.Text("Commentaire")

    note16C_lines = fields.One2many("optesis.note16c", "note_id")
    commentaire_note16C = fields.Text("Commentaire")

    note17_lines = fields.One2many("optesis.note17", "note_id")
    commentaire_note17 = fields.Text("Commentaire")

    note18_lines = fields.One2many("optesis.note18", "note_id")
    commentaire_note18 = fields.Text("Commentaire")

    note19_lines = fields.One2many("optesis.note19", "note_id")
    commentaire_note19 = fields.Text("Commentaire")

    note20_lines = fields.One2many("optesis.note20", "note_id")
    commentaire_note20 = fields.Text("Commentaire")

    note21_lines = fields.One2many("optesis.note21", "note_id")
    commentaire_note21 = fields.Text("Commentaire")

    note22_lines = fields.One2many("optesis.note22", "note_id")
    commentaire_note22 = fields.Text("Commentaire")

    note23_lines = fields.One2many("optesis.note23", "note_id")
    commentaire_note23 = fields.Text("Commentaire")

    note24_lines = fields.One2many("optesis.note24", "note_id")
    commentaire_note24 = fields.Text("Commentaire")

    note25_lines = fields.One2many("optesis.note25", "note_id")
    commentaire_note25 = fields.Text("Commentaire")

    note26_lines = fields.One2many("optesis.note26", "note_id")
    commentaire_note26 = fields.Text("Commentaire")

    note27A_lines = fields.One2many("optesis.note27a", "note_id")
    commentaire_note27A = fields.Text("Commentaire")

    note28_lines = fields.One2many("optesis.note28", "note_id")
    commentaire_note28 = fields.Text("Commentaire")

    note29_lines = fields.One2many("optesis.note29", "note_id")
    commentaire_note29 = fields.Text("Commentaire")

    note30_lines = fields.One2many("optesis.note30", "note_id")
    commentaire_note30 = fields.Text("Commentaire")

    note31_lines = fields.One2many("optesis.note31", "note_id")

    note32_lines = fields.One2many("optesis.note32", "note_id")

    note33_lines = fields.One2many("optesis.note33", "note_id")

    note34_lines = fields.One2many("optesis.note34", "note_id")

    note37_lines = fields.One2many("optesis.note37", "note_id")
    
    _defaults = {
        'sequence': lambda obj, cr, uid, context: '/',
    }


    @api.model
    def create(self, vals):
        if vals.get('sequence', '/') == '/':
            vals['sequence'] = self.env['ir.sequence'].next_by_code('optesis.note') or '/'
        result = super(OptesisNote, self).create(vals)
        return result
    
    
    @api.onchange("all_on")
    def check_all(self):
        if self.all_on:
            self.all_off = False
            self.note1 = True
            self.note3A = True
            self.note3B = True
            self.note3C = True
            self.note3D = True
            self.note3E = True
            self.note4 = True
            self.note5 = True
            self.note6 = True
            self.note7 = True
            self.note8 = True
            self.note8A = True
            self.note9 = True
            self.note10 = True
            self.note11 = True
            self.note12 = True
            self.note13 = True
            self.note14 = True
            self.note15A = True
            self.note15B = True
            self.note16A = True
            self.note16B = True
            self.note16B_BIS = True
            self.note16C = True
            self.note17 = True
            self.note18 = True
            self.note19 = True
            self.note20 = True
            self.note21 = True
            self.note22 = True
            self.note23 = True
            self.note24 = True
            self.note25 = True
            self.note26 = True
            self.note27A = True
            self.note27B = True
            self.note28 = True
            self.note29 = True
            self.note30 = True
            self.note31 = True
            self.note32 = True
            self.note33 = True
            self.note34 = True
            self.note35 = True
            self.note36 = True
            self.note37 = True
            
            
    @api.onchange("all_off")
    def uncheck_all(self):
        if self.all_off:
            self.all_on = False
            self.note1 = False
            self.note3A = False
            self.note3B = False
            self.note3C = False
            self.note3D = False
            self.note3E = False
            self.note4 = False
            self.note5 = False
            self.note6 = False
            self.note7 = False
            self.note8 = False
            self.note8A = False
            self.note9 = False
            self.note10 = False
            self.note11 = False
            self.note12 = False
            self.note13 = False
            self.note14 = False
            self.note15A = False
            self.note15B = False
            self.note16A = False
            self.note16B = False
            self.note16B_BIS = False
            self.note16C = False
            self.note17 = False
            self.note18 = False
            self.note19 = False
            self.note20 = False
            self.note21 = False
            self.note22 = False
            self.note23 = False
            self.note24 = False
            self.note25 = False
            self.note26 = False
            self.note27A = False
            self.note27B = False
            self.note28 = False
            self.note29 = False
            self.note30 = False
            self.note31 = False
            self.note32 = False
            self.note33 = False
            self.note34 = False
            self.note35 = False
            self.note36 = False
            self.note37 = False

    @api.onchange("note1","date_fin")
    def onchange_note1(self):
        line = []
        line2 = []
        if self.note1 is True:
            
            line.append((0,0,{'name':'Dettes financieres et ressources assimilees', 'note':'Note'}))
            line.append((0,0,{'name':'Emprunts obligataires convertibles', 'note':'Note'}))
            line.append((0,0,{'name':'Autres emprunts obligataires', 'note':'Note'}))
            line.append((0,0,{'name':'Emprunts et dettes des etablissements de credit', 'note':'Note'}))
            line.append((0,0,{'name':'Autres dettes financieres', 'note':'Note'}))
            line.append((0,0,{'name':'SOUS TOTAL (1)', 'note':'Note'}))
            line.append((0,0,{'name':'Dettes du passif circulant', 'note':'Note'}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '172%'\
                            group by sub.code) as query")
            dcbi = self.env.cr.fetchone()[0] or 0.0 
            line.append((0,0,{'name':'Dettes de crédit-bail immobilier', 'note':'Note', 'montant':dcbi}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '173%'\
                            group by sub.code) as query")
            dcbm = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Dettes de crédit-bail mobilier', 'note':'Note', 'montant':dcbm}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1762%'\
                            group by sub.code) as query")
            dclv = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Dettes sur contrats de location-vente', 'note':'Note', 'montant':dclv}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1763%'\
                            group by sub.code) as query")
            dcla = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Dettes sur contrats de location-acquisition', 'note':'Note', 'montant':dcla}))
            
            line.append((0,0,{'name':'SOUS TOTAL (2)', 'note':'Note'}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '401%'\
                            group by sub.code) as query")
            fcr = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Fournisseurs et comptes rattachés', 'note':'Note', 'montant':fcr}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '419%'\
                            group by sub.code) as query")
            cli = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Clients', 'note':'Note', 'montant':cli}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '422%' or sub.code like '423%' or sub.code like '425%' or sub.code like '426%' or sub.code like '427%' or sub.code like '429%'\
                            group by sub.code) as query")
            perso = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Personnel', 'note':'Note', 'montant':perso}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '431%' or sub.code like '438%'\
                            group by sub.code) as query")
            ssos = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Sécurité sociale et organismes sociaux', 'note':'Note', 'montant':ssos}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4421%'\
                            group by sub.code) as query")
            etat = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Etat', 'note':'Note', 'montant':etat}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1674%'\
                            group by sub.code) as query")
            oi = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Organismes internationaux', 'note':'Note', 'montant':oi}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '465%' or sub.code like '496%'\
                            group by sub.code) as query")
            ag = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Associés et groupe', 'note':'Note', 'montant':ag}))
            
            st3 = fcr + cli + perso + ssos + etat + oi + ag
            line.append((0,0,{'name':'SOUS TOTAL (3)', 'note':'Note', 'montant':st3}))
            
            line.append((0,0,{'name':'TOTAL (1) + (2) + (3)', 'note':'Note'}))
            
            self.note1_lines1 = line

            line2.append((0,0,{'name':'Engagements consentis à des entites liees'}))
            line2.append((0,0,{'name':'Primes de remboursements, non echues'}))
            line2.append((0,0,{'name':'Avals, cautions, garanties'}))
            line2.append((0,0,{'name':'hypotheques, nantissements, gages, autres'}))
            line2.append((0,0,{'name':'Effets escomptes non echus'}))
            line2.append((0,0,{'name':'Creances commerciales et professionelles cedees'}))
            line2.append((0,0,{'name':'Abandons de creances conditionnels'}))
            self.note1_lines2 = line2
            
    @api.onchange("note1_lines1")
    def note1_line1_subtotal(self):
        st = 0
        cpt = 0
        total = 0
        for line in self.note1_lines1:
            cpt += 1
            if cpt <= 5:
                st += line.montant
            if cpt == 6:
                st1 = st
                line.montant = st1
                st = 0
            if cpt > 6 and cpt <= 11:
                st += line.montant
            if cpt == 12:
                st2 = st
                line.montant = st2
                st = 0
            if cpt > 12 and cpt <= 19:
                st += line.montant
            if cpt == 20:
                st3 = st
                line.montant = st3
                st = 0
            if cpt == 21:
                total = st1 + st2 + st3
                line.montant = total

    @api.onchange("note3A", "date_debut")
    def onchange_note3A(self):
        line = []
        
        if self.note3A is True:
            
            line.append((0,0,{'name':'IMMOBILISATIONS INCORPORELLES'}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '211%'\
                            group by sub.code) as query")
            fdpn = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '211%'\
                            group by sub.code) as query")
            fdp = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Frais de développement et de prospection', 'montant_ouverture':fdpn, 'montant_cloture':fdp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '212%' or sub.code like '213%'\
                            group by sub.code) as query")
            blldsn = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '212%' or sub.code like '213%'\
                            group by sub.code) as query")
            bllds = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Brevet, licences, logiciels et droits similaires', 'montant_ouverture':blldsn, 'montant_cloture':bllds}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '215%' or sub.code like '216%'\
                            group by sub.code) as query")
            fcdbn = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '215%' or sub.code like '216%'\
                            group by sub.code) as query")
            fcdb = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Fonds commercial et droit au bail', 'montant_ouverture':fcdbn, 'montant_cloture':fcdb}))
            
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '218%' or sub.code like '219%'\
                            group by sub.code) as query")
            aiin = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '218%' or sub.code like '219%'\
                            group by sub.code) as query")
            aii = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Autres immobilisations incorporelles', 'montant_ouverture':aiin, 'montant_cloture':aii}))
           
        
            line.append((0,0,{'name':'IMMOBILISATIONS CORPORELLES'}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '221%' or sub.code like '222%'\
                            group by sub.code) as query")
            thipn = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '221%' or sub.code like '222%'\
                            group by sub.code) as query")
            thip = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Terrains hors immeubles de placement', 'montant_ouverture':thipn, 'montant_cloture':thip}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '2881%' or sub.code like '2928%'\
                            group by sub.code) as query")
            tipn = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '2881%' or sub.code like '2928%'\
                            group by sub.code) as query")
            tip = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Terrains - immeubles de placement', 'montant_ouverture':tipn, 'montant_cloture':tip}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '231%' or sub.code like '232%' or sub.code like '233%' or sub.code like '237%' or sub.code like '2391%' \
                            group by sub.code) as query")
            akn_brut = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '231%' or sub.code like '232%' or sub.code like '233%' or sub.code like '237%' or sub.code like '2391%' \
                            group by sub.code) as query")
            ak_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Batiments hors immeubles de placement', 'montant_ouverture':akn_brut, 'montant_cloture':ak_brut}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '2315%' or sub.code like '2325%'\
                            group by sub.code) as query")
            bipn = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '2315%' or sub.code like '2325%'\
                            group by sub.code) as query")
            bip = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Batiments-immeubles de placement', 'montant_ouverture':bipn, 'montant_cloture':bip}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '234%' or sub.code like '235%' or sub.code like '238%' or sub.code like '2392%' or sub.code like '2393%' \
                            group by sub.code) as query")
            aln_brut = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '234%' or sub.code like '235%' or sub.code like '238%' or sub.code like '2392%' or sub.code like '2393%' \
                            group by sub.code) as query")
            al_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Aménagements, agencements et installations', 'montant_ouverture':aln_brut, 'montant_cloture':al_brut}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '24%' and sub.code not like '245%' and sub.code not like '2495%' \
                            group by sub.code) as query")
            amn_brut = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '24%' and sub.code not like '245%' and sub.code not like '2495%' \
                            group by sub.code) as query")
            am_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Matériel, mobilier et actifs biologiques', 'montant_ouverture':amn_brut, 'montant_cloture':am_brut}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '245%'\
                            group by sub.code) as query")
            mtn = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '245%'\
                            group by sub.code) as query")
            mt = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Matériel de transport', 'montant_ouverture':mtn, 'montant_cloture':mt}))
            
            
            line.append((0,0,{'name':'AVANCES ET ACOMPTES VERSES SUR IMMOBILISATTION'}))
            line.append((0,0,{'name':'IMMOBILISATIONS FINANCIERES'}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '261%' or sub.code like '262%' or sub.code like '263%' or sub.code like '264%'\
                            group by sub.code) as query")
            tpn = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '261%' or sub.code like '262%' or sub.code like '263%' or sub.code like '264%'\
                            group by sub.code) as query")
            tp = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Titres de participation', 'montant_ouverture':tpn, 'montant_cloture':tp}))
            
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '270%'\
                            group by sub.code) as query")
            aifn = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '270%'\
                            group by sub.code) as query")
            aif = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Autres immobilisations financiéres', 'montant_ouverture':aifn, 'montant_cloture':aif}))
            
            self.note3A_lines = line

    @api.onchange("note3B", "date_debut", "date_fin")
    def onchange_note3B(self):
        line = []
        if self.note3B is True:
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '212%' or sub.code like '213%' or sub.code like '214%' or sub.code like '2193%' \
                            group by sub.code) as query")
            afn_brut = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '212%' or sub.code like '213%' or sub.code like '214%' or sub.code like '2193%' \
                            group by sub.code) as query")
            af_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Brevets, licences, logiciels et droits similaires', 'montant_ouverture':afn_brut, 'montant_cloture':af_brut}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '215%' or sub.code like '216%' \
                            group by sub.code) as query")
            agn_brut = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '215%' or sub.code like '216%' \
                            group by sub.code) as query")
            ag_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Fonds commercial et droit au bail', 'montant_ouverture':agn_brut, 'montant_cloture':ag_brut}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '217%' or sub.code like '218%'and sub.code not like '2181%' or sub.code like '2198%'\
                            group by sub.code) as query")
            ahn_brut = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '217%' or sub.code like '218%'and sub.code not like '2181%' or sub.code like '2198%'\
                            group by sub.code) as query")
            ah_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Autres immobilisations corporelles', 'montant_ouverture':ahn_brut, 'montant_cloture':ah_brut}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '22%' \
                            group by sub.code) as query")
            ajn_brut = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '22%' \
                            group by sub.code) as query")
            aj_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Terrains', 'montant_ouverture':ajn_brut, 'montant_cloture':aj_brut}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '231%' or sub.code like '232%' or sub.code like '233%' or sub.code like '237%' or sub.code like '2391%' \
                            group by sub.code) as query")
            akn_brut = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '231%' or sub.code like '232%' or sub.code like '233%' or sub.code like '237%' or sub.code like '2391%' \
                            group by sub.code) as query")
            ak_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Bâtiments', 'montant_ouverture':akn_brut, 'montant_cloture':ak_brut}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '234%' or sub.code like '235%' or sub.code like '238%' or sub.code like '2392%' or sub.code like '2393%' \
                            group by sub.code) as query")
            aln_brut = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '234%' or sub.code like '235%' or sub.code like '238%' or sub.code like '2392%' or sub.code like '2393%' \
                            group by sub.code) as query")
            al_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Aménagements, agencements et installations', 'montant_ouverture':aln_brut, 'montant_cloture':al_brut}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '24%' and sub.code not like '245%' and sub.code not like '2495%' \
                            group by sub.code) as query")
            amn_brut = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '24%' and sub.code not like '245%' and sub.code not like '2495%' \
                            group by sub.code) as query")
            am_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Matériel, mobilier et actifs biologiques', 'montant_ouverture':amn_brut, 'montant_cloture':am_brut}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '245%' or sub.code like '2495%' \
                            group by sub.code) as query")
            ann_brut = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '245%' or sub.code like '2495%' \
                            group by sub.code) as query")
            an_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Matériels de transport', 'montant_ouverture':ann_brut, 'montant_cloture':an_brut}))
            
            self.note3B_lines = line

    @api.onchange("note3C", "date_debut", "date_fin")
    def onchange_note3C(self):
        line = []
        if self.note3C is True:
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '2181%' or sub.code like '211%' or sub.code like '2191%' \
                            group by sub.code) as query")
            aen_brut = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '2181%' or sub.code like '211%' or sub.code like '2191%' \
                            group by sub.code) as query")
            ae_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Frais de développement et de prospection', 'amortissement_ouverture': aen_brut, 'amortissement_cloture':ae_brut}))
            
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '212%' or sub.code like '213%' or sub.code like '214%' or sub.code like '2193%' \
                            group by sub.code) as query")
            afn_brut = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '212%' or sub.code like '213%' or sub.code like '214%' or sub.code like '2193%' \
                            group by sub.code) as query")
            af_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Brevet, licences, logiciels et droits similaires', 'amortissement_ouverture': afn_brut, 'amortissement_cloture':af_brut}))
            
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '215%' or sub.code like '216%' \
                            group by sub.code) as query")
            agn_brut = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '215%' or sub.code like '216%' \
                            group by sub.code) as query")
            ag_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Fonds commercial et droit au bail', 'amortissement_ouverture': agn_brut, 'amortissement_cloture':ag_brut}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '217%' or sub.code like '218%'and sub.code not like '2181%' or sub.code like '2198%'\
                            group by sub.code) as query")
            ahn_brut = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '217%' or sub.code like '218%'and sub.code not like '2181%' or sub.code like '2198%'\
                            group by sub.code) as query")
            ah_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Autres immobilisations incorporelles', 'amortissement_ouverture': ahn_brut, 'amortissement_cloture':ah_brut}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '22%' or sub.code like '282%' or sub.code like '292%' \
                            group by sub.code) as query")
            ajn_brut = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '22%' or sub.code like '282%' or sub.code like '292%' \
                            group by sub.code) as query")
            aj_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Terrains hors immeubles de placement', 'amortissement_ouverture': ajn_brut, 'amortissement_cloture':aj_brut}))
            
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '2881%' or sub.code like '2928%'\
                            group by sub.code) as query")
            tip1n = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '2881%' or sub.code like '2928%'\
                            group by sub.code) as query")
            tip1 = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Terrains - immeubles de placement', 'amortissement_ouverture': tip1n, 'amortissement_cloture':tip1}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '231%' or sub.code like '232%' or sub.code like '233%' or sub.code like '237%' or sub.code like '2391%' \
                            group by sub.code) as query")
            akn_brut = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '231%' or sub.code like '232%' or sub.code like '233%' or sub.code like '237%' or sub.code like '2391%' \
                            group by sub.code) as query")
            ak_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Batiments hors immeubles de placement', 'amortissement_ouverture': akn_brut, 'amortissement_cloture':ak_brut}))
            
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '2831%' or sub.code like '2832%'\
                            group by sub.code) as query")
            bip1n = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '2831%' or sub.code like '2832%'\
                            group by sub.code) as query")
            bip1 = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Batiments-immeubles de placement', 'amortissement_ouverture': bip1n, 'amortissement_cloture':bip1}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '234%' or sub.code like '235%' or sub.code like '238%' or sub.code like '2392%' or sub.code like '2393%' \
                            group by sub.code) as query")
            aln_brut = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '234%' or sub.code like '235%' or sub.code like '238%' or sub.code like '2392%' or sub.code like '2393%' \
                            group by sub.code) as query")
            al_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Aménagements, agencements et installations', 'amortissement_ouverture': aln_brut, 'amortissement_cloture':al_brut}))
            
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '24%' and sub.code not like '245%' and sub.code not like '2495%' \
                            group by sub.code) as query")
            amn_brut = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '24%' and sub.code not like '245%' and sub.code not like '2495%' \
                            group by sub.code) as query")
            am_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Matériel, mobilier et actifs biologiques', 'amortissement_ouverture': amn_brut, 'amortissement_cloture':am_brut}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '245%' or sub.code like '2495%' \
                            group by sub.code) as query")
            ann_brut = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '245%' or sub.code like '2495%' \
                            group by sub.code) as query")
            an_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Matériels de transport', 'amortissement_ouverture': ann_brut, 'amortissement_cloture':an_brut}))
            
            self.note3C_lines = line

    @api.onchange("note3D", "date_debut")
    def onchange_note3D(self):
        line = []
        if self.note3D is True:
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '2181%' or sub.code like '211%' or sub.code like '2191%' \
                            group by sub.code) as query")
            ae_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Frais de développement et de prospection', 'montant': ae_brut}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '212%' or sub.code like '213%' or sub.code like '214%' or sub.code like '2193%' \
                            group by sub.code) as query")
            af_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Brevet, licences, logiciels et droits similaires', 'montant': af_brut}))
            
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '215%' or sub.code like '216%' \
                            group by sub.code) as query")
            ag_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Fonds commercial et droit au bail', 'montant': ag_brut}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '217%' or sub.code like '218%'and sub.code not like '2181%' or sub.code like '2198%'\
                            group by sub.code) as query")
            ah_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Autres immobilisations incorporelles', 'montant': ah_brut}))
            
            stii = ae_brut + af_brut + ag_brut + ah_brut
            line.append((0,0,{'name':'SOUS TOTAL: IMMOBILISATION INCORPORELLES', 'montant':stii}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '22%' \
                            group by sub.code) as query")
            aj_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Terrains', 'montant': aj_brut}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '231%' or sub.code like '232%' or sub.code like '233%' or sub.code like '237%' or sub.code like '2391%' \
                            group by sub.code) as query")
            ak_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Bâtiments',  'montant': ak_brut}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '234%' or sub.code like '235%' or sub.code like '238%' or sub.code like '2392%' or sub.code like '2393%' \
                            group by sub.code) as query")
            al_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Aménagements, agencements et installations', 'montant': al_brut}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '24%' and sub.code not like '245%' and sub.code not like '2495%' \
                            group by sub.code) as query")
            am_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Matériel, mobilier et actifs biologiques', 'montant': am_brut}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '245%' or sub.code like '2495%' \
                            group by sub.code) as query")
            an_brut = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Matériels de transport', 'montant': an_brut}))
            
            stic = aj_brut + ak_brut + al_brut + am_brut + an_brut
            line.append((0,0,{'name':'SOUS TOTAL: IMMOBILISATION CORPORELLES', 'montant':stic}))
            
            line.append((0,0,{'name':'Titres de participations'}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '270%'\
                            group by sub.code) as query")
            aif = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Autres immobilisations financiéres', 'montant': aif}))
            
            stif = aif 
            line.append((0,0,{'name':'SOUS TOTAL: IMMOBILISATION FINANCIERES', 'montant':stic}))
            
            tg = stii + stic + stif
            line.append((0,0,{'name':'TOTAL GENERAL', 'montant':tg}))
            
            self.note3D_lines = line

    @api.onchange("note3E")
    def onchange_note3E(self):
        line = []
        if self.note3E is True:
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':'Total écarts de réévaluation'}))
            line.append((0,0,{'name':'Total Provisions spéciales de réévaluation'}))
            line.append((0,0,{'name':'Montant de l’écart incorporé au capital'}))
            self.note3E_lines = line

    @api.onchange("note4", "date_debut", "date_fin")
    def onchange_note4(self):
        line = []
        line2 = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note4 is True:
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '26%'\
                            group by sub.code) as query")
            tp = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '26%'\
                            group by sub.code) as query")
            tpn = self.env.cr.fetchone()[0] or 0.0
            if tpn != 0:
                vtp = ((tp - tpn) / tpn) * 100
            else:
                vtp = 0
            line.append((0,0,{'name':'Titre de participation', 'annee_n':tp, 'annee_n1':tpn, 'variation':vtp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '271%'\
                            group by sub.code) as query")
            pc = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '271%'\
                            group by sub.code) as query")
            pcn = self.env.cr.fetchone()[0] or 0.0
            if pcn != 0:
                vpc = ((pc - pcn) / pcn) * 100
            else:
                vpc = 0
            line.append((0,0,{'name':'Prêts et créances', 'annee_n':pc, 'annee_n1':pcn, 'variation':vpc}))
            
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '272%'\
                            group by sub.code) as query")
            pp = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '272%'\
                            group by sub.code) as query")
            ppn = self.env.cr.fetchone()[0] or 0.0
            if ppn != 0:
                vpp = ((pp - ppn) / ppn) * 100
            else:
                vpp = 0
            line.append((0,0,{'name':'Prêts au personnel', 'annee_n':pp, 'annee_n1':ppn, 'variation':vpp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '273%'\
                            group by sub.code) as query")
            ce = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '273%'\
                            group by sub.code) as query")
            cen = self.env.cr.fetchone()[0] or 0.0
            if cen != 0:
                vce = ((ce - cen) / cen) * 100
            else:
                vce = 0
            line.append((0,0,{'name':'Créances sur l’état', 'annee_n':ce, 'annee_n1':cen, 'variation':vce}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '274%'\
                            group by sub.code) as query")
            ti = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '274%'\
                            group by sub.code) as query")
            tin = self.env.cr.fetchone()[0] or 0.0
            if tin != 0:
                vti = ((ti - tin) / tin) * 100
            else:
                vti = 0
            line.append((0,0,{'name':'Titres immobilisés', 'annee_n':ti, 'annee_n1':tin, 'variation':vti}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '275%'\
                            group by sub.code) as query")
            dc = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '275%'\
                            group by sub.code) as query")
            dcn = self.env.cr.fetchone()[0] or 0.0
            if dcn != 0:
                vdc = ((dc - dcn) / dcn) * 100
            else:
                vdc = 0
            line.append((0,0,{'name':'Dépôts et cautionnement', 'annee_n':dc, 'annee_n1':dcn, 'variation':vdc}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '276%'\
                            group by sub.code) as query")
            ic = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '276%'\
                            group by sub.code) as query")
            icn = self.env.cr.fetchone()[0] or 0.0
            if icn != 0:
                vic = ((ic - icn) / icn) * 100
            else:
                vic = 0
            line.append((0,0,{'name':'Intérêts courus', 'annee_n':ic, 'annee_n1':icn, 'variation':vic}))
            
            tb = tp + pc + pp + ce + ti + dc + ic 
            tbn = tpn + pcn + ppn + cen + tin + dcn + icn
            if tbn != 0:
                vtb = ((tb - tbn) / tbn) * 100
            else:
                vtb = 0
            line.append((0,0,{'name':'TOTAL BRUT', 'annee_n':tb, 'annee_n1':tbn, 'variation':vtb}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '296%'\
                            group by sub.code) as query")
            dtp = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '296%'\
                            group by sub.code) as query")
            dtpn = self.env.cr.fetchone()[0] or 0.0
            if dtpn != 0:
                vdtp = ((dtp - dtpn) / dtpn) * 100
            else:
                vdtp = 0
            
            line.append((0,0,{'name':'Dépréciations titres de participation', 'annee_n':dtp, 'annee_n1':dtpn, 'variation':vdtp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '296%'\
                            group by sub.code) as query")
            dai = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '296%'\
                            group by sub.code) as query")
            dain = self.env.cr.fetchone()[0] or 0.0
            if dain != 0:
                vdai = ((dai - dain) / dain) * 100
            else:
                vdai = 0
            
            line.append((0,0,{'name':'Dépréciations autres immobilisations', 'annee_n':dai, 'annee_n1':dain, 'variation':vdai}))
            
            line.append((0,0,{'name':'TOTAL NET DEPRECIATION', 'annee_n':dai, 'annee_n1':dain, 'variation':vdai}))
            
            self.note4_lines1 = line

            line2.append((0,0,{'name':''}))
            self.note4_lines2 = line2

    @api.onchange("note5")
    def onchange_note5(self):
        line = []
        line2 = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note5 is True:
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '485%'\
                            group by sub.code) as query")
            cci = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '485%'\
                            group by sub.code) as query")
            ccin = self.env.cr.fetchone()[0] or 0.0
            if ccin != 0:
                vcci = ((cci - ccin) / ccin) * 100
            else:     
                vcci = 0
            line.append((0,0,{'name':'Créances sur cession d’immobilisation', 'annee_n':cci, 'annee_n1':ccin, 'variation':vcci}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '488%'\
                            group by sub.code) as query")
            aho = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '488%'\
                            group by sub.code) as query")
            ahon = self.env.cr.fetchone()[0] or 0.0
            
            if ahon != 0:
                vaho = ((aho - ahon) / ahon) * 100
            else:     
                vaho = 0
            line.append((0,0,{'name':'Autres créances hors activités ordinaires', 'annee_n':aho, 'annee_n1':ahon, 'variation':vaho}))
            
            tbrut = cci + aho
            tbrutn = ccin + ahon
            if tbrutn != 0:
                vtbrut = ((tbrut - tbrutn) / tbrutn) * 100
            else:     
                vtbrut = 0
            line.append((0,0,{'name':'TOTAL BRUT', 'annee_n':tbrut, 'annee_n1':tbrutn, 'variation':vtbrut}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '49%'\
                            group by sub.code) as query")
            dch = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '49%'\
                            group by sub.code) as query")
            dchn = self.env.cr.fetchone()[0] or 0.0
            if dchn != 0:
                vdch = ((dch - dchn) / dchn) * 100
            else:     
                vdch = 0
            line.append((0,0,{'name':'Dépréciations des créances HAO', 'annee_n':dch, 'annee_n1':dchn, 'variation':vdch}))
            
            line.append((0,0,{'name':'TOTAL NET DEPRECIATIONS', 'annee_n':dch, 'annee_n1':dchn, 'variation':vdch}))
            self.note5_lines1 = line
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '481%'\
                            group by sub.code) as query")
            fi = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '481%'\
                            group by sub.code) as query")
            fin = self.env.cr.fetchone()[0] or 0.0
            if fin != 0:
                vfi = ((fi - fin) / fin) * 100
            else:     
                vfi = 0
            line2.append((0,0,{'name':'Fournisseurs d’investissement', 'annee_n':fi, 'annee_n1':fin, 'variation':vfi}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '482%'\
                            group by sub.code) as query")
            fip = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '482%'\
                            group by sub.code) as query")
            fipn = self.env.cr.fetchone()[0] or 0.0
            if fipn != 0:
                vfip = ((fip - fipn) / fipn) * 100
            else:     
                vfip = 0
            line2.append((0,0,{'name':'Fournisseurs d’investissement effet a payer', 'annee_n':fip, 'annee_n1':fipn, 'variation':vfip}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '482%'\
                            group by sub.code) as query")
            fifp = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '482%'\
                            group by sub.code) as query")
            fifpn = self.env.cr.fetchone()[0] or 0.0
            if fifpn != 0:
                vfifp = ((fifp - fifpn) / fifpn) * 100
            else:     
                vfifp = 0
            line2.append((0,0,{'name':'Fournisseurs d’investissement factures non parvenues', 'annee_n':fifp, 'annee_n1':fifpn, 'variation':vfifp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4813%'\
                            group by sub.code) as query")
            vril = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4813%'\
                            group by sub.code) as query")
            vriln = self.env.cr.fetchone()[0] or 0.0
            if vriln != 0:
                vvril = ((vril - vriln) / vriln) * 100
            else:     
                vvril = 0
            line2.append((0,0,{'name':'Versements restant a effectuer sur titres de participation et titres immobilises non liberes', 'annee_n':vril, 'annee_n1':vriln, 'variation':vvril}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '484%'\
                            group by sub.code) as query")
            ado = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '484%'\
                            group by sub.code) as query")
            adon = self.env.cr.fetchone()[0] or 0.0
            if adon != 0:
                vado = ((ado - adon) / adon) * 100
            else:     
                vado = 0
            line2.append((0,0,{'name':'Autres dettes hors activites ordinaires', 'annee_n':ado, 'annee_n1':adon, 'variation':vado}))
            
            total = fi + fip + fifp + vril + ado
            totaln = fin + fipn + fifpn + vriln + adon
            if totaln != 0:
                vtotal = ((total - totaln) / totaln) * 100
            else:     
                vtotal = 0
            line2.append((0,0,{'name':'Total', 'annee_n':total, 'annee_n1':totaln, 'variation':vtotal}))
            
            self.note5_lines2 = line2


    @api.onchange("note6")
    def onchange_note6(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note6 is True:
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '31%'\
                            group by sub.code) as query")
            md = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '31%'\
                            group by sub.code) as query")
            mdn = self.env.cr.fetchone()[0] or 0.0
            if mdn != 0:
                vmd = ((md - mdn) / mdn) * 100
            else:     
                vmd = 0
            line.append((0,0,{'name':'Marchandises', 'annee_n':md, 'annee_n1':mdn, 'variation':vmd}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '32%'\
                            group by sub.code) as query")
            mp = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '32%'\
                            group by sub.code) as query")
            mpn = self.env.cr.fetchone()[0] or 0.0
            if mpn != 0:
                vmp = ((mp - mpn) / mpn) * 100
            else:     
                vmp = 0
            line.append((0,0,{'name':'Matiéres premiéres et fournitures liées', 'annee_n':mp, 'annee_n1':mpn, 'variation':vmp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '33%'\
                            group by sub.code) as query")
            ap = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '33%'\
                            group by sub.code) as query")
            apn = self.env.cr.fetchone()[0] or 0.0
            if apn != 0:
                vap = ((ap - apn) / apn) * 100
            else:     
                vap = 0
            line.append((0,0,{'name':'Autres approvisionnements', 'annee_n':ap, 'annee_n1':apn, 'variation':vap}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '34%'\
                            group by sub.code) as query")
            pc = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '34%'\
                            group by sub.code) as query")
            pcn = self.env.cr.fetchone()[0] or 0.0
            if pcn != 0:
                vpc = ((pc - pcn) / pcn) * 100
            else:     
                vpc = 0
            line.append((0,0,{'name':'Produits en cours', 'annee_n':pc, 'annee_n1':pcn, 'variation':vpc}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '35%'\
                            group by sub.code) as query")
            sc = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '35%'\
                            group by sub.code) as query")
            scn = self.env.cr.fetchone()[0] or 0.0
            if scn != 0:
                vsc = ((sc - scn) / scn) * 100
            else:     
                vsc = 0
            line.append((0,0,{'name':'Services en cours', 'annee_n':sc, 'annee_n1':scn, 'variation':vsc}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '36%'\
                            group by sub.code) as query")
            pf = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '36%'\
                            group by sub.code) as query")
            pfn = self.env.cr.fetchone()[0] or 0.0
            if pfn != 0:
                vpf = ((pf - pfn) / pfn) * 100
            else:     
                vpf = 0
            line.append((0,0,{'name':'Produits finis', 'annee_n':pf, 'annee_n1':pfn, 'variation':vpf}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '37%'\
                            group by sub.code) as query")
            pi = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '37%'\
                            group by sub.code) as query")
            pin = self.env.cr.fetchone()[0] or 0.0
            if pin != 0:
                vpi = ((pi - pin) / pin) * 100
            else:     
                vpi = 0
            line.append((0,0,{'name':'Produits intermédiaires', 'annee_n':pi, 'annee_n1':pin, 'variation':vpi}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '38%'\
                            group by sub.code) as query")
            scd = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '38%'\
                            group by sub.code) as query")
            scdn = self.env.cr.fetchone()[0] or 0.0
            if scdn != 0:
                vscd = ((scd - scdn) / scdn) * 100
            else:     
                vscd = 0
            line.append((0,0,{'name':'Stocks en cours de route, en consignation ou en dépôt', 'annee_n':scd, 'annee_n1':scdn, 'variation':vscd}))
            
            tbrutc = md + mp + ap + pc + sc + pf + pi +scd
            tbrutcn = mdn + mpn + apn + pcn + scn + pfn + pin + scdn
            if tbrutcn != 0:
                vtbrutc = ((tbrutc - tbrutcn) / tbrutcn) * 100
            else:     
                vtbrutc = 0
            line.append((0,0,{'name':'TOTAL BRUT STOCKS ET EN COURS', 'annee_n':tbrutc, 'annee_n1':tbrutcn, 'variation':vtbrutc}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '39%'\
                            group by sub.code) as query")
            ds = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '39%'\
                            group by sub.code) as query")
            dsn = self.env.cr.fetchone()[0] or 0.0
            if dsn != 0:
                vds = ((ds - dsn) / dsn) * 100
            else:     
                vds = 0
            line.append((0,0,{'name':'Dépréciations des stocks', 'annee_n':ds, 'annee_n1':dsn, 'variation':vds}))
            
            line.append((0,0,{'name':'TOTAL NET DEPRECIATION', 'annee_n':ds, 'annee_n1':dsn, 'variation':vds}))
            
            self.note6_lines = line


    @api.onchange("note7")
    def onchange_note7(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note7 is True:
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '411%'\
                            group by sub.code) as query")
            hrpg = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '411%'\
                            group by sub.code) as query")
            hrpgn = self.env.cr.fetchone()[0] or 0.0
            if hrpgn != 0:
                vhrpg = ((hrpg - hrpgn) / hrpgn) * 100
            else:     
                vhrpg = 0
            line.append((0,0,{'name':'Clients (hors réserves de propriété groupe)', 'annee_n':hrpg, 'annee_n1':hrpgn, 'variation':vhrpg}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4121%'\
                            group by sub.code) as query")
            cer = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4121%'\
                            group by sub.code) as query")
            cern = self.env.cr.fetchone()[0] or 0.0
            if cern != 0:
                vcer = ((cer - cern) / cern) * 100  
            else:     
                vcer = 0
            line.append((0,0,{'name':'Clients effets à recevoir (hors réserves de propriété groupe)', 'annee_n':cer, 'annee_n1':cern, 'variation':vcer}))
            
            line.append((0,0,{'name':'Clients et effets à recevoir avec réserves de propriété'}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4122%'\
                            group by sub.code) as query")
            cerg = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4122%'\
                            group by sub.code) as query")
            cergn = self.env.cr.fetchone()[0] or 0.0
            if cergn != 0:
                vcer = ((cerg - cergn) / cergn) * 100
            else:     
                vcerg = 0
            line.append((0,0,{'name':'Clients et effets à recevoir Groupe', 'annee_n':cerg, 'annee_n1':cergn, 'variation':vcerg}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '414%'\
                            group by sub.code) as query")
            cci = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '414%'\
                            group by sub.code) as query")
            ccin = self.env.cr.fetchone()[0] or 0.0
            if ccin != 0:
                vcci = ((cci - ccin) / ccin) * 100 
            else:     
                vcci = 0
            line.append((0,0,{'name':'Créances sur cession d’immobilisation', 'annee_n':cci, 'annee_n1':ccin, 'variation':vcci}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '415%'\
                            group by sub.code) as query")
            cee = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '415%'\
                            group by sub.code) as query")
            ceen = self.env.cr.fetchone()[0] or 0.0
            if ceen != 0:
                vcee = ((cee - ceen) / ceen) * 100
            else:     
                vcee = 0
            line.append((0,0,{'name':'Clients effets escomptés et non échus', 'annee_n':cee, 'annee_n1':ceen, 'variation':vcee}))
            
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4181%' or sub.code like '4186%'\
                            group by sub.code) as query")
            cld = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4181%' or sub.code like '4186%'\
                            group by sub.code) as query")
            cldn = self.env.cr.fetchone()[0] or 0.0
            if cldn != 0:
                vcld = ((cld - cldn) / cldn) * 100
            else:     
                vcld = 0
            line.append((0,0,{'name':'Créances litigieuses ou douteuses', 'annee_n':cld, 'annee_n1':cldn, 'variation':vcld}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '418%'\
                            group by sub.code) as query")
            cpr = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '418%'\
                            group by sub.code) as query")
            cprn = self.env.cr.fetchone()[0] or 0.0
            if cprn != 0:
                vcpr = ((cpr - cprn) / cprn) * 100
            else:     
                vcpr = 0
            line.append((0,0,{'name':'Clients produits à recevoir', 'annee_n':cpr, 'annee_n1':cprn, 'variation':vcpr}))
            
            tbc = hrpg + cer + cerg + cci + cee + cld + cpr
            tbcn = hrpgn + cern + cergn + ccin + ceen + cldn + cprn
            if tbcn != 0:
                vtbc = ((tbc - tbcn) / tbcn) * 100
            else:     
                vtbc = 0
            line.append((0,0,{'name':'TOTAL BRUT CLIENTS', 'annee_n':tbc, 'annee_n1':tbcn, 'variation':vtbc}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '491%'\
                            group by sub.code) as query")
            dcc = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '491%'\
                            group by sub.code) as query")
            dccn = self.env.cr.fetchone()[0] or 0.0
            if dccn != 0:
                vdcc = ((dcc - dccn) / dccn) * 100
            else:     
                vdcc = 0
            line.append((0,0,{'name':'Dépréciations des comptes clients', 'annee_n':dcc, 'annee_n1':dccn, 'variation':vdcc}))
            
            line.append((0,0,{'name':'TOTAL NET DEPRECIATION', 'annee_n':dcc, 'annee_n1':dccn, 'variation':vdcc}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4191%'\
                            group by sub.code) as query")
            carhg = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4191%'\
                            group by sub.code) as query")
            carhgn = self.env.cr.fetchone()[0] or 0.0
            if carhgn != 0:
                vcarhg = ((carhg - carhgn) / carhgn) * 100 
            else:     
                vcarhg = 0
            line.append((0,0,{'name':'Clients, avances reçues hors groupe', 'annee_n':carhg, 'annee_n1':carhgn, 'variation':vcarhg}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4192%'\
                            group by sub.code) as query")
            carg = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4192%'\
                            group by sub.code) as query")
            cargn = self.env.cr.fetchone()[0] or 0.0
            if cargn != 0:
                vcarg = ((carg - cargn) / cargn) * 100
            else:     
                vcarg = 0
            line.append((0,0,{'name':'Clients, avances reçues groupe', 'annee_n':carg, 'annee_n1':cargn, 'variation':vcarg}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4194%' or sub.code like '4198%'\
                            group by sub.code) as query")
            acc = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4194%' or sub.code like '4198%'\
                            group by sub.code) as query")
            accn = self.env.cr.fetchone()[0] or 0.0
            if accn != 0:
                vacc = ((acc - accn) / accn) * 100
            else:     
                vacc = 0
            line.append((0,0,{'name':'Autres clients crédteurs', 'annee_n':acc, 'annee_n1':accn, 'variation':vacc}))
            
            tcc = carhg + carg + acc
            tccn = carhgn + cargn + accn
            if tccn != 0:
                vtcc = ((tcc - tccn) / tccn) * 100
            else:     
                vtcc = 0
            line.append((0,0,{'name':'TOTAL CLIENTS CREDITEURS', 'annee_n':tcc, 'annee_n1':tccn, 'variation':vtcc}))
            
            self.note7_lines = line


    @api.onchange("note8")
    def onchange_note8(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note8 is True:     
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '421%'\
                            group by sub.code) as query")
            perso = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '421%'\
                            group by sub.code) as query")
            person = self.env.cr.fetchone()[0] or 0.0
            if person != 0:
                vperso = ((perso - person) / person) * 100
            else:     
                vperso = 0
            line.append((0,0,{'name':'Personnel', 'annee_n':perso, 'annee_n1':person, 'variation':vperso}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '43%'\
                            group by sub.code) as query")
            os = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '43%'\
                            group by sub.code) as query")
            osn = self.env.cr.fetchone()[0] or 0.0
            if osn != 0:
                vos = ((os - osn) / osn) * 100
            else:     
                vos = 0
            line.append((0,0,{'name':'Organismes sociaux', 'annee_n':os, 'annee_n1':osn, 'variation':vos}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '44%'\
                            group by sub.code) as query")
            ecp = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '44%'\
                            group by sub.code) as query")
            ecpn = self.env.cr.fetchone()[0] or 0.0
            if ecpn != 0:
                vecp = ((ecp - ecpn) / ecpn) * 100
            else:     
                vecp = 0
            line.append((0,0,{'name':'Etat et Collectivités publiques', 'annee_n':ecp, 'annee_n1':ecpn, 'variation':vecp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '45%'\
                            group by sub.code) as query")
            oi = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '45%'\
                            group by sub.code) as query")
            oin = self.env.cr.fetchone()[0] or 0.0
            if oin != 0:
                voi = ((oi - oin) / oin) * 100
            else:     
                voi = 0
            line.append((0,0,{'name':'Organismes internationaux', 'annee_n':oi, 'annee_n1':oin, 'variation':voi}))
              
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '46%'\
                            group by sub.code) as query")
            asg = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '46%'\
                            group by sub.code) as query")
            asgn = self.env.cr.fetchone()[0] or 0.0
            if asgn != 0:
                vasg = ((asg - asgn) / asgn) * 100
            else:     
                vasg = 0
            line.append((0,0,{'name':'Apporteurs, associés et groupe', 'annee_n':asg, 'annee_n1':asgn, 'variation':vasg}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '475%'\
                            group by sub.code) as query")
            ctas = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '475%'\
                            group by sub.code) as query")
            ctasn = self.env.cr.fetchone()[0] or 0.0
            if ctasn != 0:
                vctas = ((ctas - ctasn) / ctasn) * 100
            else:     
                vctas = 0
            line.append((0,0,{'name':'Compte transitoire ajustement spécial lié à la révision du SYSCOHADA', 'annee_n':ctas, 'annee_n1':ctasn, 'variation':vctas}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4711%'\
                            group by sub.code) as query")
            add = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4711%'\
                            group by sub.code) as query")
            addn = self.env.cr.fetchone()[0] or 0.0
            if addn != 0:
                vadd = ((add - addn) / addn) * 100
            else:     
                vadd = 0
            line.append((0,0,{'name':'Autres débiteurs divers', 'annee_n':add, 'annee_n1':addn, 'variation':vadd}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '185%'\
                            group by sub.code) as query")
            cpbes = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '185%'\
                            group by sub.code) as query")
            cpbesn = self.env.cr.fetchone()[0] or 0.0
            if cpbesn != 0:
                vcpbes = ((cpbes - cpbesn) / cpbesn) * 100
            else:     
                vcpbes = 0
            line.append((0,0,{'name':'Comptes permanents non bloqués des établissements et des succursales', 'annee_n':cpbes, 'annee_n1':cpbesn, 'variation':vcpbes}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '476%'\
                            group by sub.code) as query")
            cpbes = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '476%'\
                            group by sub.code) as query")
            cpbesn = self.env.cr.fetchone()[0] or 0.0
            if cpbesn != 0:
                vcpbes = ((cpbes - cpbesn) / cpbesn) * 100
            else:     
                vcpbes = 0
            line.append((0,0,{'name':'Comptes de liaison charges et produits', 'annee_n':cpbes, 'annee_n1':cpbesn, 'variation':vcpbes}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '188%'\
                            group by sub.code) as query")
            clsp = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '188%'\
                            group by sub.code) as query")
            clspn = self.env.cr.fetchone()[0] or 0.0
            if clspn != 0:
                vclsp = ((clsp - clspn) / clspn) * 100
            else:     
                vclsp = 0
            line.append((0,0,{'name':'Comptes de liaison des sociétés en participation', 'annee_n':clsp, 'annee_n1':clspn, 'variation':vclsp}))
            
            tac  = perso + os + ecp + asg + ctas + add + cpbes + clsp
            tacn = person + osn + ecpn + asgn + ctasn + addn + cpbesn + clspn
            if tacn != 0:
                vtac = ((tac - tacn) / tacn) * 100
            else:     
                vtac = 0
            line.append((0,0,{'name':'TOTAL AUTRES CREANCES', 'annee_n':tac, 'annee_n1':tacn, 'variation':vtac}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '492%' or sub.code like '493%' or sub.code like '494%' or sub.code like '495%' or sub.code like '496%' or sub.code like '497%' \
                            group by sub.code) as query")
            dac = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '492%' or sub.code like '493%' or sub.code like '494%' or sub.code like '495%' or sub.code like '496%' or sub.code like '497%' \
                            group by sub.code) as query")
            dacn = self.env.cr.fetchone()[0] or 0.0
            if dacn != 0:
                vdac = ((dac - dacn) / dacn) * 100
            else:     
                vdac = 0
            line.append((0,0,{'name':'Dépréciations des autres créances', 'annee_n':dac, 'annee_n1':dacn, 'variation':vdac}))
            line.append((0,0,{'name':'TOTAL NET DE DEPRECIATION', 'annee_n':dac, 'annee_n1':dacn, 'variation':vdac}))
            self.note8_lines = line


    @api.onchange("note8A")
    def onchange_note8A(self):
        line = []
        line2 = []
        if self.date_debut and self.date_fin:
            current_year = self.date_debut.year
        if self.note8A is True:
            line.append((0,0,{'name':'Montant global à étaler au 1er janvier '+str(current_year)}))
            line.append((0,0,{'name':'Durrée d’étalement retenue'}))
            self.note8A_lines1 = line
            
            line2.append((0,0,{'name':'Exercice année '+str(current_year), 'compte1':'60.....', 'compte2':'60.....',}))
            line2.append((0,0,{'name':'Exercice année '+str(current_year), 'compte1':'61.....', 'compte2':'61.....',}))
            line2.append((0,0,{'name':'Exercice année '+str(current_year), 'compte1':'62.....', 'compte2':'62.....',}))
            line2.append((0,0,{'name':'Exercice année '+str(current_year), 'compte1':'63.....', 'compte2':'63.....',}))
            line2.append((0,0,{'name':'Exercice année '+str(current_year)}))
            line2.append((0,0,{'name':''}))
            line2.append((0,0,{'name':'Total exercice '+str(current_year)}))
            line2.append((0,0,{'name':'Total exercice '+str(current_year + 1)}))
            line2.append((0,0,{'name':'Total exercice '+str(current_year + 2)}))
            line2.append((0,0,{'name':'Total exercice '+str(current_year + 3)}))
            line2.append((0,0,{'name':'Total exercice '+str(current_year + 4)}))
            line2.append((0,0,{'name':'Total GENERAL'}))
            self.note8A_lines2 = line2
            
    @api.onchange("note8A_lines2")
    def note8a_line2_subtotal(self):
        cpt = 0
        st1 = 0
        st2 = 0
        st3 = 0
        st4 = 0
        st5 = 0
        st6 = 0
        total_current_year1 = 0
        total_current_year2 = 0
        total_current_year3 = 0
        total1 = 0
        tota2 = 0
        tota3 = 0
        for line in self.note8A_lines2:
            cpt += 1
            if cpt <= 6:
                st1 += line.montant1
                st2 += line.montant2
                st3 += line.montant3
            if cpt == 7:
                total_current_year1 = st1
                total_current_year2 = st2
                total_current_year3 = st3
                line.montant1 = total_current_year1
                line.montant2 = total_current_year2
                line.montant3 = total_current_year3
            if cpt > 7 and cpt < 11:
                st4 += line.montant1
                st5 += line.montant2
                st6 += line.montant3
            if cpt == 12:
                total1 = st4
                total2 = st5
                total3 = st6
                line.montant1 = total_current_year1 + total1
                line.montant2 = total_current_year2 + total2
                line.montant3 = total_current_year3 + total3


    @api.onchange("note9")
    def onchange_note9(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note9 is True:
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '501%'\
                            group by sub.code) as query")
            ttb = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '501%'\
                            group by sub.code) as query")
            ttbn = self.env.cr.fetchone()[0] or 0.0
            if ttbn != 0:
                vttb = ((ttb - ttbn) / ttbn) * 100
            else:     
                vttb = 0
            line.append((0,0,{'name':'Titres de trésor et bons de caisse à court terme', 'annee_n':ttb, 'annee_n1':ttbn, 'variation':vttb}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '502%'\
                            group by sub.code) as query")
            act = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '502%'\
                            group by sub.code) as query")
            actn = self.env.cr.fetchone()[0] or 0.0
            if actn != 0:
                vact = ((act - actn) / actn) * 100
            else:     
                vact = 0
            line.append((0,0,{'name':'Actions', 'annee_n':act, 'annee_n1':actn, 'variation':vact}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '503%'\
                            group by sub.code) as query")
            obl = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '503%'\
                            group by sub.code) as query")
            obln = self.env.cr.fetchone()[0] or 0.0
            if obln != 0:
                vobl = ((obl - obln) / obln) * 100
            else:     
                vobl = 0
            line.append((0,0,{'name':'Obligation', 'annee_n':obl, 'annee_n1':obln, 'variation':vobl}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '504%'\
                            group by sub.code) as query")
            bs = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '504%'\
                            group by sub.code) as query")
            bsn = self.env.cr.fetchone()[0] or 0.0
            if bsn != 0:
                vbs = ((bs - bsn) / bsn) * 100
            else:     
                vbs = 0
            line.append((0,0,{'name':'Bons de souscription', 'annee_n':bs, 'annee_n1':bsn, 'variation':vbs}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '505%'\
                            group by sub.code) as query")
            tnhr = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '505%'\
                            group by sub.code) as query")
            tnhrn = self.env.cr.fetchone()[0] or 0.0
            if tnhrn != 0:
                vtnhr = ((tnhr - tnhrn) / tnhrn) * 100
            else:     
                vtnhr = 0
            line.append((0,0,{'name':'Titres négociables hors régions', 'annee_n':tnhr, 'annee_n1':tnhrn, 'variation':vtnhr}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '506%'\
                            group by sub.code) as query")
            ic = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '506%'\
                            group by sub.code) as query")
            icn = self.env.cr.fetchone()[0] or 0.0
            if icn != 0:
                vic = ((ic - icn) / icn) * 100
            else:     
                vic = 0
            line.append((0,0,{'name':'Intérêts courus', 'annee_n':ic, 'annee_n1':icn, 'variation':vic}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '506%'\
                            group by sub.code) as query")
            ava = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '506%'\
                            group by sub.code) as query")
            avan = self.env.cr.fetchone()[0] or 0.0
            if avan != 0:
                vava = ((ava - avan) / avan) * 100
            else:     
                vava = 0
            line.append((0,0,{'name':'Autres valeurs assimilées', 'annee_n':ava, 'annee_n1':avan, 'variation':vava}))
            
            tbt = ttb + act + obl + bs + tnhr + ic + ava 
            tbtn = ttbn + actn + obln + bsn + tnhrn + icn + avan
            if tbtn != 0:
                vtbt = ((tbt - tbtn) / tbtn) * 100
            else:     
                vtbt = 0
            line.append((0,0,{'name':'TOTAL BRUT TITRES','annee_n':tbt, 'annee_n1':tbtn, 'variation':vtbt}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '590%'\
                            group by sub.code) as query")
            dt = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '590%'\
                            group by sub.code) as query")
            dtn = self.env.cr.fetchone()[0] or 0.0
            if dtn != 0:
                vdt = ((dtn - dtn) / dtn) * 100
            else:     
                vdt = 0
            line.append((0,0,{'name':'Dépréciations des titres', 'annee_n':dt, 'annee_n1':dtn, 'variation':vdt}))
            
            line.append((0,0,{'name':'TOTAL NET DEPRECIATION', 'annee_n':dt, 'annee_n1':dtn, 'variation':vdt}))
            self.note9_lines = line

    @api.onchange("note10")
    def onchange_note10(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note10 is True:
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '511%'\
                            group by sub.code) as query")
            eac = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '511%'\
                            group by sub.code) as query")
            eacn = self.env.cr.fetchone()[0] or 0.0
            if eacn != 0:
                veac = ((eac - eacn) / eacn) * 100
            else:     
                veac = 0
            line.append((0,0,{'name':'Effets à encaisser', 'annee_n':eac, 'annee_n1':eacn, 'variation':veac}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '512%'\
                            group by sub.code) as query")
            eaa = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '512%'\
                            group by sub.code) as query")
            eaan = self.env.cr.fetchone()[0] or 0.0
            if eaan != 0:
                veaa = ((eaa - eaan) / eaan) * 100
            else:     
                veaa = 0
            line.append((0,0,{'name':'Effets à l’encaissement', 'annee_n':eaa, 'annee_n1':eaan, 'variation':veaa}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '513%'\
                            group by sub.code) as query")
            cae = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '513%'\
                            group by sub.code) as query")
            caen = self.env.cr.fetchone()[0] or 0.0
            if caen != 0:
                vcae = ((cae - caen) / caen) * 100
            else:     
                vcae = 0
            line.append((0,0,{'name':'Chéques à encaisser', 'annee_n':cae, 'annee_n1':caen, 'variation':vcae}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '514%'\
                            group by sub.code) as query")
            cale = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '514%'\
                            group by sub.code) as query")
            calen = self.env.cr.fetchone()[0] or 0.0
            if calen != 0:
                vcale = ((cale - calen) / calen) * 100
            else:     
                vcale = 0
            line.append((0,0,{'name':'Chéques à l’encaissement', 'annee_n':cale, 'annee_n1':calen, 'variation':vcale}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '515%'\
                            group by sub.code) as query")
            cce = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '515%'\
                            group by sub.code) as query")
            ccen = self.env.cr.fetchone()[0] or 0.0
            if ccen != 0:
                vcce = ((cce - ccen) / ccen) * 100
            else:     
                vcce = 0
            line.append((0,0,{'name':'Cartes de crédit à encaisser', 'annee_n':cce, 'annee_n1':ccen, 'variation':vcce}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '518%'\
                            group by sub.code) as query")
            ave = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '518%'\
                            group by sub.code) as query")
            aven = self.env.cr.fetchone()[0] or 0.0
            if aven != 0:
                vave = ((ave - aven) / aven) * 100
            else:     
                vave = 0
            line.append((0,0,{'name':'Autres valeurs à encaisser', 'annee_n':ave, 'annee_n1':aven, 'variation':vave}))
            
            tbve = eac + eaa + cae + cale + cce + ave
            tbven = eacn + eaan + caen + calen + ccen + aven
            if tbven != 0:
                vtbve = ((tbve - tbven) / tbven) * 100
            else:     
                vtbve = 0
            line.append((0,0,{'name':'TOTAL BRUT VALEURS A ENCAISSER', 'annee_n':tbve, 'annee_n1':tbven, 'variation':vtbve}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '591%'\
                            group by sub.code) as query")
            dve = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '591%'\
                            group by sub.code) as query")
            dven = self.env.cr.fetchone()[0] or 0.0
            if dven != 0:
                vdve = ((dve - dven) / dven) * 100
            else:     
                vdve = 0
            line.append((0,0,{'name':'Dépréciations des valeurs à encaisser', 'annee_n':dve, 'annee_n1':dven, 'variation':vdve}))
            
            line.append((0,0,{'name':'TOTAL NET DEPRECIATION', 'annee_n':dve, 'annee_n1':dven, 'variation':vdve}))
            self.note10_lines = line


    @api.onchange("note11")
    def onchange_note11(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note11 is True:
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '521%'\
                            group by sub.code) as query")
            bl = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '521%'\
                            group by sub.code) as query")
            bln = self.env.cr.fetchone()[0] or 0.0
            if bln != 0:
                vbl = ((bl - bln) / bln) * 100 
            else:     
                vbl = 0
            line.append((0,0,{'name':'Banques locales', 'annee_n':bl, 'annee_n1':bln, 'variation':vbl}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '522%'\
                            group by sub.code) as query")
            baer = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '522%'\
                            group by sub.code) as query")
            baern = self.env.cr.fetchone()[0] or 0.0
            if baern != 0:
                vbaer = ((baer - baern) / baern) * 100
            else:     
                vbaer = 0
            line.append((0,0,{'name':'Banques autres états région', 'annee_n':baer, 'annee_n1':baern, 'variation':vbaer}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '525%'\
                            group by sub.code) as query")
            bdt = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '525%'\
                            group by sub.code) as query")
            bdtn = self.env.cr.fetchone()[0] or 0.0
            if bdtn != 0:
                vbdt = ((bdt - bdtn) / bdtn) * 100
            else:     
                vbdt = 0
            line.append((0,0,{'name':'Banques, dépôt à terme', 'annee_n':bdt, 'annee_n1':bdtn, 'variation':vbdt}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '523%' or sub.code like '524%'\
                            group by sub.code) as query")
            ab = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '523%' or sub.code like '524%'\
                            group by sub.code) as query")
            abn = self.env.cr.fetchone()[0] or 0.0
            if abn != 0:
                vab = ((ab - abn) / abn) * 100
            else:     
                vab = 0
            line.append((0,0,{'name':'Autres Banques', 'annee_n':ab, 'annee_n1':abn, 'variation':vab}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '526%'\
                            group by sub.code) as query")
            bic = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '526%'\
                            group by sub.code) as query")
            bicn = self.env.cr.fetchone()[0] or 0.0
            if bicn != 0:
                vbic = ((bic - bicn) / bicn) * 100
            else:     
                vbic = 0
            line.append((0,0,{'name':'Banques intérêts courus', 'annee_n':bic, 'annee_n1':bicn, 'variation':vbic}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '531%'\
                            group by sub.code) as query")
            cp = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '531%'\
                            group by sub.code) as query")
            cpn = self.env.cr.fetchone()[0] or 0.0
            if cpn != 0:
                vcp = ((cp - cpn) / cpn) * 100 
            else:     
                vcp = 0
            line.append((0,0,{'name':'Chéques postaux', 'annee_n':cp, 'annee_n1':cpn, 'variation':vcp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '538%'\
                            group by sub.code) as query")
            aef = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '538%'\
                            group by sub.code) as query")
            aefn = self.env.cr.fetchone()[0] or 0.0
            if aefn != 0:
                vaef = ((aef - aefn) / aefn) * 100
            else:     
                vaef = 0
            line.append((0,0,{'name':'Autres établissements financiers', 'annee_n':aef, 'annee_n1':aefn, 'variation':vaef}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '536%'\
                            group by sub.code) as query")
            efic = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '536%'\
                            group by sub.code) as query")
            eficn = self.env.cr.fetchone()[0] or 0.0
            if eficn != 0:
                vefic = ((efic - eficn) / eficn) * 100
            else:     
                vefic = 0
            line.append((0,0,{'name':'Etablissements financiers interêts courus', 'annee_n':efic, 'annee_n1':eficn, 'variation':vefic}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '541%' or sub.code like '542%' or sub.code like '543%' or sub.code like '544%' or sub.code like '545%'\
                            group by sub.code) as query")
            idt = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '541%' or sub.code like '542%' or sub.code like '543%' or sub.code like '544%' or sub.code like '545%'\
                            group by sub.code) as query")
            idtn = self.env.cr.fetchone()[0] or 0.0
            if idtn != 0:
                vidt = ((idt - idtn) / idtn) * 100  
            else:     
                vidt = 0
            line.append((0,0,{'name':'Instruments de trésorerie', 'annee_n':idt, 'annee_n1':idtn, 'variation':vidt}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '571%'\
                            group by sub.code) as query")
            caisse = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '571%'\
                            group by sub.code) as query")
            caissen = self.env.cr.fetchone()[0] or 0.0
            if caissen != 0:
                vcaisse = ((caisse - caissen) / caissen) * 100 
            else:     
                vcaisse = 0
            line.append((0,0,{'name':'Caisse', 'annee_n':caisse, 'annee_n1':caissen, 'variation':vcaisse}))
            
            line.append((0,0,{'name':'Caisse électronique mobile'}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '581%' or sub.code like '582%' or sub.code like '585%' or sub.code like '588%'\
                            group by sub.code) as query")
            rva = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '581%' or sub.code like '582%' or sub.code like '585%' or sub.code like '588%'\
                            group by sub.code) as query")
            rvan = self.env.cr.fetchone()[0] or 0.0
            if rvan != 0:
                vrva = ((rva - rvan) / rvan) * 100
            else:     
                vrva = 0
            line.append((0,0,{'name':'Régies d’avance et virements accréditifs', 'annee_n':rva, 'annee_n1':rvan, 'variation':vrva}))
            
            tbd = bl + baer + bdt + ab + bic + cp + aef + efic + idt + caisse + rva 
            tbdn = bln + baern + bdtn + abn + bicn + cpn + aefn + eficn + idtn + caissen + rvan
            if tbdn != 0:
                vtbd = ((tbd - tbdn) / tbdn) * 100
            else:     
                vtbd = 0             
            line.append((0,0,{'name':'TOTAL BRUT DISPONIBLE', 'annee_n':tbd, 'annee_n1':tbdn, 'variation':vtbd}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '590%' or sub.code like '591%' or sub.code like '592%' or sub.code like '593%' or sub.code like '594%'\
                            group by sub.code) as query")
            dep = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '590%' or sub.code like '591%' or sub.code like '592%' or sub.code like '593%' or sub.code like '594%'\
                            group by sub.code) as query")
            depn = self.env.cr.fetchone()[0] or 0.0
            if depn != 0:
                vdep = ((dep - depn) / depn) * 100
            else:     
                vdep = 0
            line.append((0,0,{'name':'Dépréciations', 'annee_n':dep, 'annee_n1':depn, 'variation':vdep}))
            
            line.append((0,0,{'name':'TOTAL NET DEPRECIATION', 'annee_n':dep, 'annee_n1':depn, 'variation':vdep}))
            self.note11_lines = line

    @api.onchange("note12")
    def onchange_note12(self):
        line = []
        line2 = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note12 is True:
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '478%'\
                            group by sub.code) as query")
            eca = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Ecarts de conversion actif : détailler les créance', 'Montant_en_D':eca}))
            line.append((0,0,{'name':' '}))
            line.append((0,0,{'name':' '}))
            line.append((0,0,{'name':' '}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '479%'\
                            group by sub.code) as query")
            ecp = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Ecarts de conversion passif : détailler les créance', 'Montant_en_D':ecp}))
            line.append((0,0,{'name':' '}))
            line.append((0,0,{'name':' '}))
            line.append((0,0,{'name':' '}))
            self.note12_lines1 = line
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '781%'\
                            group by sub.code) as query")
            tde = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '781%'\
                            group by sub.code) as query")
            tden = self.env.cr.fetchone()[0] or 0.0
            if tden != 0:
                vtde = ((tde - tden) / tden) * 100 
            else:     
                vtde = 0
            line2.append((0,0,{'name':'Transferts de charges d’exploitation : détailler la nature des charges transférées', 'annee_n':tde, 'annee_n1':tden, 'variation':vtde}))
            line2.append((0,0,{'name':' '}))
            line2.append((0,0,{'name':' '}))
            line2.append((0,0,{'name':' '}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '791%'\
                            group by sub.code) as query")
            tcf = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '791%'\
                            group by sub.code) as query")
            tcfn = self.env.cr.fetchone()[0] or 0.0
            if tcfn != 0:
                vtcf = ((tcf - tcfn) / tcfn) * 100
            else:     
                vtcf = 0
            line2.append((0,0,{'name':'Transferts de charges financiéres : détailler la nature des charges transférées', 'annee_n':tcf, 'annee_n1':tcfn, 'variation':vtcf}))
            line2.append((0,0,{'name':' '}))
            line2.append((0,0,{'name':' '}))
            line2.append((0,0,{'name':' '}))
            self.note12_lines2 = line2


    @api.onchange("note13")
    def onchange_note13(self):
        line = []
        if self.note13 is True:
            line.append((0,0,{'name':'Apporteur, capital non appelé'}))
            line.append((0,0,{'name':'TOTAL'}))
            self.note13_lines = line


    @api.onchange("note14")
    def onchange_note14(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note14 is True:
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1051%'\
                            group by sub.code) as query")
            pa = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1051%'\
                            group by sub.code) as query")
            pan = self.env.cr.fetchone()[0] or 0.0
            if pan != 0:
                vpa = ((pa - pan) / pan) * 100
            else:     
                vpa = 0
            line.append((0,0,{'name':'Primes d’apport', 'annee_n':pa, 'annee_n1':pan, 'variation':vpa}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1052%'\
                            group by sub.code) as query")
            pe = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1052%'\
                            group by sub.code) as query")
            pen = self.env.cr.fetchone()[0] or 0.0
            if pen != 0:
                vpe = ((pe - pen) / pen) * 100
            else:     
                vpe = 0
            line.append((0,0,{'name':'Primes d’émission', 'annee_n':pe, 'annee_n1':pen, 'variation':vpe}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1053%'\
                            group by sub.code) as query")
            pf = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1053%'\
                            group by sub.code) as query")
            pfn = self.env.cr.fetchone()[0] or 0.0
            if pfn != 0:
                vpf = ((pf - pfn) / pfn) * 100
            else:     
                vpf = 0
            line.append((0,0,{'name':'Primes de fusion', 'annee_n':pf, 'annee_n1':pfn, 'variation':vpf}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1054%'\
                            group by sub.code) as query")
            pc = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1054%'\
                            group by sub.code) as query")
            pcn = self.env.cr.fetchone()[0] or 0.0
            if pcn != 0:
                vpc = ((pc - pcn) / pcn) * 100 
            else:     
                vpc = 0
            line.append((0,0,{'name':'Primes de conversion', 'annee_n':pc, 'annee_n1':pcn, 'variation':vpc}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1058%'\
                            group by sub.code) as query")
            ap = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1058%'\
                            group by sub.code) as query")
            apn = self.env.cr.fetchone()[0] or 0.0
            if apn != 0:
                vap = ((ap - apn) / apn) * 100
            else:     
                vap = 0
            line.append((0,0,{'name':'Autres primes', 'annee_n':ap, 'annee_n1':apn, 'variation':vap}))
            
            tp = pa + pe + pf + pc + ap
            tpn = pan + pen + pfn + pcn + apn
            if tpn != 0:
                vtp = ((tp - tpn) / tpn) * 100
            else:     
                vtp = 0
            line.append((0,0,{'name':'TOTAL PRIMES', 'annee_n':tp, 'annee_n1':tpn, 'variation':vtp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '111%'\
                            group by sub.code) as query")
            rl = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '111%'\
                            group by sub.code) as query")
            rln = self.env.cr.fetchone()[0] or 0.0
            if rln != 0:
                vrl = ((rl - rln) / rln) * 100
            else:     
                vrl = 0
            line.append((0,0,{'name':'Réserves légales', 'annee_n':rl, 'annee_n1':rln, 'variation':vrl}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '112%'\
                            group by sub.code) as query")
            rs = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '112%'\
                            group by sub.code) as query")
            rsn = self.env.cr.fetchone()[0] or 0.0
            if rsn != 0:
                vrs = ((rs - rsn) / rsn) * 100
            else:     
                vrs = 0
            line.append((0,0,{'name':'Réserves statutaires', 'annee_n':rs, 'annee_n1':rsn, 'variation':vrs}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1131%'\
                            group by sub.code) as query")
            rpnlt = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1131%'\
                            group by sub.code) as query")
            rpnltn = self.env.cr.fetchone()[0] or 0.0
            if rpnltn != 0:
                vrpnlt = ((rpnlt - rpnltn) / rpnltn) * 100
            else:     
                vrpnlt = 0
            line.append((0,0,{'name':'Réserves de plus-values nettes à long terme', 'annee_n':rpnlt, 'annee_n1':rpnltn, 'variation':vrpnlt}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1132%'\
                            group by sub.code) as query")
            agpd = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1132%'\
                            group by sub.code) as query")
            agpdn = self.env.cr.fetchone()[0] or 0.0
            if agpdn != 0:
                vagpd = ((agpd - agpdn) / agpdn) * 100
            else:     
                vagpd = 0
            line.append((0,0,{'name':'d’attribution gratuite d’action au personnel salarié et aux dirigeants', 'annee_n':agpd, 'annee_n1':agpdn, 'variation':vagpd}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1138%'\
                            group by sub.code) as query")
            arr = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1138%'\
                            group by sub.code) as query")
            arrn = self.env.cr.fetchone()[0] or 0.0
            if arrn != 0:
                varr = ((arr - arrn) / arrn) * 100
            else:     
                varr = 0
            line.append((0,0,{'name':'Autres réserves réglementées', 'annee_n':arr, 'annee_n1':arrn, 'variation':varr}))
            
            tri = rl + rs + rpnlt + agpd + arr
            trin = rln + rsn + rpnltn + agpdn + arrn
            if trin != 0:
                vtri = ((tri - trin) / trin) * 100
            else:     
                vtri = 0
            line.append((0,0,{'name':'TOTAL RESERVES INDISPONIBLES', 'annee_n':tri, 'annee_n1':trin, 'variation':vtri}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1138%'\
                            group by sub.code) as query")
            rl = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1138%'\
                            group by sub.code) as query")
            rln = self.env.cr.fetchone()[0] or 0.0
            if rln != 0:
                vrl = ((rl - rln) / rln) * 100
            else:     
                vrl = 0
            line.append((0,0,{'name':'Réserves libres', 'annee_n':rl, 'annee_n1':rln, 'variation':vrl}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1138%'\
                            group by sub.code) as query")
            ra = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1138%'\
                            group by sub.code) as query")
            ran = self.env.cr.fetchone()[0] or 0.0
            if ran != 0:
                vra = ((ra - ran) / ran) * 100
            else:     
                vra = 0
            line.append((0,0,{'name':'Report à nouveau', 'annee_n':ra, 'annee_n1':ran, 'variation':vra}))
            self.note14_lines = line



    @api.onchange("note15A")
    def onchange_note15A(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note15A is True:
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1411%'\
                            group by sub.code) as query")
            etat = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1411%'\
                            group by sub.code) as query")
            etatn = self.env.cr.fetchone()[0] or 0.0
            if etatn != 0:
                vetat = (etat - etatn) / etatn
            else:     
                vetat = 0
            vetatp = vetat * 100
            line.append((0,0,{'name':'Etat', 'annee_n':etat, 'annee_n1':etatn, 'variation_va':vetat, 'variation_p':vetatp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1412%'\
                            group by sub.code) as query")
            rg = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1412%'\
                            group by sub.code) as query")
            rgn = self.env.cr.fetchone()[0] or 0.0
            if rgn != 0:
                vrg = (rg - rgn) / rgn
            else:     
                vrg = 0
            vrgp = vrg * 100
            line.append((0,0,{'name':'Régions', 'annee_n':rg, 'annee_n1':rgn, 'variation_va':vrg, 'variation_p':vrgp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1413%'\
                            group by sub.code) as query")
            dpt = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1413%'\
                            group by sub.code) as query")
            dptn = self.env.cr.fetchone()[0] or 0.0
            if dptn != 0:
                vdpt = (dpt - dptn) / dptn
            else:     
                vdpt = 0
            vdptp = vdpt * 100
            line.append((0,0,{'name':'Départements', 'annee_n':dpt, 'annee_n1':dptn, 'variation_va':vdpt, 'variation_p':vdptp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1414%'\
                            group by sub.code) as query")
            ccpd = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1414%'\
                            group by sub.code) as query")
            ccpdn = self.env.cr.fetchone()[0] or 0.0
            if ccpdn != 0:
                vccpd = (ccpd - ccpdn) / ccpdn
            else:     
                vccpd = 0
            vccpdp = vccpd * 100
            line.append((0,0,{'name':'Communes et collectivités publiques décentralisées', 'annee_n':ccpd, 'annee_n1':ccpdn, 'variation_va':vccpd, 'variation_p':vccpdp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1415%'\
                            group by sub.code) as query")
            epm = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1415%'\
                            group by sub.code) as query")
            epmn = self.env.cr.fetchone()[0] or 0.0
            if epmn != 0:
                vepm = (epm - epmn) / epmn 
            else:     
                vepm = 0
            vepmp = vepm * 100
            line.append((0,0,{'name':'Entités publiques ou mixtes', 'annee_n':epm, 'annee_n1':epmn, 'variation_va':vepm, 'variation_p':vepmp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1416%'\
                            group by sub.code) as query")
            eop = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1416%'\
                            group by sub.code) as query")
            eopn = self.env.cr.fetchone()[0] or 0.0
            if eopn != 0:
                veop = (eop - eopn) / eopn
            else:     
                veop = 0
            veopp = veop * 100
            line.append((0,0,{'name':'Entités et organismes privés', 'annee_n':eop, 'annee_n1':eopn, 'variation_va':veop, 'variation_p':veopp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1417%'\
                            group by sub.code) as query")
            oi = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1417%'\
                            group by sub.code) as query")
            oin = self.env.cr.fetchone()[0] or 0.0
            if oin != 0:
                voi = (oi - oin) / oin 
            else:     
                voi = 0
            voip = voi * 100
            line.append((0,0,{'name':'Organismes internationaux', 'annee_n':oi, 'annee_n1':oin, 'variation_va':voi, 'variation_p':voip}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1418%'\
                            group by sub.code) as query")
            autre = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1418%'\
                            group by sub.code) as query")
            autren = self.env.cr.fetchone()[0] or 0.0
            if autren != 0:
                vautre = (autre - autren) / autren 
            else:     
                vautre = 0
            vautrep = vautre * 100
            line.append((0,0,{'name':'Autres', 'annee_n':autre, 'annee_n1':autren, 'variation_va':vautre, 'variation_p':vautrep}))
            
            ts = etat + rg + dpt + ccpd + epm + eop + oi + autre
            tsn = etatn + rgn + dptn + ccpdn + epmn + eopn + oin + autren
            if tsn != 0:
                vts = (ts - tsn) / tsn
            else:     
                vts = 0
            vtsp = vts * 100
            line.append((0,0,{'name':'TOTAL SUBVENTIONS', 'annee_n':ts, 'annee_n1':tsn, 'variation_va':vts, 'variation_p':vtsp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '151%'\
                            group by sub.code) as query")
            ad = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '151%'\
                            group by sub.code) as query")
            adn = self.env.cr.fetchone()[0] or 0.0
            if adn != 0:
                vad = (ad - adn) / adn
            else:     
                vad = 0
            vadp = vad * 100
            line.append((0,0,{'name':'Amortissements dérogatoires', 'annee_n':ad, 'annee_n1':adn, 'variation_va':vad, 'variation_p':vadp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '152%'\
                            group by sub.code) as query")
            pvcr = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '152%'\
                            group by sub.code) as query")
            pvcrn = self.env.cr.fetchone()[0] or 0.0
            if pvcrn != 0:
                vpvcr = (pvcr - pvcrn) / pvcrn
            else:     
                vpvcr = 0
            vpvcrp = vpvcr * 100
            line.append((0,0,{'name':'Plus-value de cession à réinvertir', 'annee_n':pvcr, 'annee_n1':pvcrn, 'variation_va':vpvcr, 'variation_p':vpvcrp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '154%'\
                            group by sub.code) as query")
            psr = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '154%'\
                            group by sub.code) as query")
            psrn = self.env.cr.fetchone()[0] or 0.0
            if psrn != 0:
                vpsr = (psr - psrn) / psrn
            else:     
                vpsr = 0
            vpsrp = vpsr * 100
            line.append((0,0,{'name':'Provisions spéciales de réévaluation', 'annee_n':psr, 'annee_n1':psrn, 'variation_va':vpsr, 'variation_p':vpsrp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '155%'\
                            group by sub.code) as query")
            prri = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '155%'\
                            group by sub.code) as query")
            prrin = self.env.cr.fetchone()[0] or 0.0
            if prrin != 0:
                vprri = (prri - prrin) / prrin
            else:     
                vprri = 0
            vprrip = vprri * 100
            line.append((0,0,{'name':'Provisions réglementées relatives aux immobilisations', 'annee_n':prri, 'annee_n1':prrin, 'variation_va':vprri, 'variation_p':vprrip}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '156%'\
                            group by sub.code) as query")
            prrs = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '156%'\
                            group by sub.code) as query")
            prrsn = self.env.cr.fetchone()[0] or 0.0
            if prrsn != 0:
                vprrs = (prrs - prrsn) / prrsn 
            else:     
                vprrs = 0
            vprrsp = vprrs * 100
            line.append((0,0,{'name':'Provisions réglementées relatives aux stocks', 'annee_n':prrs, 'annee_n1':prrsn, 'variation_va':vprrs, 'variation_p':vprrsp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '157%'\
                            group by sub.code) as query")
            ppi = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '157%'\
                            group by sub.code) as query")
            ppin = self.env.cr.fetchone()[0] or 0.0
            if ppin != 0:
                vppi = (ppi - ppin) / ppin
            else:     
                vppi = 0
            vppip = vppi * 100
            line.append((0,0,{'name':'Provisions pour investissement', 'annee_n':ppi, 'annee_n1':ppin, 'variation_va':vppi, 'variation_p':vppip}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '158%'\
                            group by sub.code) as query")
            apfr = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '158%'\
                            group by sub.code) as query")
            apfrn = self.env.cr.fetchone()[0] or 0.0
            if apfrn != 0:
                vapfr = (apfr - apfrn) / apfrn
            else:     
                vapfr = 0
            vapfrp = vapfr * 100
            line.append((0,0,{'name':'Autres provisions et fonds reglementés', 'annee_n':apfr, 'annee_n1':apfrn, 'variation_va':vapfr, 'variation_p':vapfrp}))
            
            tpr =  ad + pvcr + psr + prri + prrs + ppi + apfr
            tprn = adn + pvcrn + psrn + prrin + prrsn + ppin + apfrn
            if tprn != 0:
                vtpr = (tpr - tprn) / tprn
            else:     
                vtpr = 0
            vtprp = vtpr * 100
            line.append((0,0,{'name':'TOTAL PROVISIONS REGLEMENTEES', 'annee_n':tpr, 'annee_n1':tprn, 'variation_va':vtpr, 'variation_p':vtprp}))
            
            tspr = ts + tpr
            tsprn = tsn + tprn
            if tsprn != 0:
                vtspr = (tspr - tsprn) / tsprn
            else:     
                vtspr = 0
            vtsprp = vtspr * 100
            line.append((0,0,{'name':'TOTAL SUBVENTIONS ET PROVISIONS REGLEMENTEES', 'annee_n':tspr, 'annee_n1':tsprn, 'variation_va':vtspr, 'variation_p':vtsprp}))
            self.note15A_lines = line


    @api.onchange("note15B")
    def onchange_note15B(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note15B is True:
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '2742%'\
                            group by sub.code) as query")
            tp = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '2742%'\
                            group by sub.code) as query")
            tpn = self.env.cr.fetchone()[0] or 0.0
            if tpn != 0:
                vtp = (tp - tpn) / tpn
            else:     
                vtp = 0
            vtpp = vtp * 100
            line.append((0,0,{'name':'Titres participatifs', 'annee_n':tp, 'annee_n1':tpn, 'variation_va':vtp, 'variation_p':vtpp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '167%'\
                            group by sub.code) as query")
            ac = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '167%'\
                            group by sub.code) as query")
            acn = self.env.cr.fetchone()[0] or 0.0
            if acn != 0:
                vac = (ac - acn) / acn
            else:     
                vac = 0
            vacp = vac * 100
            line.append((0,0,{'name':'Avances conditionnées', 'annee_n':ac, 'annee_n1':acn, 'variation_va':vac, 'variation_p':vacp}))
            
            line.append((0,0,{'name':'Titres subordonnés à durée indéterminée (T.S.D.I)'}))
            line.append((0,0,{'name':'Obligations remboursables en action (O.R.A)'}))
            line.append((0,0,{'name':'Autres'}))
            
            tafp = ac + tp
            tafpn = acn + tpn
            if tafpn != 0:
                vtafp = (tafp - tafpn) / tafpn 
            else:     
                vtafp = 0
            vtafpp = vtafp * 100
            line.append((0,0,{'name':'TOTAL AUTRES FONDS PROPRES', 'annee_n':tafp, 'annee_n1':tafpn, 'variation_va':vtafp, 'variation_p':vtafpp}))
            self.note15B_lines = line


    @api.onchange("note16A")
    def onchange_note16A(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note16A is True:
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '161%'\
                            group by sub.code) as query")
            eo = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '161%'\
                            group by sub.code) as query")
            eon = self.env.cr.fetchone()[0] or 0.0
            if eon != 0:
                veo = (eo - eon) / eon 
            else:     
                veo = 0
            veop = veo * 100
            line.append((0,0,{'name':'Emrpunts obligataires', 'annee_n':eo, 'annee_n1':eon, 'variation_va':veo, 'variation_p':veop}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '162%'\
                            group by sub.code) as query")
            edec = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '162%'\
                            group by sub.code) as query")
            edecn = self.env.cr.fetchone()[0] or 0.0
            if edecn != 0:
                vedec = (edec - edecn) / edecn
            else:     
                vedec = 0
            vedecp = vedec * 100
            line.append((0,0,{'name':'Emprunt et dettes auprés des établissements de crédit', 'annee_n':edec, 'annee_n1':edecn, 'variation_va':vedec, 'variation_p':vedecp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '163%'\
                            group by sub.code) as query")
            are = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '163%'\
                            group by sub.code) as query")
            aren = self.env.cr.fetchone()[0] or 0.0
            if aren != 0:
                vare = (are - aren) / aren
            else:     
                vare = 0
            varep = vare * 100
            line.append((0,0,{'name':'Avances reçues de l’Etat', 'annee_n':are, 'annee_n1':aren, 'variation_va':vare, 'variation_p':varep}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '164%'\
                            group by sub.code) as query")
            aracb = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '164%'\
                            group by sub.code) as query")
            aracbn = self.env.cr.fetchone()[0] or 0.0
            if aracbn != 0:
                varacb = (aracb - aracbn) / aracbn
            else:     
                varacb = 0
            varacbp = varacb * 100
            line.append((0,0,{'name':'Avances reçues et acomptes courants bloques', 'annee_n':aracb, 'annee_n1':aracbn, 'variation_va':varacb, 'variation_p':varacbp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '165%'\
                            group by sub.code) as query")
            dpr = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '165%'\
                            group by sub.code) as query")
            dprn = self.env.cr.fetchone()[0] or 0.0
            if dprn != 0:
                vdpr = (dpr - dprn) / dprn 
            else:     
                vdpr = 0
            vdprp = vdpr * 100
            line.append((0,0,{'name':'Dépôts et cautionnement reçus', 'annee_n':dpr, 'annee_n1':dprn, 'variation_va':vdpr, 'variation_p':vdprp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '166%'\
                            group by sub.code) as query")
            ic = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '166%'\
                            group by sub.code) as query")
            icn = self.env.cr.fetchone()[0] or 0.0
            if icn != 0:
                vic = (ic - icn) / icn
            else:     
                vic = 0
            vicp = vic * 100
            line.append((0,0,{'name':'Intérêts courrus', 'annee_n':ic, 'annee_n1':icn, 'variation_va':vic, 'variation_p':vicp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '167%'\
                            group by sub.code) as query")
            ascp = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '167%'\
                            group by sub.code) as query")
            ascpn = self.env.cr.fetchone()[0] or 0.0
            if ascpn != 0:
                vascp = (ascp - ascpn) / ascpn
            else:     
                vascp = 0
            vascpp = vascp * 100
            line.append((0,0,{'name':'Avances assorties de conditions particulières', 'annee_n':ascp, 'annee_n1':ascpn, 'variation_va':vascp, 'variation_p':vascpp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '168%'\
                            group by sub.code) as query")
            aed = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '168%'\
                            group by sub.code) as query")
            aedn = self.env.cr.fetchone()[0] or 0.0
            if aedn != 0:
                vaed = (aed - aedn) / aedn
            else:     
                vaed = 0
            vaedp = vaed * 100
            line.append((0,0,{'name':'Autres emprunts et dettes', 'annee_n':aed, 'annee_n1':aedn, 'variation_va':vaed, 'variation_p':vaedp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '181%'\
                            group by sub.code) as query")
            dlp = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '181%'\
                            group by sub.code) as query")
            dlpn = self.env.cr.fetchone()[0] or 0.0
            if dlpn != 0:
                vdlp = (dlp - dlpn) / dlpn
            else:     
                vdlp = 0
            vdlpp = vdlp * 100
            line.append((0,0,{'name':'Dettes lièes à des participations', 'annee_n':dlp, 'annee_n1':dlpn, 'variation_va':vdlp, 'variation_p':vdlpp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '184%'\
                            group by sub.code) as query")
            cpbes = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '184%'\
                            group by sub.code) as query")
            cpbesn = self.env.cr.fetchone()[0] or 0.0
            if cpbesn != 0:
                vcpbes = (cpbes - cpbesn) / cpbesn
            else:     
                vcpbes = 0
            vcpbesp = vcpbes * 100
            line.append((0,0,{'name':'Comptes permanents bloqués des établissements et succursales', 'annee_n':cpbes, 'annee_n1':cpbesn, 'variation_va':vcpbes, 'variation_p':vcpbesp}))
            
            tedf = eo + edec + are + aracb + dpr + ic + ascp + aed + dlp + cpbes
            tedfn = eon + edecn + aren + aracbn + dprn + icn + ascpn + aedn + dlpn + cpbesn
            if tedfn != 0:
                vtedf = (tedf - tedfn) / tedfn 
            else:     
                vtedf = 0
            vtedfp = vtedf * 100
            line.append((0,0,{'name':'TOTAL EMPRUNTS ET DETTES FINANCIERES', 'annee_n':tedf, 'annee_n1':tedfn, 'variation_va':vtedf, 'variation_p':vtedfp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '172%'\
                            group by sub.code) as query")
            cbi = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '172%'\
                            group by sub.code) as query")
            cbin = self.env.cr.fetchone()[0] or 0.0
            if cbin != 0:
                vcbi = (cbi - cbin) / cbin
            else:     
                vcbi = 0
            vcbip = vcbi * 100
            line.append((0,0,{'name':'Crédit bail immobilier', 'annee_n':cbi, 'annee_n1':cbin, 'variation_va':vcbi, 'variation_p':vcbip}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '173%'\
                            group by sub.code) as query")
            cbm = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '173%'\
                            group by sub.code) as query")
            cbmn = self.env.cr.fetchone()[0] or 0.0
            if cbmn != 0:
                vcbm = (cbm - cbmn) / cbmn
            else:     
                vcbm = 0
            vcbmp = vcbm * 100
            line.append((0,0,{'name':'Crédit bail mobilier', 'annee_n':cbm, 'annee_n1':cbmn, 'variation_va':vcbm, 'variation_p':vcbmp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '174%'\
                            group by sub.code) as query")
            lv = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '174%'\
                            group by sub.code) as query")
            lvn = self.env.cr.fetchone()[0] or 0.0
            if lvn != 0:
                vlv = (lv - lvn) / lvn
            else:     
                vlv = 0
            vlvp = vlv * 100
            line.append((0,0,{'name':'Location - Vente', 'annee_n':lv, 'annee_n1':lvn, 'variation_va':vlv, 'variation_p':vlvp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '176%'\
                            group by sub.code) as query")
            ic = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '176%'\
                            group by sub.code) as query")
            icn = self.env.cr.fetchone()[0] or 0.0
            if icn != 0:
                vic = (ic - icn) / icn
            else:     
                vic = 0
            vicp = vic * 100
            line.append((0,0,{'name':'Intérêts courrus', 'annee_n':ic, 'annee_n1':icn, 'variation_va':vic, 'variation_p':vicp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '178%'\
                            group by sub.code) as query")
            adla = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '178%'\
                            group by sub.code) as query")
            adlan = self.env.cr.fetchone()[0] or 0.0
            if adlan != 0:
                vadla = (adla - adlan) / adlan
            else:     
                vadla = 0
            vadlap = vadla * 100
            line.append((0,0,{'name':'Autres dettes de locations acquisitions', 'annee_n':adla, 'annee_n1':adlan, 'variation_va':vadla, 'variation_p':vadlap})) 
            
            tdla = cbi + cbm + lv + ic + adla
            tdlan = cbin + cbmn + lvn + icn + adlan
            if tdlan != 0:
                vtdla = (tdla - tdlan) / tdlan  
            else:     
                vtdla = 0
            vtdlap = vtdla * 100
            line.append((0,0,{'name':'TOTAL DETTES DE LOCATION ACQUISITION', 'annee_n':tdla, 'annee_n1':tdlan, 'variation_va':vtdla, 'variation_p':vtdlap}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '191%'\
                            group by sub.code) as query")
            pl = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '191%'\
                            group by sub.code) as query")
            pln = self.env.cr.fetchone()[0] or 0.0
            if pln != 0:
                vpl = (pl - pln) / pln
            else:     
                vpl = 0
            vplp = vpl * 100
            line.append((0,0,{'name':'Provisions pour litiges', 'annee_n':pl, 'annee_n1':pln, 'variation_va':vpl, 'variation_p':vplp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '192%'\
                            group by sub.code) as query")
            pgdc = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '192%'\
                            group by sub.code) as query")
            pgdcn = self.env.cr.fetchone()[0] or 0.0
            if pgdcn != 0:
                vpgdc = (pgdc - pgdcn) / pgdcn
            else:     
                vpgdc = 0
            vpgdcp = vpgdc * 100
            line.append((0,0,{'name':'Provisions pour garanties données aux clients', 'annee_n':pgdc, 'annee_n1':pgdcn, 'variation_va':vpgdc, 'variation_p':vpgdcp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '193%'\
                            group by sub.code) as query")
            ppnaf = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '193%'\
                            group by sub.code) as query")
            ppnafn = self.env.cr.fetchone()[0] or 0.0
            if ppnafn != 0:
                vppnaf = (ppnaf - ppnafn) / ppnafn
            else:     
                vppnaf = 0
            vppnafp = vppnaf * 100
            line.append((0,0,{'name':'Provisions pour pertes sur marchés à achèvement futur', 'annee_n':ppnaf, 'annee_n1':ppnafn, 'variation_va':vppnaf, 'variation_p':vppnafp}))
             
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '194%'\
                            group by sub.code) as query")
            ppc = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '194%'\
                            group by sub.code) as query")
            ppcn = self.env.cr.fetchone()[0] or 0.0
            if ppcn != 0:
                vppc = (ppc - ppcn) / ppcn
            else:     
                vppc = 0
            vppcp = vppc * 100
            line.append((0,0,{'name':'Provisions pour perte de change', 'annee_n':ppc, 'annee_n1':ppcn, 'variation_va':vppc, 'variation_p':vppcp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '195%'\
                            group by sub.code) as query")
            ppi = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '195%'\
                            group by sub.code) as query")
            ppin = self.env.cr.fetchone()[0] or 0.0
            if ppin != 0:
                vppi = (ppi - ppin) / ppin
            else:     
                vppi = 0
            vppip = vppi * 100
            line.append((0,0,{'name':'Provisions pour impôts', 'annee_n':ppi, 'annee_n1':ppin, 'variation_va':vppi, 'variation_p':vppip}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1961%'\
                            group by sub.code) as query")
            ppoa = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1961%'\
                            group by sub.code) as query")
            ppoan = self.env.cr.fetchone()[0] or 0.0
            if ppoan != 0:
                vppoa = (ppoa - ppoan) / ppoan
            else:     
                vppoa = 0
            vppoap = vppoa * 100
            line.append((0,0,{'name':'Provisions pour pensions et obligations assimilées', 'annee_n':ppoa, 'annee_n1':ppoan, 'variation_va':vppoa, 'variation_p':vppoap}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1962%'\
                            group by sub.code) as query")
            arr = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1962%'\
                            group by sub.code) as query")
            arrn = self.env.cr.fetchone()[0] or 0.0
            if arrn != 0:
                varr = (arr - arrn) / arrn  
            else:     
                varr = 0
            varrp = varr * 100
            line.append((0,0,{'name':'Actif du régime de retraite', 'annee_n':arr, 'annee_n1':arrn, 'variation_va':varr, 'variation_p':varrp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '197%'\
                            group by sub.code) as query")
            ppr = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '197%'\
                            group by sub.code) as query")
            pprn = self.env.cr.fetchone()[0] or 0.0
            if pprn != 0:
                vppr = (ppr - pprn) / pprn  
            else:     
                vppr = 0
            vpprp = vppr * 100
            line.append((0,0,{'name':'Provisions pour restructuration', 'annee_n':ppr, 'annee_n1':pprn, 'variation_va':vppr, 'variation_p':vpprp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1981%'\
                            group by sub.code) as query")
            pap = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1981%'\
                            group by sub.code) as query")
            papn = self.env.cr.fetchone()[0] or 0.0
            if papn != 0:
                vpap = (pap - papn) / papn 
            else:     
                vpap = 0
            vpapp = vpap * 100
            line.append((0,0,{'name':'Provisions pour amendes et pénalités', 'annee_n':pap, 'annee_n1':papn, 'variation_va':vpap, 'variation_p':vpapp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1983%'\
                            group by sub.code) as query")
            ppa = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1983%'\
                            group by sub.code) as query")
            ppan = self.env.cr.fetchone()[0] or 0.0
            if ppan != 0:
                vppa = (ppa - ppan) / ppan
            else:     
                vppa = 0
            vppap = vppa * 100
            line.append((0,0,{'name':'Provisons de propre assureur', 'annee_n':ppa, 'annee_n1':ppan, 'variation_va':vppa, 'variation_p':vppap}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1984%'\
                            group by sub.code) as query")
            pdre = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1984%'\
                            group by sub.code) as query")
            pdren = self.env.cr.fetchone()[0] or 0.0
            if pdren != 0:
                vpdre = (pdre - pdren) / pdren
            else:     
                vpdre = 0
            vpdrep = vpdre * 100
            line.append((0,0,{'name':'Provisions pour démantèlement et remise en état', 'annee_n':pdre, 'annee_n1':pdren, 'variation_va':vpdre, 'variation_p':vpdrep}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1985%'\
                            group by sub.code) as query")
            pdd = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1985%'\
                            group by sub.code) as query")
            pddn = self.env.cr.fetchone()[0] or 0.0
            if pddn != 0:
                vpdd = (pdd - pddn) / pddn
            else:     
                vpdd = 0
            vpddp = vpdd * 100
            line.append((0,0,{'name':'Provisions de droits à déduction', 'annee_n':pdd, 'annee_n1':pddn, 'variation_va':vpdd, 'variation_p':vpddp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1985%'\
                            group by sub.code) as query")
            ap = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '1985%'\
                            group by sub.code) as query")
            apn = self.env.cr.fetchone()[0] or 0.0
            if apn != 0:
                vap = (ap - apn) / apn
            else:     
                vap = 0
            vapp = vap * 100
            line.append((0,0,{'name':'Autres provisions', 'annee_n':ap, 'annee_n1':apn, 'variation_va':vap, 'variation_p':vapp}))
                        
            tpfprc = pl + pgdc + ppnaf + ppc + ppi + ppoa + arr + ppr + pap + ppa + pdre + pdd + ap
            tpfprcn = pln + pgdcn + ppnafn + ppcn + ppin + ppoan + arrn + pprn + papn + ppan + pdren + pddn + apn
            if tpfprcn != 0:
                vtpfprc = (tpfprc - tpfprcn) / tpfprcn
            else:     
                vtpfprc = 0
            vtpfprcp = vtpfprc * 100
            line.append((0,0,{'name':'TAL PROVISIONS FINANCIERES POUR RISQUES ET CHARGES', 'annee_n':tpfprc, 'annee_n1':tpfprcn, 'variation_va':vtpfprc, 'variation_p':vtpfprcp}))
            self.note16A_lines = line


    @api.onchange("note16B")
    def onchange_note16B(self):
        line = []
        line2 = []
        line3 = []
        if self.note16B is True:
            line.append((0,0,{'name':'Taux d’augmentation des salaires'}))
            line.append((0,0,{'name':'Taux d’actualisation'}))
            line.append((0,0,{'name':'Taux d’inflation'}))
            line.append((0,0,{'name':'Probabilité d’être dans l’entité à la date de départ à la retraite'}))
            line.append((0,0,{'name':'Probabilité d’être en vie à lâge de départ à la retraite (table de mortalité)'}))
            line.append((0,0,{'name':'Taux de rendement effectif des actifs du régime'}))
            self.note16BTab1_lines = line

            line2.append((0,0,{'name':'Obligation au titre des engagements de retraite à l’ouverture'}))
            line2.append((0,0,{'name':'Coût des services rendus a cours de l’exercice'}))
            line2.append((0,0,{'name':'Coût financier'}))
            line2.append((0,0,{'name':'Perte actuarielles / (gain)'}))
            line2.append((0,0,{'name':'Prestations payées au cours de l’exercice'}))
            line2.append((0,0,{'name':'Coût des services passés'}))
            line2.append((0,0,{'name':'Obligation au titre des engagements de retraite à clôture'}))
            self.note16BTab2_lines = line2

            line3.append((0,0,{'name':'Taux d’actualisation (variation de ... %)'}))
            line3.append((0,0,{'name':'Taux de progression des salaires (variation de ... %)'}))
            line3.append((0,0,{'name':'Taux de départ du personnel (variation de ...%)'}))
            self.note16BTab3_lines = line3


    @api.onchange("note16B_BIS")
    def onchange_note16BBIS(self):
        line = []
        line2 = []
        if self.note16B_BIS is True:
            line.append((0,0,{'name':'Valeur actuelle de l’obligation résultant de régimes financés'}))
            line.append((0,0,{'name':'Valeur actuelle des actifs affectés aux plans de retraite'}))
            self.note16BBISTab1_lines = line

            line2.append((0,0,{'name':'Actions'}))
            line2.append((0,0,{'name':'Obligations'}))
            line2.append((0,0,{'name':'Autres'}))
            self.note16BBISTab2_lines = line2


    @api.onchange("note16C")
    def onchange_note16C(self):
        line = []
        if self.note16C is True:
            line.append((0,0,{'name':'Actif éventuel'}))
            line.append((0,0,{'name':'Litiges'}))
            line.append((0,0,{'name':'............'}))
            line.append((0,0,{'name':'............'}))
            line.append((0,0,{'name':'............'}))
            line.append((0,0,{'name':'............'}))
            line.append((0,0,{'name':'Passif éventuel'}))
            line.append((0,0,{'name':'Litiges'}))
            line.append((0,0,{'name':'............'}))
            line.append((0,0,{'name':'............'}))
            line.append((0,0,{'name':'............'}))
            line.append((0,0,{'name':'............'}))
            self.note16C_lines = line


    @api.onchange("note17")
    def onchange_note17(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note17 is True:
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4011%' or sub.code like '4013%' or sub.code like '4017%'\
                            group by sub.code) as query")
            fdc = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4011%' or sub.code like '4013%' or sub.code like '4017%'\
                            group by sub.code) as query")
            fdcn = self.env.cr.fetchone()[0] or 0.0
            if fdcn != 0:
                vfdc = ((fdc - fdcn) / fdcn) * 100
            else:     
                vfdc = 0
            line.append((0,0,{'name':'Fournisseurs dettes en comptes (hors groupe)', 'annee_n':fdc, 'annee_n1':fdcn, 'variation_p':vfdc}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4021%' or sub.code like '4023%'\
                            group by sub.code) as query")
            fep = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4021%' or sub.code like '4023%'\
                            group by sub.code) as query")
            fepn = self.env.cr.fetchone()[0] or 0.0
            if fepn != 0:
                vfep = ((fep - fepn) / fepn) * 100
            else:     
                vfep = 0
            line.append((0,0,{'name':'Fournisseurs effet à payer (hors groupe)', 'annee_n':fep, 'annee_n1':fepn, 'variation_p':vfep}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4022%'\
                            group by sub.code) as query")
            fdepg = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4022%'\
                            group by sub.code) as query")
            fdepgn = self.env.cr.fetchone()[0] or 0.0
            if fdepgn != 0:
                vfdepg = ((fdepg - fdepgn) / fdepgn) * 100
            else:     
                vfdepg = 0
            line.append((0,0,{'name':'Fournisseurs, dettes et effet à payer groupe', 'annee_n':fdepg, 'annee_n1':fdepgn, 'variation_p':vfdepg}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4081%' or sub.code like '4083%' or sub.code like '4086%'\
                            group by sub.code) as query")
            ffp = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4081%' or sub.code like '4083%' or sub.code like '4086%'\
                            group by sub.code) as query")
            ffpn = self.env.cr.fetchone()[0] or 0.0
            if ffpn != 0:
                vffp = ((ffp - ffpn) / ffpn) * 100
            else:     
                vffp = 0
            line.append((0,0,{'name':'Fournisseurs factures non parvenues (horsgroupe)', 'annee_n':ffp, 'annee_n1':ffpn, 'variation_p':vffp}))
            
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4082%'\
                            group by sub.code) as query")
            ffpg = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4082%'\
                            group by sub.code) as query")
            ffpgn = self.env.cr.fetchone()[0] or 0.0
            if ffpgn != 0:
                vffpg = ((ffpg - ffpgn) / ffpgn) * 100
            else:     
                vffpg = 0
            line.append((0,0,{'name':'Fournisseurs factures non parvenues groupe', 'annee_n':ffpg, 'annee_n1':ffpgn, 'variation_p':vffpg}))
            
            tf = fdc + fep + fdepg + ffp + ffpg
            tfn = fdcn + fepn + fdepgn + ffpn + ffpgn
            if tfn != 0:
                vtf = ((tf - tfn) / tfn) * 100 
            else:     
                vtf = 0
            line.append((0,0,{'name':'TOTAL FOURNISSEURS', 'annee_n':tf, 'annee_n1':tfn, 'variation_p':vtf}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4091%'\
                            group by sub.code) as query")
            fac = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4091%'\
                            group by sub.code) as query")
            facn = self.env.cr.fetchone()[0] or 0.0
            if facn != 0:
                vfac = ((fac - facn) / facn) * 100  
            else:     
                vfac = 0
            line.append((0,0,{'name':'Fournisseurs, avanves et accompte (horsgroupe)', 'annee_n':fac, 'annee_n1':facn, 'variation_p':vfac}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4092%'\
                            group by sub.code) as query")
            facg = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4092%'\
                            group by sub.code) as query")
            facgn = self.env.cr.fetchone()[0] or 0.0
            if facgn != 0:
                vfacg = ((facg - facgn) / facgn) * 100
            else:     
                vfacg = 0
            line.append((0,0,{'name':'Fournisseurs, avanves et accompte groupe', 'annee_n':facg, 'annee_n1':facgn, 'variation_p':vfacg}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4092%'\
                            group by sub.code) as query")
            afd = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4092%'\
                            group by sub.code) as query")
            afdn = self.env.cr.fetchone()[0] or 0.0
            if afdn != 0:
                vafd = ((afd - afdn) / afdn) * 100
            else:     
                vafd = 0
            line.append((0,0,{'name':'Autres fournisseur debiteur', 'annee_n':afd, 'annee_n1':afdn, 'variation_p':vafd}))
            
            tfd = fac + facg + afd
            tfdn = facn + facgn + afdn
            if tfdn != 0:
                vtfd = ((tfd - tfdn) / tfdn) * 100
            else:     
                vtfd = 0
            line.append((0,0,{'name':'TOTAL FOURNISSEURS DEBITEURS', 'annee_n':tfd, 'annee_n1':tfdn, 'variation_p':vtfd}))
            self.note17_lines = line


    @api.onchange("note18")
    def onchange_note18(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note18 is True:
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '421%'\
                            group by sub.code) as query")
            paa = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '421%'\
                            group by sub.code) as query")
            paan = self.env.cr.fetchone()[0] or 0.0
            if paan != 0:
                vpaa = (paa - paan) / paan 
            else:     
                vpaa = 0
            vpaap = vpaa * 100
            line.append((0,0,{'name':'Personnel avances et accomptes', 'annee_n':paa, 'annee_n1':paan, 'variation_va':vpaa, 'variation_p':vpaap}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '422%'\
                            group by sub.code) as query")
            prd = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '422%'\
                            group by sub.code) as query")
            prdn = self.env.cr.fetchone()[0] or 0.0
            if prdn != 0:
                vprd = (prd - prdn) / prdn  
            else:     
                vprd = 0
            vprdp = vprd * 100
            line.append((0,0,{'name':'Personnel rémunérations dues', 'annee_n':prd, 'annee_n1':prdn, 'variation_va':vprd, 'variation_p':vprdp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4231%' or sub.code like '4232%' or sub.code like '4233%' or sub.code like '424%' or sub.code like '425%' or sub.code like '426%' or sub.code like '427%' or sub.code like '4281%' or sub.code like '4286%'\
                            group by sub.code) as query")
            ap = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4231%' or sub.code like '4232%' or sub.code like '4233%' or sub.code like '424%' or sub.code like '425%' or sub.code like '426%' or sub.code like '427%' or sub.code like '4281%' or sub.code like '4286%'\
                            group by sub.code) as query")
            apn = self.env.cr.fetchone()[0] or 0.0
            if apn != 0:
                vap = (ap - apn) / apn
            else:     
                vap = 0
            vapp = vap * 100
            line.append((0,0,{'name':'Autres personnel', 'annee_n':ap, 'annee_n1':apn, 'variation_va':vap, 'variation_p':vapp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '431%'\
                            group by sub.code) as query")
            css = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '431%'\
                            group by sub.code) as query")
            cssn = self.env.cr.fetchone()[0] or 0.0
            if cssn != 0:
                vcss = (css - cssn) / cssn
            else:     
                vcss = 0
            vcssp = vcss * 100
            line.append((0,0,{'name':'Caisse de sécurité sociale', 'annee_n':css, 'annee_n1':cssn, 'variation_va':vcss, 'variation_p':vcssp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '432%'\
                            group by sub.code) as query")
            cr = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '432%'\
                            group by sub.code) as query")
            crn = self.env.cr.fetchone()[0] or 0.0
            if crn != 0:
                vcr = (cr - crn) / crn
            else:     
                vcr = 0
            vcrp = vcr * 100
            line.append((0,0,{'name':'Caisse de retraite', 'annee_n':cr, 'annee_n1':crn, 'variation_va':vcr, 'variation_p':vcrp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '433%'\
                            group by sub.code) as query")
            aos = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '433%'\
                            group by sub.code) as query")
            aosn = self.env.cr.fetchone()[0] or 0.0
            if aosn != 0:
                vaos = (aos - aosn) / aosn
            else:     
                vaos = 0
            vaosp = vaos * 100
            line.append((0,0,{'name':'Autres organismes sociaux', 'annee_n':aos, 'annee_n1':aosn, 'variation_va':vaos, 'variation_p':vaosp}))
            
            tds = paa + prd + ap + css + cr + aos 
            tdsn = paan + prdn + apn + cssn + crn + aosn
            if tdsn != 0:
                vtds = (tds - tdsn) / tdsn
            else:     
                vtds = 0
            vtdsp = vtds * 100
            line.append((0,0,{'name':'TOTAL DETTES SOCIALES', 'annee_n':tds, 'annee_n1':tdsn, 'variation_va':vtds, 'variation_p':vtdsp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '441%'\
                            group by sub.code) as query")
            eib = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '441%'\
                            group by sub.code) as query")
            eibn = self.env.cr.fetchone()[0] or 0.0
            if eibn != 0:
                veib = (eib - eibn) / eibn  
            else:     
                veib = 0
            veibp = veib * 100
            line.append((0,0,{'name':'Etat, impôts sur les bénéfices', 'annee_n':eib, 'annee_n1':eibn, 'variation_va':veib, 'variation_p':veibp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4421%'\
                            group by sub.code) as query")
            eit = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4421%'\
                            group by sub.code) as query")
            eitn = self.env.cr.fetchone()[0] or 0.0
            if eitn != 0:
                veit = (eit - eitn) / eitn
            else:     
                veit = 0
            veitp = veit * 100
            line.append((0,0,{'name':'Etats, impôts et taxes', 'annee_n':eit, 'annee_n1':eitn, 'variation_va':veit, 'variation_p':veitp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4441%'\
                            group by sub.code) as query")
            etva = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4441%'\
                            group by sub.code) as query")
            etvan = self.env.cr.fetchone()[0] or 0.0
            if etvan != 0:
                vetva = (etva - etvan) / etvan
            else:     
                vetva = 0
            vetvap = vetva * 100
            line.append((0,0,{'name':'Etat, TVA', 'annee_n':etva, 'annee_n1':etvan, 'variation_va':vetva, 'variation_p':vetvap}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '447%'\
                            group by sub.code) as query")
            eirs = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '447%'\
                            group by sub.code) as query")
            eirsn = self.env.cr.fetchone()[0] or 0.0
            if eirsn != 0:
                veirs = (eirs - eirsn) / eirsn
            else:     
                veirs = 0
            veirsp = veirs * 100
            line.append((0,0,{'name':'Etat, impôts retenus à la source', 'annee_n':eirs, 'annee_n1':eirsn, 'variation_va':veirs, 'variation_p':veirsp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '446%' or sub.code like '4486%' or sub.code like '4490%'\
                            group by sub.code) as query")
            ade = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '446%' or sub.code like '4486%' or sub.code like '4490%'\
                            group by sub.code) as query")
            aden = self.env.cr.fetchone()[0] or 0.0
            if aden != 0:
                vade = (ade - aden) / aden
            else:     
                vade = 0
            vadep = vade * 100
            line.append((0,0,{'name':'Autres dettes Etat', 'annee_n':ade, 'annee_n1':aden, 'variation_va':vade, 'variation_p':vadep}))
            
            tdf = eib + eit + etva + eirs + ade
            tdfn = eibn + eitn + etvan + eirsn + aden
            if tdfn != 0:
                vtdf = (tdf - tdfn) / tdfn
            else:     
                vtdf = 0
            vtdfp = vtdf * 100
            line.append((0,0,{'name':'TOTAL DETTES FISCALES', 'annee_n':tdf, 'annee_n1':tdfn, 'variation_va':vtdf, 'variation_p':vtdfp}))
            
            tdsf = tds + tdf
            tdsfn = tdsn + tdfn
            if tdsfn != 0:
                vtdsf = (tdsf - tdsfn) / tdsfn
            else:     
                vtdsf = 0
            vtdsfp = vtdsf * 100
            line.append((0,0,{'name':'TOTAL DETTES SOCIALES ET FISCALES', 'annee_n':tdsf, 'annee_n1':tdsfn, 'variation_va':vtdsf, 'variation_p':vtdsfp}))
            self.note18_lines = line


    @api.onchange("note19")
    def onchange_note19(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note19 is True:
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4510%' or sub.code like '4520%' or sub.code like '4580%'\
                            group by sub.code) as query")
            oi = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4510%' or sub.code like '4520%' or sub.code like '4580%'\
                            group by sub.code) as query")
            oin = self.env.cr.fetchone()[0] or 0.0
            if oin != 0:
                voi = (oi - oin) / oin
            else:     
                voi = 0
            voip = voi * 100
            line.append((0,0,{'name':'Organismes internationaux', 'annee_n':oi, 'annee_n1':oin, 'variation_va':voi, 'variation_p':voip}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '461%'\
                            group by sub.code) as query")
            aoc = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '461%'\
                            group by sub.code) as query")
            aocn = self.env.cr.fetchone()[0] or 0.0
            if aocn != 0:
                vaoc = (aoc - aocn) / aocn 
            else:     
                vaoc = 0
            vaocp = vaoc * 100
            line.append((0,0,{'name':'Apporteurs, opérations sur le capital', 'annee_n':aoc, 'annee_n1':aocn, 'variation_va':vaoc, 'variation_p':vaocp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4962%'\
                            group by sub.code) as query")
            ac = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4962%'\
                            group by sub.code) as query")
            acn = self.env.cr.fetchone()[0] or 0.0
            if acn != 0:
                vac = (ac - acn) / acn
            else:     
                vac = 0
            vacp = vac * 100
            line.append((0,0,{'name':'Associés, compte', 'annee_n':ac, 'annee_n1':acn, 'variation_va':vac, 'variation_p':vacp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '6540%'\
                            group by sub.code) as query")
            adp = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '6540%'\
                            group by sub.code) as query")
            adpn = self.env.cr.fetchone()[0] or 0.0
            if adpn != 0:
                vadp = (adp - adpn) / adpn 
            else:     
                vadp = 0
            vadpp = vadp * 100
            line.append((0,0,{'name':'Associés dividendes à payer', 'annee_n':adp, 'annee_n1':adpn, 'variation_va':vadp, 'variation_p':vadpp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '466%'\
                            group by sub.code) as query")
            gcc = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '466%'\
                            group by sub.code) as query")
            gccn = self.env.cr.fetchone()[0] or 0.0
            if gccn != 0:
                vgcc = (gcc - gccn) / gccn
            else:     
                vgcc = 0
            vgccp = vgcc * 100
            line.append((0,0,{'name':'Groupe, comptes courants', 'annee_n':gcc, 'annee_n1':gccn, 'variation_va':vgcc, 'variation_p':vgccp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '463%' or sub.code like '465%'\
                            group by sub.code) as query")
            ads = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '463%' or sub.code like '465%'\
                            group by sub.code) as query")
            adsn = self.env.cr.fetchone()[0] or 0.0
            if adsn != 0:
                vads = (ads - adsn) / adsn
            else:     
                vads = 0
            vadsp = vads * 100
            line.append((0,0,{'name':'Autres dettes associés', 'annee_n':ads, 'annee_n1':adsn, 'variation_va':vads, 'variation_p':vadsp}))
            
            tda = oi + aoc + ac + adp + gcc + ads
            tdan = oin + aocn + acn + adpn + gccn + adsn
            if tdan != 0:
                vtda = (tda - tdan) / tdan 
            else:     
                vtda = 0
            vtdap = vtda * 100
            line.append((0,0,{'name':'TOTAL DETTES ASSOCIES', 'annee_n':tda, 'annee_n1':tdan, 'variation_va':vtda, 'variation_p':vtdap}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4712%'\
                            group by sub.code) as query")
            cd = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4712%'\
                            group by sub.code) as query")
            cdn = self.env.cr.fetchone()[0] or 0.0
            if cdn != 0:
                vcd = (cd - cdn) / cdn
            else:     
                vcd = 0
            vcdp = vcd * 100
            line.append((0,0,{'name':'Créditeurs divers', 'annee_n':cd, 'annee_n1':cdn, 'variation_va':vcd, 'variation_p':vcdp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '471%'\
                            group by sub.code) as query")
            obl = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '471%'\
                            group by sub.code) as query")
            obln = self.env.cr.fetchone()[0] or 0.0
            if obln != 0:
                vobl = (obl - obln) / obln
            else:     
                vobl = 0
            voblp = vobl * 100
            line.append((0,0,{'name':'Obligataires', 'annee_n':obl, 'annee_n1':obln, 'variation_va':vobl, 'variation_p':voblp}))
            
            
            line.append((0,0,{'name':'Rémunération d’administrateurs'}))
            line.append((0,0,{'name':'Compte du factor'}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4726%'\
                            group by sub.code) as query")
            vretdnl = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4726%'\
                            group by sub.code) as query")
            vretdnln = self.env.cr.fetchone()[0] or 0.0
            if vretdnln != 0:
                vvretdnl = (vretdnl - vretdnln) / vretdnln
            else:     
                vvretdnl = 0
            vvretdnlp = vvretdnl * 100
            line.append((0,0,{'name':'Versements restant à effectuer sur titre de déplacement non libérés', 'annee_n':vretdnl, 'annee_n1':vretdnln, 'variation_va':vvretdnl, 'variation_p':vvretdnlp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '475%'\
                            group by sub.code) as query")
            cta = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '475%'\
                            group by sub.code) as query")
            ctan = self.env.cr.fetchone()[0] or 0.0
            if ctan != 0:
                vcta = (cta - ctan) / ctan
            else:     
                vcta = 0
            vctap = vcta * 100
            line.append((0,0,{'name':'Compte transitoire ajustement spécial lié à la révision SYSCOHADA', 'annee_n':cta, 'annee_n1':ctan, 'variation_va':vcta, 'variation_p':vctap}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '473%' or sub.code like '474%' or sub.code like '477%'\
                            group by sub.code) as query")
            acd = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '473%' or sub.code like '474%' or sub.code like '477%'\
                            group by sub.code) as query")
            acdn = self.env.cr.fetchone()[0] or 0.0
            if acdn != 0:
                vacd = (acd - acdn) / acdn
            else:     
                vacd = 0
            vacdp = vacd * 100
            line.append((0,0,{'name':'Autres créditeur divers', 'annee_n':acd, 'annee_n1':acdn, 'variation_va':vacd, 'variation_p':vacdp}))
            
            tcd = cd + obl + vretdnl + cta + acd 
            tcdn = cdn + obln + vretdnln + ctan + acdn
            if tcdn != 0:
                vtcd = (tcd - tcdn) / tcdn  
            else:     
                vtcd = 0
            vtcdp = vtcd * 100
            line.append((0,0,{'name':'TOTAL CREDITEURS DIVERS', 'annee_n':tcd, 'annee_n1':tcdn, 'variation_va':vtcd, 'variation_p':vtcdp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '185%'\
                            group by sub.code) as query")
            cpb = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '185%'\
                            group by sub.code) as query")
            cpbn = self.env.cr.fetchone()[0] or 0.0
            if cpbn != 0:
                vcpb = (cpb - cpbn) / cpbn
            else:     
                vcpb = 0
            vcpbp = vcpb * 100
            line.append((0,0,{'name':'Comptes permanents non bloqués des établissements et des succursales', 'annee_n':cpb, 'annee_n1':cpbn, 'variation_va':vcpb, 'variation_p':vcpbp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '186%' or sub.code like '187%'\
                            group by sub.code) as query")
            clc = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '186%' or sub.code like '187%'\
                            group by sub.code) as query")
            clcn = self.env.cr.fetchone()[0] or 0.0
            if clcn != 0:
                vclc = (clc - clcn) / clcn 
            else:     
                vclc = 0
            vclcp = vclc * 100
            line.append((0,0,{'name':'Comptes de liaison charges et produits', 'annee_n':clc, 'annee_n1':clcn, 'variation_va':vclc, 'variation_p':vclcp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '188%'\
                            group by sub.code) as query")
            clsp = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '188%'\
                            group by sub.code) as query")
            clspn = self.env.cr.fetchone()[0] or 0.0
            if clspn != 0:
                vclsp = (clsp - clspn) / clspn
            else:     
                vclsp = 0
            vclspp = vclsp * 100
            line.append((0,0,{'name':'Comptes de liaison des sociétés en participation', 'annee_n':clsp, 'annee_n1':clspn, 'variation_va':vclsp, 'variation_p':vclspp}))
            
            tcl = cpb + clc + clsp
            tcln = cpbn +  clcn + clspn
            if tcln != 0:
                vtcl = (tcl - tcln) / tcln
            else:     
                vtcl = 0
            vtclp = vtcl * 100
            line.append((0,0,{'name':'TOTAL COMPTE DE LIAISON', 'annee_n':tcl, 'annee_n1':tcln, 'variation_va':vtcl, 'variation_p':vtclp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '499%' or sub.code like '599%' and sub.code not like '4998%' \
                            group by sub.code) as query")
            dn = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '499%' or sub.code like '599%' and sub.code not like '4998%' \
                            group by sub.code) as query")
            dnn = self.env.cr.fetchone()[0] or 0.0
            if dnn != 0:
                vdn = (dn - dnn) / dnn
                if vdn < 0:
                    vdn = -vdn  
            else:     
                vdn = 0
            vdnp = vdn * 100
            line.append((0,0,{'name':'Provisions pour risques à court terme (voir note 28)', 'annee_n':dn, 'annee_n1':dnn, 'variation_va':vdn, 'variation_p':vdnp}))
            self.note19_lines = line


    @api.onchange("note20")
    def onchange_note20(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note20 is True:
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '564%'\
                            group by sub.code) as query")
            ecc = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '564%'\
                            group by sub.code) as query")
            eccn = self.env.cr.fetchone()[0] or 0.0
            if eccn != 0:
                vecc = ((ecc - eccn) / eccn) * 100
            else:     
                vecc = 0
            line.append((0,0,{'name':'Escomptes de crédit de campagne', 'annee_n':ecc, 'annee_n1':eccn, 'variation_p':vecc}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '565%'\
                            group by sub.code) as query")
            eco = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '565%'\
                            group by sub.code) as query")
            econ = self.env.cr.fetchone()[0] or 0.0
            if econ != 0:
                veco = ((eco - econ) / econ) * 100
            else:     
                veco = 0
            line.append((0,0,{'name':'Escomptes de crédit ordinaire', 'annee_n':eco, 'annee_n1':econ, 'variation_p':veco}))
            
            tbcet = ecc + eco 
            tbcetn = eccn + econ 
            if tbcetn != 0:
                vtbcet = ((tbcet - tbcetn) / tbcetn) * 100
            else:     
                vtbcet = 0
            line.append((0,0,{'name':'TOTAL : BANQUES, CREDITS D’ESCOMPTE ET DE TRESORERIE', 'annee_n':tbcet, 'annee_n1':tbcetn, 'variation_p':vtbcet}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '521%'\
                            group by sub.code) as query")
            bl = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '521%'\
                            group by sub.code) as query")
            bln = self.env.cr.fetchone()[0] or 0.0
            if bln != 0:
                vbl = ((bl - bln) / bln) * 100
            else:     
                vbl = 0
            line.append((0,0,{'name':'Banques locales', 'annee_n':bl, 'annee_n1':bln, 'variation_p':vbl}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '522%'\
                            group by sub.code) as query")
            baer = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '522%'\
                            group by sub.code) as query")
            baern = self.env.cr.fetchone()[0] or 0.0
            if baern != 0:
                vbaer = ((baer - baern) / baern) * 100
            else:     
                vbaer = 0
            line.append((0,0,{'name':'Banques autres états région', 'annee_n':baer, 'annee_n1':baern, 'variation_p':vbaer}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '523%' or sub.code like '524%' or sub.code like '525%'\
                            group by sub.code) as query")
            aub = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '523%' or sub.code like '524%' or sub.code like '525%'\
                            group by sub.code) as query")
            aubn = self.env.cr.fetchone()[0] or 0.0
            if aubn != 0:
                vaub = ((aub - aubn) / aubn) * 100
            else:     
                vaub = 0
            line.append((0,0,{'name':'Autres Banques', 'annee_n':aub, 'annee_n1':aubn, 'variation_p':vaub}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '526%'\
                            group by sub.code) as query")
            bic = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '526%'\
                            group by sub.code) as query")
            bicn = self.env.cr.fetchone()[0] or 0.0
            if bicn != 0:
                vbic = ((bic - bicn) / bicn) * 100
            else:     
                vbic = 0
            line.append((0,0,{'name':'Banques intérêts courus', 'annee_n':bic, 'annee_n1':bicn, 'variation_p':vbic}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '561%'\
                            group by sub.code) as query")
            crt = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '561%'\
                            group by sub.code) as query")
            crtn = self.env.cr.fetchone()[0] or 0.0
            if crtn != 0:
                vcrt = ((crt - crtn) / crtn) * 100
            else:     
                vcrt = 0
            line.append((0,0,{'name':'Crédit de trésorerie', 'annee_n':crt, 'annee_n1':crtn, 'variation_p':vcrt}))
            
            tbct = bl + baer + aub + bic + crt
            tbctn = bln + baern + aubn + bicn + crtn
            if tbctn != 0:
                vtbct = ((tbct - tbctn) / tbctn) * 100
            else:     
                vtbct = 0
            line.append((0,0,{'name':'TOTAL : BANQUES, CREDITS DE TRESORERIE', 'annee_n':tbct, 'annee_n1':tbctn, 'variation_p':vtbct}))
            
            tg = tbcet + tbct
            tgn = tbcetn + tbctn
            if tgn != 0:
                vtg = ((tg - tgn) / tgn) * 100
            else:     
                vtg = 0
            line.append((0,0,{'name':'TOTAL GENERAL', 'annee_n':tg, 'annee_n1':tgn, 'variation_p':vtg}))
            self.note20_lines = line

    @api.onchange("note21")
    def onchange_note21(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note21 is True:
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '701100%'\
                            group by sub.code) as query")
            vdr = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '701100%'\
                            group by sub.code) as query")
            vdrn = self.env.cr.fetchone()[0] or 0.0
            if vdrn != 0:
                vvdr = ((vdr - vdrn) / vdrn) * 100
            else:     
                vvdr = 0
            line.append((0,0,{'name':'Ventes dans la Région', 'annee_n':vdr, 'annee_n1':vdrn, 'variation_p':vvdr}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '701200%'\
                            group by sub.code) as query")
            vhr = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '701200%'\
                            group by sub.code) as query")
            vhrn = self.env.cr.fetchone()[0] or 0.0
            if vhrn != 0:
                vvhr = ((vhr - vhrn) / vhrn) * 100
            else:     
                vvhr = 0
            line.append((0,0,{'name':'Vente hors Région', 'annee_n':vhr, 'annee_n1':vhrn, 'variation_p':vvhr}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '701300%' or sub.code like '701400%'\
                            group by sub.code) as query")
            vg = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '701300%' or sub.code like '701400%'\
                            group by sub.code) as query")
            vgn = self.env.cr.fetchone()[0] or 0.0
            if vgn != 0:
                vvg = ((vg - vgn) / vgn) * 100 
            else:     
                vvg = 0
            line.append((0,0,{'name':'Vente groupe', 'annee_n':vg, 'annee_n1':vgn, 'variation_p':vvg}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '701500%'\
                            group by sub.code) as query")
            vsi = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '701500%'\
                            group by sub.code) as query")
            vsin = self.env.cr.fetchone()[0] or 0.0
            if vsin != 0:
                vvsi = ((vsi - vsin) / vsin) * 100 
            else:     
                vvsi = 0
            line.append((0,0,{'name':'Ventes sur internet', 'annee_n':vsi, 'annee_n1':vsin, 'variation_p':vvsi}))
            
            tvm = vdr + vhr + vg + vsi
            tvmn = vdrn + vhrn + vgn + vsin
            if tvmn != 0:
                vtvm = ((tvm - tvmn) / tvmn) * 100
            else:     
                vtvm = 0
            line.append((0,0,{'name':'TOTAL : VENTES DE MARCHANDISES', 'annee_n':tvm, 'annee_n1':tvmn, 'variation_p':vtvm}))
            
            line.append((0,0,{'name':''}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '702100%'\
                            group by sub.code) as query")
            vdr2 = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '702100%'\
                            group by sub.code) as query")
            vdrn2 = self.env.cr.fetchone()[0] or 0.0
            if vdrn2 != 0:
                vvdr2 = ((vdr2 - vdrn2) / vdrn2) * 100
            else:     
                vvdr2 = 0
            line.append((0,0,{'name':'Ventes dans la Région', 'annee_n':vdr2, 'annee_n1':vdrn2, 'variation_p':vvdr2}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '702200%'\
                            group by sub.code) as query")
            vhr2 = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '702200%'\
                            group by sub.code) as query")
            vhrn2 = self.env.cr.fetchone()[0] or 0.0
            if vhrn2 != 0:
                vvhr2 = ((vhr2 - vhrn2) / vhrn2) * 100
            else:     
                vvhr2 = 0
            line.append((0,0,{'name':'Vente hors Région', 'annee_n':vhr2, 'annee_n1':vhrn2, 'variation_p':vvhr2}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '702300%' or sub.code like '702400%'\
                            group by sub.code) as query")
            vg2 = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '702300%' or sub.code like '702400%'\
                            group by sub.code) as query")
            vgn2 = self.env.cr.fetchone()[0] or 0.0
            if vgn2 != 0:
                vvg2 = ((vg2 - vgn2) / vgn2) * 100
            else:     
                vvg2 = 0
            line.append((0,0,{'name':'Vente groupe', 'annee_n':vg2, 'annee_n1':vgn2, 'variation_p':vvg2}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '702500%'\
                            group by sub.code) as query")
            vsi2 = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '702500%'\
                            group by sub.code) as query")
            vsin2 = self.env.cr.fetchone()[0] or 0.0
            if vsin2 != 0:
                vvsi2 = ((vsi2 - vsin2) / vsin2) * 100
            else:     
                vvsi2 = 0
            line.append((0,0,{'name':'Ventes sur internet', 'annee_n':vsi2, 'annee_n1':vsin2, 'variation_p':vvsi2}))
            
            tvpf = vdr2 + vhr2 + vg2 + vsi2
            tvpfn = vdrn2 + vhrn2 + vgn2 + vsin2
            if tvpfn != 0:
                vtvpf = ((tvpf - tvpfn) / tvpfn) * 100
            else:     
                vtvpf = 0
            line.append((0,0,{'name':'TOTAL : VENTES DE PRODUITS FABRIQUES', 'annee_n':tvpf, 'annee_n1':tvpfn, 'variation_p':vtvpf}))
            line.append((0,0,{'name':''}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '705100%' or sub.code like '706100%'\
                            group by sub.code) as query")
            vdr3 = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '705100%' or sub.code like '706100%'\
                            group by sub.code) as query")
            vdrn3 = self.env.cr.fetchone()[0] or 0.0
            if vdrn3 != 0:
                vvdr3 = ((vdr3 - vdrn3) / vdrn3) * 100
            else:     
                vvdr3 = 0
            line.append((0,0,{'name':'Ventes dans la Région', 'annee_n':vdr3, 'annee_n1':vdrn3, 'variation_p':vvdr3}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '705200%' or sub.code like '706200%'\
                            group by sub.code) as query")
            vhr3 = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '705200%' or sub.code like '706200%'\
                            group by sub.code) as query")
            vhrn3 = self.env.cr.fetchone()[0] or 0.0
            if vhrn3 != 0:
                vvhr3 = ((vhr3 - vhrn3) / vhrn3) * 100
            else:     
                vvhr3 = 0
            line.append((0,0,{'name':'Vente hors Région', 'annee_n':vhr3, 'annee_n1':vhrn3, 'variation_p':vvhr3}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '705300%' or sub.code like '705400%' or sub.code like '706300%' or sub.code like '706400%'\
                            group by sub.code) as query")
            vg3 = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '705300%' or sub.code like '705400%' or sub.code like '706300%' or sub.code like '706400%'\
                            group by sub.code) as query")
            vgn3 = self.env.cr.fetchone()[0] or 0.0
            if vgn3 != 0:
                vvg3 = ((vg3 - vgn3) / vgn3) * 100
            else:     
                vvg3 = 0
            line.append((0,0,{'name':'Vente groupe', 'annee_n':vg3, 'annee_n1':vgn3, 'variation_p':vvg3}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '705500%' or sub.code like '706500%'\
                            group by sub.code) as query")
            vsi3 = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '705500%' or sub.code like '706500%'\
                            group by sub.code) as query")
            vsin3 = self.env.cr.fetchone()[0] or 0.0
            if vsin3 != 0:
                vvsi3 = ((vsi3 - vsin3) / vsin3) * 100
            else:     
                vvsi3 = 0
            line.append((0,0,{'name':'Ventes sur internet', 'annee_n':vsi3, 'annee_n1':vsin3, 'variation_p':vvsi3}))
            
            tvtsv = vdr3 + vhr3 + vg3 + vsi3
            tvtsvn = vdrn3 + vhrn3 + vgn3 + vsin3
            if tvtsvn != 0:
                vtvtsv = ((tvtsv - tvtsvn) / tvtsvn) * 100 
            else:     
                vtvtsv = 0
            line.append((0,0,{'name':'TOTAL : VENTES DE TRAVAUX ET SERVICES VENDUS', 'annee_n':tvtsv, 'annee_n1':tvtsvn, 'variation_p':vtvtsv}))
            
            line.append((0,0,{'name':''}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '707100%' or sub.code like '707200%' or sub.code like '707300%' or sub.code like '707400%' or sub.code like '707500%' or sub.code like '707600%' or sub.code like '707700%' or sub.code like '707800%'\
                            group by sub.code) as query")
            pa = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '707100%' or sub.code like '707200%' or sub.code like '707300%' or sub.code like '707400%' or sub.code like '707500%' or sub.code like '707600%' or sub.code like '707700%' or sub.code like '707800%'\
                            group by sub.code) as query")
            pan = self.env.cr.fetchone()[0] or 0.0
            if pan != 0:
                vpa = ((pa - pan) / pan) * 100
            else:     
                vpa = 0
            line.append((0,0,{'name':'Produits accessoires', 'annee_n':pa, 'annee_n1':pan, 'variation_p':vpa}))
            line.append((0,0,{'name':'TOTAL : CHIFFRES D’AFFAIRE', 'annee_n':pa, 'annee_n1':pan, 'variation_p':vpa}))
            line.append((0,0,{'name':''}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '721000%' or sub.code like '722000%' or sub.code like '724000%' or sub.code like '726000%'\
                            group by sub.code) as query")
            pi = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '721000%' or sub.code like '722000%' or sub.code like '724000%' or sub.code like '726000%'\
                            group by sub.code) as query")
            pin = self.env.cr.fetchone()[0] or 0.0
            if pin != 0:
                vpi = ((pi - pin) / pin) * 100
            else:     
                vpi = 0
            line.append((0,0,{'name':'Production immobilisée', 'annee_n':pi, 'annee_n1':pin, 'variation_p':vpi}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '711000%' or sub.code like '712000%' or sub.code like '713000%' or sub.code like '714000%' or sub.code like '718100%' or sub.code like '718200%' or sub.code like '718300%'\
                            group by sub.code) as query")
            sd = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '711000%' or sub.code like '712000%' or sub.code like '713000%' or sub.code like '714000%' or sub.code like '718100%' or sub.code like '718200%' or sub.code like '718300%'\
                            group by sub.code) as query")
            sdn = self.env.cr.fetchone()[0] or 0.0
            if sdn != 0:
                vsd = ((sd - sdn) / sdn) * 100
            else:     
                vsd = 0
            line.append((0,0,{'name':'Subvention d’exploitation', 'annee_n':sd, 'annee_n1':sdn, 'variation_p':vsd}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '751000%' or sub.code like '752000%' or sub.code like '754000%' or sub.code like '756000%' or sub.code like '758000%' or sub.code like '759000%'\
                            group by sub.code) as query")
            ap = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '751000%' or sub.code like '752000%' or sub.code like '754000%' or sub.code like '756000%' or sub.code like '758000%' or sub.code like '759000%'\
                            group by sub.code) as query")
            apn = self.env.cr.fetchone()[0] or 0.0
            if apn != 0:
                vap = ((ap - apn) / apn) * 100
            else:     
                vap = 0
            line.append((0,0,{'name':'Autres produits', 'annee_n':ap, 'annee_n1':apn, 'variation_p':vap}))
            
            tap = pi + sd + ap
            tapn = pin + sdn + ap
            if tapn != 0:
                vtap = ((tap - tapn) / tapn) * 100
            else:     
                vtap = 0
            line.append((0,0,{'name':'TOTAL : AUTRES PRODUITS', 'annee_n':tap, 'annee_n1':tapn, 'variation_p':vtap}))
            line.append((0,0,{'name':''}))
            
            total = tvm + tvpf + tvtsv + pa + tap
            totaln = tvmn + tvpfn + tvtsvn + pan + tapn
            if totaln != 0:
                vtotal = ((total - totaln) / totaln) * 100
            else:     
                vtotal = 0
            line.append((0,0,{'name':'TOTAL'}))

            self.note21_lines = line


    @api.onchange("note22")
    def onchange_note22(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note22 is True:
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '601100%'\
                            group by sub.code) as query")
            adr = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '601100%'\
                            group by sub.code) as query")
            adrn = self.env.cr.fetchone()[0] or 0.0
            if adrn != 0:
                vadr = ((adr - adrn) / adrn) * 100
            else:     
                vadr = 0
            line.append((0,0,{'name':'Achats dans la Région', 'annee_n':adr, 'annee_n1':adrn, 'variation_p':vadr}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '601200%'\
                            group by sub.code) as query")
            ahr = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '601200%'\
                            group by sub.code) as query")
            ahrn = self.env.cr.fetchone()[0] or 0.0
            if ahrn != 0:
                vahr = ((ahr - ahrn) / ahrn) * 100
            else:     
                vahr = 0
            line.append((0,0,{'name':'Achats hors Région', 'annee_n':ahr, 'annee_n1':ahrn, 'variation_p':vahr}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '601300%' or sub.code like '601400%'\
                            group by sub.code) as query")
            ag = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '601300%' or sub.code like '601400%'\
                            group by sub.code) as query")
            agn = self.env.cr.fetchone()[0] or 0.0
            if agn != 0:
                vag = ((ag - agn) / agn) * 100
            else:     
                vag = 0
            line.append((0,0,{'name':'Achats groupe', 'annee_n':ag, 'annee_n1':agn, 'variation_p':vag}))
            
            tam = adr + ahr + ag
            tamn = adrn + ahrn + agn
            if tamn != 0:
                vtam = ((tam - tamn) / tamn) * 100
            else:     
                vtam = 0
            line.append((0,0,{'name':'TOTAL : ACHATS DE MARCHANDISES', 'annee_n':tam, 'annee_n1':tamn, 'variation_p':vtam}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '602100%'\
                            group by sub.code) as query")
            adr2 = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '602100%'\
                            group by sub.code) as query")
            adrn2 = self.env.cr.fetchone()[0] or 0.0
            if adrn2 != 0:
                vadr2 = ((adr2 - adrn2) / adrn2) * 100
            else:     
                vadr2 = 0
            line.append((0,0,{'name':'Achats dans la Région', 'annee_n':adr2, 'annee_n1':adrn2, 'variation_p':vadr2}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '602200%'\
                            group by sub.code) as query")
            ahr2 = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '602200%'\
                            group by sub.code) as query")
            ahrn2 = self.env.cr.fetchone()[0] or 0.0
            if ahrn2 != 0:
                vahr2 = ((ahr2 - ahrn2) / ahrn2) * 100
            else:     
                vahr2 = 0
            line.append((0,0,{'name':'Achats hors Région', 'annee_n':ahr2, 'annee_n1':ahrn2, 'variation_p':vahr2}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '602300%' or sub.code like '602400%'\
                            group by sub.code) as query")
            ag2 = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '602300%' or sub.code like '602400%'\
                            group by sub.code) as query")
            agn2 = self.env.cr.fetchone()[0] or 0.0
            if agn2 != 0:
                vag2 = ((ag2 - agn2) / agn2) * 100
            else:     
                vag2 = 0
            line.append((0,0,{'name':'Achats groupe', 'annee_n':ag2, 'annee_n1':agn2, 'variation_p':vag2}))
            
            tampfl = adr2 + ahr2 + ag2
            tampfln = adrn2 + ahrn2 + agn2
            if tampfln != 0:
                vtampfl = ((tampfl - tampfln) / tampfln) * 100
            else:     
                vtampfl = 0
            line.append((0,0,{'name':'TOTAL : ACHATS MATIERES PREMIERES ET FOURNITURES LIEES', 'annee_n':tampfl, 'annee_n1':tampfln, 'variation_p':vtampfl}))
            
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '604100%'\
                            group by sub.code) as query")
            mc = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '604100%'\
                            group by sub.code) as query")
            mcn = self.env.cr.fetchone()[0] or 0.0
            if mcn != 0:
                vmc = ((mc - mcn) / mcn) * 100
            else:     
                vmc = 0
            line.append((0,0,{'name':'Matiéres consommables', 'annee_n':mc, 'annee_n1':mcn, 'variation_p':vmc}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '604200%'\
                            group by sub.code) as query")
            mco = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '604200%'\
                            group by sub.code) as query")
            mcon = self.env.cr.fetchone()[0] or 0.0
            if mcon != 0:
                vmco = ((mco - mcon) / mcon) * 100
            else:     
                vmco = 0
            line.append((0,0,{'name':'Matiéres combustibles', 'annee_n':mco, 'annee_n1':mcon, 'variation_p':vmco}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '604300%'\
                            group by sub.code) as query")
            pe = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '604300%'\
                            group by sub.code) as query")
            pen = self.env.cr.fetchone()[0] or 0.0
            if pen != 0:
                vpe = ((pe - pen) / pen) * 100
            else:     
                vpe = 0
            line.append((0,0,{'name':'Produit d’entretien', 'annee_n':pe, 'annee_n1':pen, 'variation_p':vpe}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '604400%'\
                            group by sub.code) as query")
            faum = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '604400%'\
                            group by sub.code) as query")
            faumn = self.env.cr.fetchone()[0] or 0.0
            if faumn != 0:
                vfaum = ((faum - faumn) / faumn) * 100
            else:     
                vfaum = 0
            line.append((0,0,{'name':'Fournitures d’atelier, d’usine et de magasin', 'annee_n':faum, 'annee_n1':faumn, 'variation_p':vfaum}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '605200%'\
                            group by sub.code) as query")
            eau = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '605100%'\
                            group by sub.code) as query")
            eaun = self.env.cr.fetchone()[0] or 0.0
            if eaun != 0:
                veau = ((eau - eaun) / eaun) * 100
            else:     
                veau = 0
            line.append((0,0,{'name':'Eaux', 'annee_n':eau, 'annee_n1':eaun, 'variation_p':veau}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '605200%'\
                            group by sub.code) as query")
            elect = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '605200%'\
                            group by sub.code) as query")
            electn = self.env.cr.fetchone()[0] or 0.0
            if electn != 0:
                velect = ((elect - electn) / electn) * 100
            else:     
                velect = 0
            line.append((0,0,{'name':'Electricité', 'annee_n':elect, 'annee_n1':electn, 'variation_p':velect}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '605300%'\
                            group by sub.code) as query")
            ae = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '605300%'\
                            group by sub.code) as query")
            aen = self.env.cr.fetchone()[0] or 0.0
            if aen != 0:
                vae = ((ae - aen) / aen) * 100
            else:     
                vae = 0
            line.append((0,0,{'name':'Autres énergies', 'annee_n':ae, 'annee_n1':aen, 'variation_p':vae}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '605400%'\
                            group by sub.code) as query")
            fe = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '605400%'\
                            group by sub.code) as query")
            fen = self.env.cr.fetchone()[0] or 0.0
            if fen != 0:
                vfe = ((fe - fen) / fen) * 100
            else:     
                vfe = 0
            line.append((0,0,{'name':'Fourniture d’entretien', 'annee_n':fe, 'annee_n1':fen, 'variation_p':vfe}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '605500%'\
                            group by sub.code) as query")
            fb = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '605500%'\
                            group by sub.code) as query")
            fbn = self.env.cr.fetchone()[0] or 0.0
            if fbn != 0:
                vfb = ((fb - fbn) / fbn) * 100
            else:     
                vfb = 0
            line.append((0,0,{'name':'Fourniture de bureau', 'annee_n':fb, 'annee_n1':fbn, 'variation_p':vfb}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '605600%'\
                            group by sub.code) as query")
            pmo = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '605600%'\
                            group by sub.code) as query")
            pmon = self.env.cr.fetchone()[0] or 0.0
            if pmon != 0:
                vpmo = ((pmo - pmon) / pmon) * 100
            else:     
                vpmo = 0
            line.append((0,0,{'name':'Petit matériel et outillages produits', 'annee_n':pmo, 'annee_n1':pmon, 'variation_p':vpmo}))
            
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '605700%'\
                            group by sub.code) as query")
            aep = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '605700%'\
                            group by sub.code) as query")
            aepn = self.env.cr.fetchone()[0] or 0.0
            if aepn != 0:
                vaep = ((aep - aepn) / aepn) * 100
            else:     
                vaep = 0
            line.append((0,0,{'name':'Achats études, prestation de services, de travaux matériels et équipements', 'annee_n':aep, 'annee_n1':aepn, 'variation_p':vaep}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '608100%' or sub.code like '608200%' or sub.code like '608300%'\
                            group by sub.code) as query")
            adem = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '608100%' or sub.code like '608200%' or sub.code like '608300%'\
                            group by sub.code) as query")
            ademn = self.env.cr.fetchone()[0] or 0.0
            if ademn != 0:
                vadem = ((adem - ademn) / ademn) * 100
            else:     
                vadem = 0
            line.append((0,0,{'name':'Achats d\'embalage', 'annee_n':adem, 'annee_n1':ademn, 'variation_p':vadem}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '608500%'\
                            group by sub.code) as query")
            fsa = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '608500%'\
                            group by sub.code) as query")
            fsan = self.env.cr.fetchone()[0] or 0.0
            if fsan != 0:
                vfsa = ((fsa - fsan) / fsan) * 100 
            else:     
                vfsa = 0
            line.append((0,0,{'name':'Frais sur achats', 'annee_n':fsa, 'annee_n1':fsan, 'variation_p':vfsa}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '608900%'\
                            group by sub.code) as query")
            rab = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '608900%'\
                            group by sub.code) as query")
            rabn = self.env.cr.fetchone()[0] or 0.0
            if rabn != 0:
                vrab = ((rab - rabn) / rabn) * 100
            else:     
                vrab = 0
            line.append((0,0,{'name':'Remises, rabais, remises et ristournes', 'annee_n':rab, 'annee_n1':rabn, 'variation_p':vrab}))
            
            taa = mc + mco + pe + faum + eau + elect + ae + fe + fb + pmo + aep + adem + fsa + rab
            taan = mcn + mcon + pen + faumn + eaun + electn + aen + fe + fbn + pmon + aepn + ademn + fsan + rabn
            if taan != 0:
                vtaa = ((taa - taan) / taan) * 100
            else:     
                vtaa = 0
            line.append((0,0,{'name':'TOTAL : AUTRES ACHATS', 'annee_n':taa, 'annee_n1':taan, 'variation_p':vtaa}))


            self.note22_lines = line


    @api.onchange("note23")
    def onchange_note23(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note23 is True:
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '612%'\
                            group by sub.code) as query")
            tsv = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '612%'\
                            group by sub.code) as query")
            tsvn = self.env.cr.fetchone()[0] or 0.0
            if tsvn != 0:
                vtsv = ((tsv - tsvn) / tsvn) * 100
            else:     
                vtsv = 0
            line.append((0,0,{'name':'Transport sur ventes', 'annee_n':tsv, 'annee_n1':tsvn, 'variation_p':vtsv}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '613%'\
                            group by sub.code) as query")
            tplct = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '613%'\
                            group by sub.code) as query")
            tplctn = self.env.cr.fetchone()[0] or 0.0
            if tplctn != 0:
                vtplct = ((tplct - tplctn) / tplctn) * 100
            else:     
                vtplct = 0
            line.append((0,0,{'name':'Transport pour le compte de tiers', 'annee_n':tplct, 'annee_n1':tplctn, 'variation_p':vtplct}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '614%'\
                            group by sub.code) as query")
            tdp = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '614%'\
                            group by sub.code) as query")
            tdpn = self.env.cr.fetchone()[0] or 0.0
            if tdpn != 0:
                vtdp = ((tdp - tdpn) / tdpn) * 100
            else:     
                vtdp = 0
            line.append((0,0,{'name':'Transport du personnel', 'annee_n':tdp, 'annee_n1':tdpn, 'variation_p':vtdp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '616%'\
                            group by sub.code) as query")
            tpl = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '616%'\
                            group by sub.code) as query")
            tpln = self.env.cr.fetchone()[0] or 0.0
            if tpln != 0:
                vtpl = ((tpl - tpln) / tpln) * 100
            else:     
                vtpl = 0
            line.append((0,0,{'name':'Transport de plis', 'annee_n':tpl, 'annee_n1':tpln, 'variation_p':vtpl}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '618%'\
                            group by sub.code) as query")
            atr = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '618%'\
                            group by sub.code) as query")
            atrn = self.env.cr.fetchone()[0] or 0.0
            if atrn != 0:
                vatr = ((atr - atrn) / atrn) * 100
            else:     
                vatr = 0
            line.append((0,0,{'name':'Autres transport', 'annee_n':atr, 'annee_n1':atrn, 'variation_p':vatr}))
            
            total = tsv + tplct + tdp + tpl + atr
            totaln = tsvn + tplctn + tdpn + tpln + atrn
            if totaln != 0:
                vtotal = ((total - totaln) / totaln) * 100
            else:     
                vtotal = 0
            line.append((0,0,{'name':'TOTAL', 'annee_n':total, 'annee_n1':totaln, 'variation_p':vtotal}))

            self.note23_lines = line

    @api.onchange("note24")
    def onchange_note24(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note24 is True:
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '621000%'\
                            group by sub.code) as query")
            stg = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '621000%'\
                            group by sub.code) as query")
            stgn = self.env.cr.fetchone()[0] or 0.0
            if stgn != 0:
                vstg = ((stg - stgn) / stgn) * 100
            else:     
                vstg = 0
            line.append((0,0,{'name':'Sous-traitance générale', 'annee_n':stg, 'annee_n1':stgn, 'variation_p':vstg}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '622000%'\
                            group by sub.code) as query")
            lcl = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '622000%'\
                            group by sub.code) as query")
            lcln = self.env.cr.fetchone()[0] or 0.0
            if lcln != 0:
                vlcl = ((lcl - lcln) / lcln) * 100
            else:     
                vlcl = 0
            line.append((0,0,{'name':'Locations et charges locatives', 'annee_n':lcl, 'annee_n1':lcln, 'variation_p':vlcl}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '623000%'\
                            group by sub.code) as query")
            rla = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '623000%'\
                            group by sub.code) as query")
            rlan = self.env.cr.fetchone()[0] or 0.0
            if rlan != 0:
                vrla = ((rla - rlan) / rlan) * 100
            else:     
                vrla = 0
            line.append((0,0,{'name':'Redevances de location acquisition', 'annee_n':rla, 'annee_n1':rlan, 'variation_p':vrla}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '624000%'\
                            group by sub.code) as query")
            erm = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '624000%'\
                            group by sub.code) as query")
            ermn = self.env.cr.fetchone()[0] or 0.0
            if ermn != 0:
                verm = ((erm - ermn) / ermn) * 100
            else:     
                verm = 0
            line.append((0,0,{'name':'Entretien, réparations et maintenance', 'annee_n':erm, 'annee_n1':ermn, 'variation_p':verm}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '625000%'\
                            group by sub.code) as query")
            pra = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '625000%'\
                            group by sub.code) as query")
            pran = self.env.cr.fetchone()[0] or 0.0
            if pran != 0:
                vpra = ((pra - pran) / pran) * 100
            else:     
                vpra = 0
            line.append((0,0,{'name':'Primes d’assurances', 'annee_n':pra, 'annee_n1':pran, 'variation_p':vpra}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '626000%'\
                            group by sub.code) as query")
            erd = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '626000%'\
                            group by sub.code) as query")
            erdn = self.env.cr.fetchone()[0] or 0.0
            if erdn != 0:
                verd = ((erd - erdn) / erdn) * 100
            else:     
                verd = 0
            line.append((0,0,{'name':'Etudes, recherches et documentation', 'annee_n':erd, 'annee_n1':erdn, 'variation_p':verd}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '627000%'\
                            group by sub.code) as query")
            pprp = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '627000%'\
                            group by sub.code) as query")
            pprpn = self.env.cr.fetchone()[0] or 0.0
            if pprpn != 0:
                vpprp = ((pprp - pprpn) / pprpn) * 100  
            else:     
                vpprp = 0
            line.append((0,0,{'name':'Publicité, publication, relations publiques', 'annee_n':pprp, 'annee_n1':pprpn, 'variation_p':vpprp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '627000%'\
                            group by sub.code) as query")
            fdt = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '627000%'\
                            group by sub.code) as query")
            fdtn = self.env.cr.fetchone()[0] or 0.0
            if fdtn != 0:
                vfdt = ((fdt - fdtn) / fdtn) * 100
            else:     
                vfdt = 0
            line.append((0,0,{'name':'Frais de télécommunication', 'annee_n':fdt, 'annee_n1':fdtn, 'variation_p':vfdt}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '628000%'\
                            group by sub.code) as query")
            fba = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '628000%'\
                            group by sub.code) as query")
            fban = self.env.cr.fetchone()[0] or 0.0
            if fban != 0:
                vfba = ((fba - fban) / fban) * 100
            else:     
                vfba = 0
            line.append((0,0,{'name':'Frais bancaires', 'annee_n':fba, 'annee_n1':fban, 'variation_p':vfba}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '632000%'\
                            group by sub.code) as query")
            ric = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '632000%'\
                            group by sub.code) as query")
            ricn = self.env.cr.fetchone()[0] or 0.0
            if ricn != 0:
                vric = ((ric - ricn) / ricn) * 100 
            else:     
                vric = 0
            line.append((0,0,{'name':'Rémunération d’intermédiaires et de conseils', 'annee_n':ric, 'annee_n1':ricn, 'variation_p':vric}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '633000%'\
                            group by sub.code) as query")
            ffp = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '633000%'\
                            group by sub.code) as query")
            ffpn = self.env.cr.fetchone()[0] or 0.0
            if ffpn != 0:
                vffp = ((ffp - ffpn) / ffpn) * 100
            else:     
                vffp = 0
            line.append((0,0,{'name':'Frais de formation du persoonel', 'annee_n':ffp, 'annee_n1':ffpn, 'variation_p':vffp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '634000%'\
                            group by sub.code) as query")
            rpb = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '634000%'\
                            group by sub.code) as query")
            rpbn = self.env.cr.fetchone()[0] or 0.0
            if rpbn != 0:
                vrpb = ((rpb - rpbn) / rpbn) * 100
            else:     
                vrpb = 0
            line.append((0,0,{'name':'Redevances pour brevets, licences, logiciels, concession et droit similaires', 'annee_n':rpb, 'annee_n1':rpbn, 'variation_p':vrpb}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '635000%'\
                            group by sub.code) as query")
            coti = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '635000%'\
                            group by sub.code) as query")
            cotin = self.env.cr.fetchone()[0] or 0.0
            if cotin != 0:
                vcoti = ((coti - cotin) / cotin) * 100
            else:     
                vcoti = 0
            line.append((0,0,{'name':'Cotisations', 'annee_n':coti, 'annee_n1':cotin, 'variation_p':vcoti}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '638000%'\
                            group by sub.code) as query")
            ace = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '638000%'\
                            group by sub.code) as query")
            acen = self.env.cr.fetchone()[0] or 0.0
            if acen != 0:
                vace = ((ace - acen) / acen) * 100  
            else:     
                vace = 0
            line.append((0,0,{'name':'Autres charges externes', 'annee_n':ace, 'annee_n1':acen, 'variation_p':vace}))
            
            total = stg + lcl + erm + rla + pra + erd + pprp + fdt + fba + ric + ffp + rpb + coti + ace
            totaln = stgn + lcln + ermn + rlan + pran + erdn + pprpn + fdtn + fban +  ricn + ffpn + rpbn +cotin + acen
            if totaln != 0:
                vtotal = ((total - totaln) / totaln) * 100
            else:     
                vtotal = 0
            line.append((0,0,{'name':'TOTAL', 'annee_n':total, 'annee_n1':totaln, 'variation_p':vtotal}))
            self.note24_lines = line

    @api.onchange("note25")
    def onchange_note25(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note25 is True:
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '641000%'\
                            group by sub.code) as query")
            itd = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '641000%'\
                            group by sub.code) as query")
            itdn = self.env.cr.fetchone()[0] or 0.0
            if itdn != 0:
                vitd = ((itd - itdn) / itdn) * 100
            else:     
                vitd = 0
            line.append((0,0,{'name':'Impôts et taxe directs', 'annee_n':itd, 'annee_n1':itdn, 'variation_p':vitd}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '645000%'\
                            group by sub.code) as query")
            iti = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '645000%'\
                            group by sub.code) as query")
            itin = self.env.cr.fetchone()[0] or 0.0
            if itin != 0:
                viti = ((iti - itin) / itin) * 100
            else:     
                viti = 0
            line.append((0,0,{'name':'Impôts et taxe indirects', 'annee_n':iti, 'annee_n1':itin, 'variation_p':viti}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '646000%'\
                            group by sub.code) as query")
            dre = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '646000%'\
                            group by sub.code) as query")
            dren = self.env.cr.fetchone()[0] or 0.0
            if dren != 0:
                vdre = ((dre - dren) / dren) * 100
            else:     
                vdre = 0
            line.append((0,0,{'name':'Droits d’enregistrement', 'annee_n':dre, 'annee_n1':dren, 'variation_p':vdre}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '647000%'\
                            group by sub.code) as query")
            paf = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '647000%'\
                            group by sub.code) as query")
            pafn = self.env.cr.fetchone()[0] or 0.0
            if pafn != 0:
                vpaf = ((paf - pafn) / pafn) * 100
            else:     
                vpaf = 0
            line.append((0,0,{'name':'Pénalités et amendes fiscales', 'annee_n':paf, 'annee_n1':pafn, 'variation_p':vpaf}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '648000%'\
                            group by sub.code) as query")
            aip = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '648000%'\
                            group by sub.code) as query")
            aipn = self.env.cr.fetchone()[0] or 0.0
            if aipn != 0:
                vaip = ((aip - aipn) / aipn) * 100
            else:     
                vaip = 0
            line.append((0,0,{'name':'Autres impôts et taxes', 'annee_n':aip, 'annee_n1':aipn, 'variation_p':vaip}))
            
            total = itd + iti + dre + paf + aip
            totaln = itdn + itin + dren + pafn + aipn 
            if totaln != 0:
                vtotal = ((total - totaln) / totaln) * 100
            else:     
                vtotal = 0
            line.append((0,0,{'name':'TOTAL', 'annee_n':total, 'annee_n1':totaln, 'variation_p':vtotal}))
            self.note24_lines = line
            self.note25_lines = line

    @api.onchange("note26")
    def onchange_note26(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note26 is True:
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '6511%'\
                            group by sub.code) as query")
            pcc = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '6511%'\
                            group by sub.code) as query")
            pccn = self.env.cr.fetchone()[0] or 0.0
            if pccn != 0:
                vpcc = ((pcc - pccn) / pccn) * 100
            else:     
                vpcc = 0
            line.append((0,0,{'name':'Pertes sur créances clients', 'annee_n':pcc, 'annee_n1':pccn, 'variation_p':vpcc}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '6515%'\
                            group by sub.code) as query")
            pad = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '6515%'\
                            group by sub.code) as query")
            padn = self.env.cr.fetchone()[0] or 0.0
            if padn != 0:
                vpad = ((pad - padn) / padn) * 100
            else:     
                vpad = 0
            line.append((0,0,{'name':'Pertes sur autres débiteurs', 'annee_n':pad, 'annee_n1':padn, 'variation_p':vpad}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '652%'\
                            group by sub.code) as query")
            qpr = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '652%'\
                            group by sub.code) as query")
            qprn = self.env.cr.fetchone()[0] or 0.0
            if qprn != 0:
                vqpr = ((qpr - qprn) / qprn) * 100
            else:     
                vqpr = 0
            line.append((0,0,{'name':'Quote-part de résultat sur opération faite en commun', 'annee_n':qpr, 'annee_n1':qprn, 'variation_p':vqpr}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '654%'\
                            group by sub.code) as query")
            vcc = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '654%'\
                            group by sub.code) as query")
            vccn = self.env.cr.fetchone()[0] or 0.0
            if vccn != 0:
                vvcc = ((vcc - vccn) / vccn) * 100
            else:     
                vvcc = 0
            line.append((0,0,{'name':'Valeur comptable des cessions courantes d’immobilisations', 'annee_n':vcc, 'annee_n1':vccn, 'variation_p':vvcc}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '6581%'\
                            group by sub.code) as query")
            idf = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '6581%'\
                            group by sub.code) as query")
            idfn = self.env.cr.fetchone()[0] or 0.0
            if idfn != 0:
                vidf = ((idf - idfn) / idfn) * 100
            else:     
                vidf = 0
            line.append((0,0,{'name':'Indemnités de fonction et autres rémunérations d’administrateurs', 'annee_n':idf, 'annee_n1':idfn, 'variation_p':vidf}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '6582%' or sub.code like '6583%'\
                            group by sub.code) as query")
            dem = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '6582%' or sub.code like '6583%'\
                            group by sub.code) as query")
            demn = self.env.cr.fetchone()[0] or 0.0
            if demn != 0:
                vdem = ((dem - demn) / demn) * 100
            else:     
                vdem = 0
            line.append((0,0,{'name':'Dons et mécénat', 'annee_n':dem, 'annee_n1':demn, 'variation_p':vdem}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '6588%'\
                            group by sub.code) as query")
            acd = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '6588%'\
                            group by sub.code) as query")
            acdn = self.env.cr.fetchone()[0] or 0.0
            if acdn != 0:
                vacd = ((acd - acdn) / acdn) * 100
            else:     
                vacd = 0
            line.append((0,0,{'name':'Autres charges divers', 'annee_n':acd, 'annee_n1':acdn, 'variation_p':vacd}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '6591%'\
                            group by sub.code) as query")
            cpd = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '6591%'\
                            group by sub.code) as query")
            cpdn = self.env.cr.fetchone()[0] or 0.0
            if cpdn != 0:
                vcpd = ((cpd - cpdn) / cpdn) * 100
            else:     
                vcpd = 0
            line.append((0,0,{'name':'Charges pour dépréciation et provisions pour risques à court terme d’exploitation', 'annee_n':cpd, 'annee_n1':cpdn, 'variation_p':vcpd}))
            
            total = pcc + pad + qpr + vcc + idf + dem + acd + cpd 
            totaln = pccn + padn + qprn + vccn + idfn + demn + acdn + cpdn
            if totaln != 0:
                vtotal = ((total - totaln) / totaln) * 100
            else:     
                vtotal = 0
            line.append((0,0,{'name':'TOTAL', 'annee_n':total, 'annee_n1':totaln, 'variation_p':vtotal}))
            self.note26_lines = line

    @api.onchange("note27A")
    def onchange_note27A(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note27A is True:
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '661%' or sub.code like '662%'\
                            group by sub.code) as query")
            rdv = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '661%' or sub.code like '662%'\
                            group by sub.code) as query")
            rdvn = self.env.cr.fetchone()[0] or 0.0
            if rdvn != 0:
                vrdv = ((rdv - rdvn) / rdvn) * 100
            else:     
                vrdv = 0
            line.append((0,0,{'name':'Rémunérations directes versées au personnel', 'annee_n':rdv, 'annee_n1':rdvn, 'variation_p':vrdv}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '663%'\
                            group by sub.code) as query")
            ifv = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '663%'\
                            group by sub.code) as query")
            ifvn = self.env.cr.fetchone()[0] or 0.0
            if ifvn != 0:
                vifv = ((ifv - ifvn) / ifvn) * 100
            else:     
                vifv = 0
            line.append((0,0,{'name':'Indemnités forfaitaires versées au personnel', 'annee_n':ifv, 'annee_n1':ifvn, 'variation_p':vifv}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '664%'\
                            group by sub.code) as query")
            cso = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '664%'\
                            group by sub.code) as query")
            cson = self.env.cr.fetchone()[0] or 0.0
            if cson != 0:
                vcso = ((cso - cson) / cson) * 100
                if vcso < 0:
                    vcso = -vcso  
            else:     
                vcso = 0
            line.append((0,0,{'name':'Charges sociales', 'annee_n':cso, 'annee_n1':cson, 'variation_p':vcso}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '666%'\
                            group by sub.code) as query")
            rcs = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '666%'\
                            group by sub.code) as query")
            rcsn = self.env.cr.fetchone()[0] or 0.0
            if rcsn != 0:
                vrcs = ((rcs - rcsn) / rcsn) * 100
            else:     
                vrcs = 0
            line.append((0,0,{'name':'Rémunérations et charges sociales de l\'exploitant individuel', 'annee_n':rcs, 'annee_n1':rcsn, 'variation_p':vrcs}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '667%'\
                            group by sub.code) as query")
            rtp = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '667%'\
                            group by sub.code) as query")
            rtpn = self.env.cr.fetchone()[0] or 0.0
            if rtpn != 0:
                vrtp = ((rtp - rtpn) / rtpn) * 100
            else:     
                vrtp = 0
            line.append((0,0,{'name':'Rémunération transférée de personnel extérieur', 'annee_n':rtp, 'annee_n1':rtpn, 'variation_p':vrtp}))
                
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '668%'\
                            group by sub.code) as query")
            acs = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '668%'\
                            group by sub.code) as query")
            acsn = self.env.cr.fetchone()[0] or 0.0
            if acsn != 0:
                vacs = ((acs - acsn) / acsn) * 100
            else:     
                vacs = 0    
            line.append((0,0,{'name':'Autres charges sociales', 'annee_n':acs, 'annee_n1':acsn, 'variation_p':vacs}))
            
            total = rdv + ifv + cso +  rcs + rtp + acs
            totaln = rdvn + ifvn + cson + rcsn + rtpn + acsn
            if totaln != 0:
                vtotal = ((total - totaln) / totaln) * 100
            else:     
                vtotal = 0
            line.append((0,0,{'name':'TOTAL', 'annee_n':total, 'annee_n1':totaln, 'variation_p':vtotal}))           

            self.note27A_lines = line


    @api.onchange("note28")
    def onchange_note28(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note28 is True:
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '15%'\
                            group by sub.code) as query")
            prrn = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '19%'\
                            group by sub.code) as query")
            prr = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Provisions réglementées', 'provision_ouverture':prrn, 'provision_cloturre':prr}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '19%'\
                            group by sub.code) as query")
            pfprcn = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '29%'\
                            group by sub.code) as query")
            pfprc = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Provisions financiéres pour risques et charges', 'provision_ouverture':prrn, 'provision_cloturre':prr}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '29%'\
                            group by sub.code) as query")
            ddin = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '29%'\
                            group by sub.code) as query")
            ddi = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Dépréciations des immobilisations', 'provision_ouverture':ddin, 'provision_cloturre':ddi}))
            
            total_dn = prrn + pfprcn + ddin
            total_d = prr + pfprc + ddi
            line.append((0,0,{'name':'TOTAL : DOTATIONS', 'provision_ouverture':total_dn, 'provision_cloturre':total_d}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '39%'\
                            group by sub.code) as query")
            ddsn = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '39%'\
                            group by sub.code) as query")
            dds = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Dépréciations des stocks', 'provision_ouverture':ddsn, 'provision_cloturre':dds}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '498%'\
                            group by sub.code) as query")
            dacn = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '498%'\
                            group by sub.code) as query")
            dac = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Dépréciations actif circulant HAO', 'provision_ouverture':dacn, 'provision_cloturre':dac}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '490%'\
                            group by sub.code) as query")
            depfn = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '490%'\
                            group by sub.code) as query")
            depf = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Dépréciations fournisseurs', 'provision_ouverture':depfn, 'provision_cloturre':depf}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '491%'\
                            group by sub.code) as query")
            depcn = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '491%'\
                            group by sub.code) as query")
            depc = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Dépréciations clients', 'provision_ouverture':depcn, 'provision_cloturre':depc}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '492%' or sub.code like '493%' or sub.code like '494%' or sub.code like '495%' or sub.code like '496%' or sub.code like '497%'\
                            group by sub.code) as query")
            dacn = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '492%' or sub.code like '493%' or sub.code like '494%' or sub.code like '495%' or sub.code like '496%' or sub.code like '497%'\
                            group by sub.code) as query")
            dac = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Dépréciations autres créances', 'provision_ouverture':dacn, 'provision_cloturre':dac}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '590%'\
                            group by sub.code) as query")
            dtpn = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '590%'\
                            group by sub.code) as query")
            dtp = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Dépréciations titres de placement', 'provision_ouverture':dtpn, 'provision_cloturre':dtp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '591%'\
                            group by sub.code) as query")
            dven = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '591%'\
                            group by sub.code) as query")
            dve = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Dépréciations valeurs à encaisser', 'provision_ouverture':dven, 'provision_cloturre':dve}))
                
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '592%' or sub.code like '593%' or sub.code like '594%'\
                            group by sub.code) as query")
            depdn = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '592%' or sub.code like '593%' or sub.code like '594%'\
                            group by sub.code) as query")
            depd = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Dépréciations disponibilité', 'provision_ouverture':depdn, 'provision_cloturre':depd}))
              
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4991%' or sub.code like '4997%'\
                            group by sub.code) as query")
            dpprn = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '4991%' or sub.code like '4997%'\
                            group by sub.code) as query")
            dppr = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Dépréciations et provisions pour risques à court termes exploitation', 'provision_ouverture':dpprn, 'provision_cloturre':dppr}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_debut)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '599%'\
                            group by sub.code) as query")
            dpprfn = self.env.cr.fetchone()[0] or 0.0
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '599%'\
                            group by sub.code) as query")
            dpprf = self.env.cr.fetchone()[0] or 0.0
            line.append((0,0,{'name':'Dépréciations et provisions pour risques à court termes à caractére financier', 'provision_ouverture':dpprfn, 'provision_cloturre':dpprf}))
            
            total_cn = ddsn + dacn + depfn + depcn + dacn + dtpn + dven + depdn + dpprn + dpprfn
            total_c = dds + dac + depf + depc + dac + dtp + dve + depd + dppr + dpprf
            line.append((0,0,{'name':'TOTAL: CHARGE POUR DEPRECIATIONS ET PROVISIONS A COURT TERME', 'provision_ouverture':total_cn, 'provision_cloturre':total_c}))
            
            totaln = total_dn + total_cn
            total = total_d + total_c 
            line.append((0,0,{'name':'TOTAL', 'provision_ouverture':totaln, 'provision_cloturre':total}))
            self.note28_lines = line

    @api.onchange("note29")
    def onchange_note29(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note29 is True:
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '671%'\
                            group by sub.code) as query")
            ide = self.env.cr.fetchone()[0] or 0.0
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '671%'\
                            group by sub.code) as query")
            iden = self.env.cr.fetchone()[0] or 0.0
            if iden != 0:
                vide = ((iden - iden) / iden) * 100 
            else:     
                vide = 0  
            line.append((0,0,{'name':'Intérêts des emprunts', 'annee_n':ide, 'annee_n1':iden, 'variation':vide}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '672%'\
                            group by sub.code) as query")
            idlla = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '672%'\
                            group by sub.code) as query")
            idllan = self.env.cr.fetchone()[0] or 0.0
            if idllan != 0:
                vidlla = ((idllan - idllan) / idllan) * 100
            else:     
                vidlla = 0
            line.append((0,0,{'name':'Intérêts dans loyers de location acquisition', 'annee_n':idlla, 'annee_n1':idllan, 'variation':vidlla}))
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '673%'\
                            group by sub.code) as query")
            esa = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '673%'\
                            group by sub.code) as query")
            esan = self.env.cr.fetchone()[0] or 0.0
            if esan != 0:
                vesa = ((esa - esan) / esan) * 100
            else:     
                vesa = 0
            line.append((0,0,{'name':'Escomptes accordés', 'annee_n':esa, 'annee_n1':esan, 'variation':vesa}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '674%'\
                            group by sub.code) as query")
            aui = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '674%'\
                            group by sub.code) as query")
            auin = self.env.cr.fetchone()[0] or 0.0
            if auin != 0:
                vaui = ((aui - auin) / auin) * 100
            else:     
                vaui = 0
            line.append((0,0,{'name':'Autres intérêts', 'annee_n':aui, 'annee_n1':auin, 'variation':vaui}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '675%'\
                            group by sub.code) as query")
            edec = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '675%'\
                            group by sub.code) as query")
            edecn = self.env.cr.fetchone()[0] or 0.0
            if edecn != 0:
                vedec = ((edec - edecn) / edecn) * 100
            else:     
                vedec = 0
            line.append((0,0,{'name':'Escomptes des effets de commerce', 'annee_n':edec, 'annee_n1':edecn, 'variation':vedec}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '676%'\
                            group by sub.code) as query")
            pdc = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '676%'\
                            group by sub.code) as query")
            pdcn = self.env.cr.fetchone()[0] or 0.0
            if pdcn != 0:
                vpdc = ((pdc - pdcn) / pdcn) * 100
            else:     
                vpdc = 0
            line.append((0,0,{'name':'Pertes de change', 'annee_n':pdc, 'annee_n1':pdcn, 'variation':vpdc}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '6771%'\
                            group by sub.code) as query")
            pctp = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '6771%'\
                            group by sub.code) as query")
            pctpn = self.env.cr.fetchone()[0] or 0.0
            if pctpn != 0:
                vpctp = ((pctp - pctpn) / pctpn) * 100
            else:     
                vpctp = 0
            line.append((0,0,{'name':'Perte sur cessions de titre de placement', 'annee_n':pctp, 'annee_n1':pctpn, 'variation':vpctp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '6772%'\
                            group by sub.code) as query")
            mpa = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '6772%'\
                            group by sub.code) as query")
            mpan = self.env.cr.fetchone()[0] or 0.0
            if mpan != 0:
                vmpa = ((mpa - mpan) / mpan) * 100
            else:     
                vmpa = 0
            line.append((0,0,{'name':'Malis provenant d’attribution gratuite d’actions au personnel salarié et aux dirigeants', 'annee_n':mpa, 'annee_n1':mpan, 'variation':vmpa}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '678%'\
                            group by sub.code) as query")
            prf = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '678%'\
                            group by sub.code) as query")
            prfn = self.env.cr.fetchone()[0] or 0.0
            if prfn != 0:
                vprf = ((prf - prfn) / prfn) * 100
            else:     
                vprf = 0
            line.append((0,0,{'name':'Pertes sur risques financiers', 'annee_n':prf, 'annee_n1':prfn, 'variation':vprf}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '679%'\
                            group by sub.code) as query")
            cpd = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '679%'\
                            group by sub.code) as query")
            cpdn = self.env.cr.fetchone()[0] or 0.0
            if cpdn != 0:
                vcpd = ((cpd - cpdn) / cpdn) * 100
            else:     
                vcpd = 0
            line.append((0,0,{'name':'Charges pour dépréciation et provisions à court terme à caractére financier', 'annee_n':cpd, 'annee_n1':cpdn, 'variation':vcpd}))
            
            stf = ide + idlla + esa + aui + edec + pdc + pctp + mpa + prf + cpd 
            stfn = iden + idllan + esan + auin + edecn + pdcn + pctpn + mpan + prfn + cpdn
            if stfn != 0:
                vstf = ((stf - stfn) / stfn) * 100
            else:     
                vstf = 0
            line.append((0,0,{'name':'SOUS TOTAL : FRAIS FINANCIERS', 'annee_n':stf, 'annee_n1':stfn, 'variation':vstf}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '771%'\
                            group by sub.code) as query")
            ipc = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '771%'\
                            group by sub.code) as query")
            ipcn = self.env.cr.fetchone()[0] or 0.0
            if ipcn != 0:
                vipc = ((ipc - ipcn) / ipcn) * 100
            else:     
                vipc = 0
            line.append((0,0,{'name':'Intérêts de prêts et créances diverses', 'annee_n':ipc, 'annee_n1':ipcn, 'variation':vipc}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '7721%'\
                            group by sub.code) as query")
            rdp = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '7721%'\
                            group by sub.code) as query")
            rdpn = self.env.cr.fetchone()[0] or 0.0
            if rdpn != 0:
                vrdp = ((rdp - rdpn) / rdpn) * 100
            else:     
                vrdp = 0
            line.append((0,0,{'name':'Revenus de participation', 'annee_n':rdp, 'annee_n1':rdpn, 'variation':vrdp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '773%'\
                            group by sub.code) as query")
            eso = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '773%'\
                            group by sub.code) as query")
            eson = self.env.cr.fetchone()[0] or 0.0
            if eson != 0:
                veso = ((eso - eson) / eson) * 100
            else:     
                veso = 0            
            line.append((0,0,{'name':'Escomptes obtenus', 'annee_n':eso, 'annee_n1':eson, 'variation':veso}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '774%'\
                            group by sub.code) as query")
            revp = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '774%'\
                            group by sub.code) as query")
            revpn = self.env.cr.fetchone()[0] or 0.0
            if revpn != 0:
                vrevp = ((revp - revpn) / revpn) * 100
            else:     
                vrevp = 0
            line.append((0,0,{'name':'Revenus de placement', 'annee_n':revp, 'annee_n1':revpn, 'variation':vrevp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '776%'\
                            group by sub.code) as query")
            gdc = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '776%'\
                            group by sub.code) as query")
            gdcn = self.env.cr.fetchone()[0] or 0.0
            if gdcn != 0:
                vgdc = ((gdc - gdcn) / gdcn) * 100
            else:     
                vgdc = 0
            line.append((0,0,{'name':'Gains de change', 'annee_n':gdc, 'annee_n1':gdcn, 'variation':vgdc}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '777%'\
                            group by sub.code) as query")
            gsc = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '777%'\
                            group by sub.code) as query")
            gscn = self.env.cr.fetchone()[0] or 0.0
            if gscn != 0:
                vgsc = ((gsc - gscn) / gscn) * 100
            else:     
                vgsc = 0
            line.append((0,0,{'name':'Gains sur cessions de titres de placement', 'annee_n':gsc, 'annee_n1':gscn, 'variation':vgsc}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '778%'\
                            group by sub.code) as query")
            grf = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '778%'\
                            group by sub.code) as query")
            grfn = self.env.cr.fetchone()[0] or 0.0
            if grfn != 0:
                vgrf = ((grf - grfn) / grfn) * 100
            else:     
                vgrf = 0
            line.append((0,0,{'name':'Gains sur risques financiers', 'annee_n':grf, 'annee_n1':grfn, 'variation':vgrf}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '779%'\
                            group by sub.code) as query")
            repc = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '779%'\
                            group by sub.code) as query")
            repcn = self.env.cr.fetchone()[0] or 0.0
            if repcn != 0:
                vrepc = ((repc - repcn) / repcn) * 100
            else:     
                vrepc = 0
            line.append((0,0,{'name':'Reprises de charges pour dépréciation et provisions à court terme à caractére financier', 'annee_n':repc, 'annee_n1':repcn, 'variation':vrepc}))
            
            strf = ipc + rdp + eso + revp + gdc + gsc + grf + repc
            strfn = ipcn + rdpn + eson + revpn + gdcn + gscn + grfn + repcn
            if strfn != 0:
                vstrf = ((strf - strfn) / strfn) * 100
            else:     
                vstrf = 0
            line.append((0,0,{'name':'SOUS TOTAL : REVENUS FINANCIERS', 'annee_n':strf, 'annee_n1':strfn, 'variation':vstrf}))
            self.note29_lines = line

    @api.onchange("note30")
    def onchange_note30(self):
        line = []
        if self.date_debut and self.date_fin:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
        if self.note30 is True:
            line.append((0,0,{'name':'Charges HAO constatées (1) à détailler'}))
            line.append((0,0,{'name':'(1) ...........................................................'}))
            line.append((0,0,{'name':'(1) ...........................................................'}))
            line.append((0,0,{'name':'(1) ...........................................................'}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '834%'\
                            group by sub.code) as query")
            psc = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '834%'\
                            group by sub.code) as query")
            pscn = self.env.cr.fetchone()[0] or 0.0
            if pscn != 0:
                vpsc = ((psc - pscn) / pscn) * 100
            else:     
                vpsc = 0
            line.append((0,0,{'name':'Perte sur créances HAO', 'annee_n':psc, 'annee_n1':pscn, 'variation':vpsc}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '835%'\
                            group by sub.code) as query")
            dla = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '835%'\
                            group by sub.code) as query")
            dlan = self.env.cr.fetchone()[0] or 0.0
            if dlan != 0:
                vdla = ((dla - dlan) / dlan) * 100
            else:     
                vdla = 0
            line.append((0,0,{'name':'Dons et libéralités accordés', 'annee_n':dla, 'annee_n1':dlan, 'variation':vdla}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '836%'\
                            group by sub.code) as query")
            abc = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '836%'\
                            group by sub.code) as query")
            abcn = self.env.cr.fetchone()[0] or 0.0
            if abcn != 0:
                vabc = ((abc - abcn) / abcn) * 100
            else:     
                vabc = 0
            line.append((0,0,{'name':'Abandon de créances consentis', 'annee_n':abc, 'annee_n1':abcn, 'variation':vabc}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '839%'\
                            group by sub.code) as query")
            cph = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '839%'\
                            group by sub.code) as query")
            cphn = self.env.cr.fetchone()[0] or 0.0
            if cphn != 0:
                vcph = ((cph - cphn) / cphn) * 100
            else:     
                vcph = 0
            line.append((0,0,{'name':'Charges provisionneées HAO', 'annee_n':cph, 'annee_n1':cphn, 'variation':vcph}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '85%'\
                            group by sub.code) as query")
            dha = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '85%'\
                            group by sub.code) as query")
            dhan = self.env.cr.fetchone()[0] or 0.0
            if dhan != 0:
                vdha = ((dha - dhan) / dhan) * 100
            else:     
                vdha = 0
            line.append((0,0,{'name':'Dotation hors activités ordinaires', 'annee_n':dha, 'annee_n1':dhan, 'variation':vdha}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '87%'\
                            group by sub.code) as query")
            pdt = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '87%'\
                            group by sub.code) as query")
            pdtn = self.env.cr.fetchone()[0] or 0.0
            if pdtn != 0:
                vpdt = ((pdt - pdtn) / pdtn) * 100
            else:     
                vpdt = 0
            line.append((0,0,{'name':'Participation des travailleurs', 'annee_n':pdt, 'annee_n1':pdtn, 'variation':vpdt}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '88%'\
                            group by sub.code) as query")
            sube = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '88%'\
                            group by sub.code) as query")
            suben = self.env.cr.fetchone()[0] or 0.0
            if suben != 0:
                vsube = ((sube - suben) / suben) * 100
            else:     
                vsube = 0
            line.append((0,0,{'name':'Subvention d’équilibre', 'annee_n':sube, 'annee_n1':suben, 'variation':vsube}))
            
            sthao = psc + dla + abc + cph + dha + pdt + sube
            sthaon = pscn + dlan + abcn + cphn + dhan + pdtn + suben
            if sthaon != 0:
                vsthao = ((str - sthaon) / sthaon) * 100
            else:     
                vsthao = 0
            line.append((0,0,{'name':'SOUS TOTAL: AUTRES CHARGES HAO', 'annee_n':sthao, 'annee_n1':sthaon, 'variation':vsthao}))
            
            line.append((0,0,{'name':'Produits HAO constatés (1) à détailler'}))
            line.append((0,0,{'name':'(1) ...........................................................'}))
            line.append((0,0,{'name':'(1) ...........................................................'}))
            line.append((0,0,{'name':'(1) ...........................................................'}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '845%'\
                            group by sub.code) as query")
            dlo = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '845%'\
                            group by sub.code) as query")
            dlon = self.env.cr.fetchone()[0] or 0.0
            if dlon != 0:
                vdlo = ((dlo - dlon) / dlon) * 100
            else:     
                vdlo = 0
            line.append((0,0,{'name':'Dons et libéralités obtenus', 'annee_n':dlo, 'annee_n1':dlon, 'variation':vdlo}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '846%'\
                            group by sub.code) as query")
            aco = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '846%'\
                            group by sub.code) as query")
            acon = self.env.cr.fetchone()[0] or 0.0
            if acon != 0:
                vaco = ((aco - acon) / acon) * 100
            else:     
                vaco = 0
            line.append((0,0,{'name':'Abandon de créances obtenus', 'annee_n':aco, 'annee_n1':acon, 'variation':vaco}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '848%'\
                            group by sub.code) as query")
            tch = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '848%'\
                            group by sub.code) as query")
            tchn = self.env.cr.fetchone()[0] or 0.0
            if tchn != 0:
                vtch = ((tch - tchn) / tchn) * 100
            else:     
                vtch = 0
            line.append((0,0,{'name':'Transferts de charges HAO', 'annee_n':tch, 'annee_n1':tchn, 'variation':vtch}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '849%'\
                            group by sub.code) as query")
            rcdp = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '849%'\
                            group by sub.code) as query")
            rcdpn = self.env.cr.fetchone()[0] or 0.0
            if rcdpn != 0:
                vrcdp = ((rcdp - rcdpn) / rcdpn) * 100
            else:     
                vrcdp = 0
            line.append((0,0,{'name':'Reprises des charges pour dépréciations et provisions à court terme HAO', 'annee_n':rcdp, 'annee_n1':rcdpn, 'variation':vrcdp}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '861%' or sub.code like '862%' or sub.code like '863%' or sub.code like '864%' or sub.code like '868%'\
                            group by sub.code) as query")
            rhao = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '861%' or sub.code like '862%' or sub.code like '863%' or sub.code like '864%' or sub.code like '868%'\
                            group by sub.code) as query")
            rhaon = self.env.cr.fetchone()[0] or 0.0
            if rhaon != 0:
                vrhao = ((rhao - rhaon) / rhaon) * 100 
            else:     
                vrhao = 0
            line.append((0,0,{'name':'Reprises hors activités ordinaire', 'annee_n':rhao, 'annee_n1':rhaon, 'variation':vrhao}))
            
            stphao = dlo + aco + tch + rcdp + rhao
            stphaon = dlon + acon + tchn + rcdpn + rhaon
            if stphaon != 0:
                vstphao = ((stphao - stphaon) / stphaon) * 100
            else:     
                vstphao = 0
            line.append((0,0,{'name':'SOUS TOTAL : AUTRES PRODUITS HAO', 'annee_n':stphao, 'annee_n1':stphaon, 'variation':vstphao}))
            
            total = sthao + stphao
            totaln = sthaon + stphaon
            if totaln != 0:
                vtotal = ((total - totaln) / totaln) * 100
            else:     
                vtotal = 0
            line.append((0,0,{'name':'TOTAL', 'annee_n':total, 'annee_n1':totaln, 'variation':vtotal}))
            self.note30_lines = line

    @api.onchange("note31")
    def onchange_note31(self):
        line = []
        if self.note31 is True:
            line.append((0,0,{'name':'STRUCTURE DU CAPITAL A LA CLOTURE DE L’EXERCICE'}))
            line.append((0,0,{'name':'Capital social'}))
            line.append((0,0,{'name':'Actions ordinaires'}))
            line.append((0,0,{'name':'Actions et dividendes prioritaires (A.D.P) sans droit de vote'}))
            line.append((0,0,{'name':'Actions nouvelles à émettre :'}))
            line.append((0,0,{'name':'        -par conversion d’obligations'}))
            line.append((0,0,{'name':'        -par exercice de droits de souscription'}))
            line.append((0,0,{'name':'OPERATIONS ET RESULTAT DE L’EXERCICE'}))
            line.append((0,0,{'name':'Résultat des activités ordinaires (R.A.O) hors dotations et reprises (exploitation et financiére)'}))
            line.append((0,0,{'name':'Participaton des travailleurs aux bénéfices'}))
            line.append((0,0,{'name':'Impôt sur le résultat'}))
            line.append((0,0,{'name':'Résultat net'}))
            line.append((0,0,{'name':'RESULTAT ET DIVIDENDES DISTRIBUES'}))
            line.append((0,0,{'name':'Résultat distribué'}))
            line.append((0,0,{'name':'Dividende attribuée à chaque action'}))
            line.append((0,0,{'name':'PERSONNEL ET POLITIQUE SALARIALE'}))
            line.append((0,0,{'name':'Effectif moyen personnel extérieur'}))
            line.append((0,0,{'name':'Masse salariale distribuée au cours de l’exercice'}))
            line.append((0,0,{'name':'Avantages sociaux versés au cours de l’exercice [Sécurité sociale, oeuvres sociales]'}))
            line.append((0,0,{'name':'Personnel extérieur facturé à l’entité'}))
            self.note31_lines = line

    @api.onchange("note32")
    def onchange_note32(self):
        line = []
        if self.note32 is True:
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':'NON VENTILLE'}))
            line.append((0,0,{'name':'TOTAL'}))
            self.note32_lines = line

    @api.onchange("note33")
    def onchange_note33(self):
        line = []
        if self.note33 is True:
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':'TOTAL'}))
            self.note33_lines = line

    @api.onchange("note34")
    def onchange_note34(self):
        line = []
        if self.date_debut and self.date_fin:
            compte_resultat = self.env['optesis.compte.resultat']._get_report_values(self.company_id.id, self.date_debut, self.date_fin)
            bilan = self.env['optesis.bilan']._get_report_values(self.company_id.id, self.date_debut, self.date_fin)
            tft = self.env['optesis.tft']._get_report_values(self.company_id.id, self.date_debut, self.date_fin)
        if self.note34 is True:
            debut_n = self.date_debut - relativedelta(years=+1)
            fin_n = self.date_fin - relativedelta(years=+1)
            
            xb = compte_resultat.get('xb_net') or 0.0
            xbn = compte_resultat.get('xbn_net') or 0.0
            if xbn != 0:
                vxb = ((xb - xbn) / xbn) * 100
            else:     
                vxb = 0
            line.append((0,0,{'name':'Chiffre d’affaires', 'annee_n':xb, 'annee_n1':xbn, 'variation':vxb}))
            
            xa = compte_resultat.get('xa_net') or 0.0
            xan = compte_resultat.get('xan_net') or 0.0 
            if xan != 0:
                vxa = ((xa - xan) / xan) * 100
            else:     
                vxa = 0
            line.append((0,0,{'name':'Marge commerciale', 'annee_n':xa, 'annee_n1':xan, 'variation':vxa}))
            
            xc = compte_resultat.get('xc_net') or 0.0
            xcn = compte_resultat.get('xcn_net') or 0.0
            if xcn != 0:
                vxc = ((xc - xcn) / xcn) * 100
            else:     
                vxc = 0
            line.append((0,0,{'name':'Valeur ajoutée', 'annee_n':xc, 'annee_n1':xcn, 'variation':vxc}))
            
            xd = compte_resultat.get('xd_net') or 0.0
            xdn = compte_resultat.get('xdn_net') or 0.0 
            if xdn != 0:
                vxd = ((xd - xdn) / xdn) * 100
            else:     
                vxd = 0
            line.append((0,0,{'name':'Excédent Brut d’exploitation (EBE)', 'annee_n':xd, 'annee_n1':xdn, 'variation':vxd}))
            
            xe = compte_resultat.get('xe_net') or 0.0
            xen = compte_resultat.get('xen_net') or 0.0
            if xen != 0:
                vxe = ((xe - xen) / xen) * 100 
            else:     
                vxe = 0
            line.append((0,0,{'name':'Résultat d’exploitation', 'annee_n':xe, 'annee_n1':xen, 'variation':vxe}))
            
            xf = compte_resultat.get('xf_net') or 0.0
            xfn = compte_resultat.get('xfn_net') or 0.0 
            if xfn != 0:
                vxf = ((xf - xfn) / xfn) * 100
            else:     
                vxf = 0
            line.append((0,0,{'name':'Résultat financier', 'annee_n':xf, 'annee_n1':xfn, 'variation':vxf}))
            
            xg = compte_resultat.get('xg_net') or 0.0
            xgn = compte_resultat.get('xgn_net') or 0.0
            if xgn != 0:
                vxg = ((xg - xgn) / xgn) * 100 
            else:     
                vxg = 0
            line.append((0,0,{'name':'Résultat des activités ordinaires', 'annee_n':xg, 'annee_n1':xgn, 'variation':vxg}))
            
            xh = compte_resultat.get('xh_net') or 0.0
            xhn = compte_resultat.get('xhn_net') or 0.0
            if xhn != 0:
                vxh = ((xh - xhn) / xhn) * 100
            else:     
                vxh = 0
            line.append((0,0,{'name':'Résultat hors activités ordinaires', 'annee_n':xh, 'annee_n1':xhn, 'variation':vxh}))
            
            xi = compte_resultat.get('xi_net') or 0.0
            xin = compte_resultat.get('xin_net') or 0.0
            if xin != 0:
                vxi = ((xi - xin) / xin) * 100
            else:     
                xi = 0
            line.append((0,0,{'name':'Résultat net', 'annee_n':xi, 'annee_n1':xin, 'variation':vxi}))
            
            xd = compte_resultat.get('xd_net') or 0.0
            xdn = compte_resultat.get('xdn_net') or 0.0
            if xdn != 0:
                vxd = ((xd - xdn) / xdn) * 100
            else:     
                vxd = 0
            line.append((0,0,{'name':'DETERMINATION DE LA CAPACITE D’AUTOFINANCEMENT EBE', 'annee_n':xd, 'annee_n1':xdn, 'variation':vxd}))
            
            ro = compte_resultat.get('ro_net') or 0.0
            ron = compte_resultat.get('ron_net') or 0.0
            if ron != 0:
                vro = ((ro - ron) / ron) * 100
            else:     
                vro = 0
            line.append((0,0,{'name':'+Valeurs comptable des cessions courantes d\'immobilisation', 'annee_n':ro, 'annee_n1':ron, 'variation':vro}))
            
            tn = compte_resultat.get('tn_net') or 0.0
            tnn = compte_resultat.get('tnn_net') or 0.0
            if tnn != 0:
                vtn = ((tn - tnn) / tnn) * 100
            else:     
                vtn = 0
            line.append((0,0,{'name':'-Produits des cessions courantes d\'immobilisation', 'annee_n':tn, 'annee_n1':tnn, 'variation':vtn}))
            
            ehf = xd + ro - tn 
            ehfn = xdn + ron - tnn
            if ehfn != 0:
                vehf = ((ehf - ehfn) / ehfn) * 100
            else:     
                vehf = 0
            line.append((0,0,{'name':'= EBE hors flux de cessions courantes d\'immobilisation', 'annee_n':ehf, 'annee_n1':ehfn, 'variation':vehf}))
                        
            line.append((0,0,{'name':'CAPACITE D’AUTOFINANCEMENT D\'EXPLOITATION', 'annee_n':ehf, 'annee_n1':ehfn, 'variation':vehf}))         
            
            tk = compte_resultat.get('tk_net') or 0.0
            tkn = compte_resultat.get('tkn_net') or 0.0
            if tkn != 0:
                vtk = ((tk - tkn) / tkn) * 100
            else:     
                vtk = 0
            line.append((0,0,{'name':'+ Revenus financiers', 'annee_n':tk, 'annee_n1':tkn, 'variation':vtk}))
            
            tl = compte_resultat.get('tl_net') or 0.0
            tln = compte_resultat.get('tln_net') or 0.0
            if tln != 0:
                vtl = ((tl - tln) / tln) * 100
            else:     
                vtl = 0    
            line.append((0,0,{'name':'+ Gain de change', 'annee_n':tl, 'annee_n1':tln, 'variation':vtl}))
            
            tm = compte_resultat.get('tm_net') or 0.0
            tmn = compte_resultat.get('tmn_net') or 0.0
            if tmn != 0:
                vtm = ((tm - tmn) / tmn) * 100 
            else:     
                vtm = 0  
            line.append((0,0,{'name':' + Transferts de charges financières', 'annee_n':tm, 'annee_n1':tmn, 'variation':vtm}))
            
            to = compte_resultat.get('to_net') or 0.0
            ton = compte_resultat.get('ton_net') or 0.0
            
            if ton != 0:
                vto = ((to - ton) / ton) * 100
            else:     
                vto = 0
            line.append((0,0,{'name':'+ Produis HAO', 'annee_n':to, 'annee_n1':ton, 'variation':vto}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(self.date_debut)+"' and  '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '848%'\
                            group by sub.code) as query")
            tfhao = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '848%'\
                            group by sub.code) as query")
            tfhaon = self.env.cr.fetchone()[0] or 0.0
            
            if tfhaon != 0:
                vtfhao = ((tfhao - tfhaon) / tfhaon) * 100
            else:     
                vtfhao = 0
            line.append((0,0,{'name':'+ Transferts de charges HAO', 'annee_n':tfhao, 'annee_n1':tfhaon, 'variation':vtfhao}))
            
            rm = compte_resultat.get('rm_net') or 0.0
            rmn = compte_resultat.get('rmn_net') or 0.0
            if rmn != 0:
                vrm = ((rm - rmn) / rmn) * 100
            else:     
                vrm = 0
            line.append((0,0,{'name':'- Frais financiers', 'annee_n':rm, 'annee_n1':rmn, 'variation':vrm}))
            
            rn = compte_resultat.get('rn_net') or 0.0
            rnn = compte_resultat.get('rnn_net') or 0.0
            if rnn != 0:
                vrn = ((rn - rnn) / rnn) * 100
            else:     
                vrn = 0
            line.append((0,0,{'name':'-Pertes de change', 'annee_n':rn, 'annee_n1':rnn, 'variation':vrn}))
            
            rp = compte_resultat.get('rp_net') or 0.0
            rpn = compte_resultat.get('rpn_net') or 0.0
            if rpn != 0:
                vrp = ((rp - rpn) / rpn) * 100
            else:     
                vrp = 0
            line.append((0,0,{'name':'-Charge HAO', 'annee_n':rp, 'annee_n1':rpn, 'variation':vrp}))
            
            rq = compte_resultat.get('rq_net') or 0.0
            rqn = compte_resultat.get('rqn_net') or 0.0
            if rqn != 0:
                vrq = ((rq - rqn) / rqn) * 100 
            else:     
                vrq = 0
            line.append((0,0,{'name':'-Participation', 'annee_n':rq, 'annee_n1':rqn, 'variation':vrq}))
            
            rs = compte_resultat.get('rs_net') or 0.0
            rsn = compte_resultat.get('rsn_net') or 0.0
            if rsn != 0:
                vrs = ((rs - rsn) / rsn) * 100
            else:     
                vrs = 0
            line.append((0,0,{'name':'- Impôt sur les résultats', 'annee_n':rs, 'annee_n1':rsn, 'variation':vrs}))
            
            cafg = tk + tl + tm + to + tfhao - rm - rn - rp - rq - rs
            cafgn = tkn + tln + ton + tfhaon - rmn - rnn - rpn - rqn - rsn
            if cafgn != 0:
                vcafg = ((cafg - cafgn) / cafgn) * 100
            else:     
                vcafg = 0
            line.append((0,0,{'name':'= CAPACITE D’AUTOFINANCEMENT GLOBALE (C.A.F.G)', 'annee_n':cafg, 'annee_n1':cafgn, 'variation':vcafg}))
            
            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(self.date_fin)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                            where sub.code like '465%'\
                            group by sub.code) as query")
            fn = self.env.cr.fetchone()[0] or 0.0

            self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                                (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(self.company_id.id)+"') as sub\
                                where sub.code like '465%'\
                                group by sub.code) as query")
            fnn = self.env.cr.fetchone()[0] or 0.0
            if fnn != 0:
                vfn = ((fn - fnn) / fnn) * 100
            else:     
                vfn = 0
            line.append((0,0,{'name':'- Distributions de dividendes opérées durant l’exercice', 'annee_n':fn, 'annee_n1':fnn, 'variation':vfn}))
            
            atf = cafg - fn
            atfn = cafgn - fnn
            if atfn != 0:
                vatf = ((atf - atfn) / atfn) * 100
            else:     
                vatf = 0
            line.append((0,0,{'name':'= AUTOFINANCEMENT', 'annee_n':atf, 'annee_n1':atfn, 'variation':vatf}))
            
            line.append((0,0,{'name':'ANALYSE DE LA RENTABILITE'}))
            
            cp = bilan.get('cp_net') or 0.0
            cpn = bilan.get('cpn_net') or 0.0
            da = bilan.get('da_net') or 0.0
            dan = bilan.get('dan_net') or 0.0 
            db = bilan.get('db_net') or 0.0
            dbn = bilan.get('dbn_net') or 0.0
            re = (xe * 70) / (cp + da + db)
            re_n = (xen * 70) / (cpn + dan + dbn)
            if re_n != 0:
                vre = ((re - re_n) / re_n) * 100
            else:     
                vre = 0
            line.append((0,0,{'name':'Rentabilité économique = Résultat d’exploitation (a) / Capitaux propres + dettes financières (%)', 'annee_n':re, 'annee_n1':re_n, 'variation':vre}))
            
            cp = bilan.get('cp_net') or 0.0
            cpn = bilan.get('cpn_net') or 0.0
            rf = xi / cp
            rfn = xin / cpn
            if rfn != 0:
                vrf = ((rf - rfn) / rfn) * 100 
            else:     
                vrf = 0
            line.append((0,0,{'name':'Rentabilité financière = Résultat net / Capitaux propres (%)', 'annee_n':rf, 'annee_n1':rfn, 'variation':vrf}))
            
            line.append((0,0,{'name':'ANALYSE DE LA Structure FINANCIERE'}))
            
            if cpn != 0:
                vcp = ((cp - cpn) / cpn) * 100
            else:     
                vcp = 0
            line.append((0,0,{'name':'+ Capitaux propres et ressources assimilées', 'annee_n':cp, 'annee_n1':cpn, 'variation':vcp}))
            dd = bilan.get('dd_net') or 0.0
            ddn = bilan.get('ddn_net') or 0.0
            if ddn != 0:
                vdd = ((dd - ddn) / ddn) * 100 
            else:     
                vdd = 0
            line.append((0,0,{'name':'+ Dettes financières* et autres ressources assimilées (b)', 'annee_n':dd, 'annee_n1':ddn, 'variation':vdd}))
            
            df = bilan.get('df_net') or 0.0
            dfn = bilan.get('dfn_net') or 0.0
            if dfn != 0:
                vdf = ((df - dfn) / dfn) * 100 
            else:     
                vdf = 0
            line.append((0,0,{'name':'= Ressources stables', 'annee_n':df, 'annee_n1':dfn, 'variation':vdf}))
            
            az = bilan.get('az_net') or 0.0
            azn = bilan.get('azn_net') or 0.0
            if azn != 0:
                vaz = ((az - azn) / azn) * 100
            else:     
                vaz = 0
            line.append((0,0,{'name':'- Actif immobilisé', 'annee_n':az, 'annee_n1':azn, 'variation':vaz}))
            
            fdr = df - az
            fdrn = dfn - azn 
            if fdrn != 0:
                vfdr = ((fdr - fdrn) / fdrn) * 100
            else:     
                vfdr = 0
            line.append((0,0,{'name':'= FONDS DE ROULEMENT (1)', 'annee_n':fdr, 'annee_n1':fdrn, 'variation':vfdr}))
            
            bk = bilan.get('bk_net') or 0.0
            bkn = bilan.get('bkn_net') or 0.0
            
            ba = bilan.get('ba_net') or 0.0 
            ban = bilan.get('ban_net') or 0.0
            
            bu = bilan.get('bu_net') or 0.0
            bun = bilan.get('bun_net') or 0.0
            
            ace = bk - ba + bu
            acen = bkn - ban - bun           
            if acen != 0:
                vace = ((ace - acen) / acen) * 100
            else:     
                vace = 0
            line.append((0,0,{'name':'+ Actif circulant d’exploitation (b)', 'annee_n':ace, 'annee_n1':acen, 'variation':vace}))
            
            dp = bilan.get('dp_net') or 0.0
            dpn = bilan.get('dpn_net') or 0.0
            
            dh = bilan.get('dh_net') or 0.0
            dhn = bilan.get('dhn_net') or 0.0
            
            dv = bilan.get('dv_net') or 0.0
            dvn = bilan.get('dvn_net') or 0.0
            
            pce = dp - dh + dv
            pcen = dpn - dhn + dvn
            if pcen != 0:
                vpce = ((pce - pcen) / pcen) * 100 
            else:     
                vpce = 0
            line.append((0,0,{'name':'- Passif circulant d’exploitation (b)', 'annee_n':pce, 'annee_n1':pcen, 'variation':vpce}))
            
            bfe = fdr + ace - pce
            bfen = fdrn + acen - pcen
            if bfen != 0:
                vbfe = ((bfe - bfen) / bfen) * 100 
            else:     
                vbfe = 0
            line.append((0,0,{'name':'= BESOIN DE FINANCEMENT D\'EXPLOITATION (2)', 'annee_n':bfe, 'annee_n1':bfen, 'variation':vbfe}))
            
            if ban != 0:
                vba = ((ba - ban) / ban) * 100
            else:     
                vba = 0
            line.append((0,0,{'name':'+ Actif circulant HAO', 'annee_n':ba, 'annee_n1':ban, 'variation':vba}))
            
            if dhn != 0:
                vdh = ((dh - dhn) / dhn) * 100
            else:     
                vdh = 0
            line.append((0,0,{'name':'- Passif circulant HAO', 'annee_n':dh, 'annee_n1':dhn, 'variation':vdh}))
            
            bfh = bfe + ba - dh 
            bfhn = bfen + ban - dhn
            if bfhn != 0:
                vbfh = ((bfh - bfhn) / bfhn) * 100
            else:     
                vbfh = 0
            line.append((0,0,{'name':'= BESOIN DE FINANCEMENT HAO (3)', 'annee_n':bfh, 'annee_n1':bfhn, 'variation':vbfh}))
            
            bfg = bfe + bfh
            bfgn = bfen + bfhn
            if bfgn != 0:
                vbfg = ((bfg - bfgn) / bfgn) * 100
            else:     
                vbfg = 0
            line.append((0,0,{'name':'BESOIN DE FINANCEMENT GLOBAL (4) = (2) + (3)', 'annee_n':bfg, 'annee_n1':bfgn, 'variation':vbfg}))
            
            trn = fdr - bfg
            trnn = fdrn - bfgn
            if trnn != 0:
                vtrn = ((trn - trnn) / trnn) * 100
            else:     
                vtrn = 0
            line.append((0,0,{'name':'TRESORERIE NETTE(5) = (1) - (4)', 'annee_n':trn, 'annee_n1':trnn, 'variation':vtrn}))
            
            line.append((0,0,{'name':'ANALYSE DE LA VARIATION DE LA TRESORERIE'}))           
            
            zb = tft.get('zb_net') or 0.0
            zbn = tft.get('zbn_net') or 0.0
            if zbn != 0:
                vzb = ((zb - zbn) / zbn) * 100
            else:     
                vzb = 0
            line.append((0,0,{'name':'Flux de trésorerie des activités opérationnelles', 'annee_n':zb, 'annee_n1':zbn, 'variation':vzb}))
            
            zc = tft.get('zc_net') or 0.0
            zcn = tft.get('zcn_net') or 0.0
            if zcn != 0:
                vzc = ((zc - zcn) / zcn) * 100 
            else:     
                vzc = 0
            line.append((0,0,{'name':'- Flux de trésorerie des activités d’investissement', 'annee_n':zc, 'annee_n1':zcn, 'variation':vzc}))
            
            zf = tft.get('zf_net') or 0.0
            zfn = tft.get('zfn_net') or 0.0
            if zfn != 0:
                vzf = ((zf - zfn) / zfn) * 100
            else:     
                vzf = 0
            line.append((0,0,{'name':'+ Flux de trésorerie des actitivtés de financement', 'annee_n':zf, 'annee_n1':zfn, 'variation':vzf}))
            
            vtnp = zb - zc + zf
            vtnpn = zbn - zcn + zfn
            if vtnpn != 0:
                vvtnp = ((vtnp - vtnpn) / vtnpn) * 100 
            else:     
                vvtnp = 0
            line.append((0,0,{'name':'= VARIATION DE LA TRESORERIE NETTE DE LA PERIODE', 'annee_n':vtnp, 'annee_n1':vtnpn, 'variation':vvtnp}))
            
            line.append((0,0,{'name':'ANALYSE DE LA VARIATION de L’ENDETTEMENT FINANCIER NET'}))
            
            dt = bilan.get('dt_net') or 0.0
            dtn = bilan.get('dtn_net') or 0.0
            
            efb = da + db + dt
            efbn = dan + dbn + dtn
            if efbn != 0:
                vefb = ((efb - efbn) / efbn) * 100
            else:
                vefb = 0
            line.append((0,0,{'name':'Endettement financier brut (Dettes financières + Trésorerie passif)', 'annee_n':efb, 'annee_n1':efbn, 'variation':vefb}))
            
            bt = bilan.get('bt_net') or 0.0
            btn = tft.get('btn_net') or 0.0
            if btn != 0:
                vbt = ((bt - btn) / btn) * 100
            else:     
                vbt = 0
            line.append((0,0,{'name':'- Trésoreie actif', 'annee_n':bt, 'annee_n1':btn, 'variation':vbt}))
            
            efn = efb - bt
            efnn = efbn - btn
            if btn != 0:
                vefn = ((efn - efnn) / efnn) * 100
            else:     
                vefn = 0
            line.append((0,0,{'name':'= ENDETTEMENT FINANCIER NET', 'annee_n':efn, 'annee_n1':efnn, 'variation':vefn
                             }))
            self.note34_lines = line

    @api.onchange("note37")
    def onchange_note37(self):
        line = []
        if self.note37 is True:
            line.append((0,0,{'name':'1 : RESULTAT NET COMPTABLE DE LEXERCICE'}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':'2 : A REINTEGRER'}))
            line.append((0,0,{'name':'Impôt sur le résultat'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'3 : A DEDUIRE'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'4 : RESULTAT IMPOSABLE AVANT DEDUCTION DES DEFICITES (4=1+2-3)'}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'6 : AMORTISSEMENTS REGULIEREMENT DIFFERES'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'7 : AMORTISSEMENTS DE L’EXERCICE A DIFFERERE'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':'8 : RESULTAT FISCAL DE L’EXERCICE (8=4-5-6+7)'}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':'9 : IMPOTS SUR LE RESULTAT AU TAUX DE ....'}))
            self.note37_lines = line




class OptesisNote1Tab1(models.Model):
    _name = "optesis.note1.tab1"

    name = fields.Char("Libelle")
    montant = fields.Float("Montant brut")
    note = fields.Char("Note")
    hypo = fields.Float("Hypotheques")
    nant = fields.Float("Nantissements")
    gage = fields.Float("Gages / autres")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote1Tab2(models.Model):
    _name = "optesis.note1.tab2"

    name = fields.Char("Libelle")
    eng_dons = fields.Float("Engagements Dons")
    eng_recu = fields.Float("Engagements Dons")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote3a(models.Model):
    _name = "optesis.note3a"

    name = fields.Char("RUBRIQUES - SITUATIONS")
    montant_ouverture = fields.Float("MONTANT BRUT A L’OUVERTURE DE L’EXERCICE")
    acqisition = fields.Float("Acquisition Apport Creation")
    virement = fields.Float("Virement poste a poste")
    reevaluation = fields.Float("Suite a une reevaluation pratiquee au cours de l’exercice")
    cession = fields.Float("Cession / Hors service")
    virement2 = fields.Float("Virements de poste a poste")
    montant_cloture = fields.Float("MONTANT BRUT A LA CLOTURE DE L’EXERCICE")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote3b(models.Model):
    _name = "optesis.note3b"

    name = fields.Char("SITUATION ET MOUVEMENTS RUBRIQUES")
    nature_contrat = fields.Char("NATURE DU CONTRAT (I;M;A)")
    montant_ouverture = fields.Float("MONTANT BRUT A L’OUVERTURE DE L’EXERCICE")
    acqisition = fields.Float("Acquisition Apport creance")
    virement = fields.Float("Virement de poste a poste")
    reevaluation = fields.Float("Suite a une reevaluation pratiquee au cours de l’exercice")
    cession = fields.Float("Cession Scission Hors service")
    virement2 = fields.Float("Virement de poste a poste")
    montant_cloture = fields.Float("MONTANT BRUT A LA CLOTURE DE L’EXERCICE")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote3c(models.Model):
    _name = "optesis.note3c"

    name = fields.Char("SITUATION ET MOUVEMENTS RUBRIQUES")
    amortissement_ouverture = fields.Float("AMORTISSEMENTS CUMULES A L’OUVERTURE DE L’EXERCICE")
    augmentation = fields.Float("AUGMENTATION: DOTATION DE L’EXERCICE")
    diminutions = fields.Float("DIMUNITIONS: Amortissements relatifs aux elements de l’actif")
    amortissement_cloture = fields.Float("CUMUL DES AMORTISSEMENTS A LA CLOTURE DE L’EXERCICE")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote3d(models.Model):
    _name = "optesis.note3d"

    name = fields.Char("Libelle")
    montant = fields.Float("MONTANT BRUT")
    amortissement = fields.Float("AMORTISSEMENTS PRATIQUES")
    valeur_compta = fields.Float("VALEUR COMPTABLE NETTE")
    cession = fields.Float("PRIX DE CESSION")
    value = fields.Float("PLUS-VALUE OU MOINS-VALUE")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote3e(models.Model):
    _name = "optesis.note3e"

    name = fields.Char("Elements reevalues par postes du bilan")
    montant = fields.Float("Montant couts historiques")
    ecart_provision = fields.Float("Ecarts et provisions speciales de reevaluation")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote4Tab1(models.Model):
    _name = "optesis.note4.tab1"

    name = fields.Char("Libelle")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation = fields.Float("Variation en %")
    creance1 = fields.Float("Creances a un an au plus")
    creance2 = fields.Float("Creances a plus d’un an et a deux ans au plus")
    creance3 = fields.Float("Creances a plus de deux ans")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote4Tab2(models.Model):
    _name = "optesis.note4.tab2"

    name = fields.Char("Denomination sociale")
    localisation = fields.Char("Localisation (Ville / Pays)")
    valeur_acquisition = fields.Float("Valeur d’acquisition")
    detenu = fields.Float("% Detenu")
    montant = fields.Float("Montant des capitaux propres filiale")
    resultat = fields.Float("Resultat dernier exrcice filiale")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote5Tab1(models.Model):
    _name = "optesis.note5.tab1"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote5Tab2(models.Model):
    _name = "optesis.note5.tab2"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote6(models.Model):
    _name = "optesis.note6"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote7(models.Model):
    _name = "optesis.note7"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation = fields.Float("Variation en %")
    creance1 = fields.Float("Creances a un an au plus")
    creance2 = fields.Float("Creances a plus d’un an et a deux ans au plus")
    creance3 = fields.Float("Creances a plus de deux ans")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote8(models.Model):
    _name = "optesis.note8"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation = fields.Float("Variation en %")
    creance1 = fields.Float("Creances a un an au plus")
    creance2 = fields.Float("Creances a plus d’un an et a deux ans au plus")
    creance3 = fields.Float("Creances a plus de deux ans")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote8aTab1(models.Model):
    _name = "optesis.note8a.tab1"

    name = fields.Char("Libelles")
    frais = fields.Float("Frais d’etablissement")
    charge =fields.Float("Charge à répartir sur plusieurs exercices")
    prime = fields.Float("Prime de remboursement des oblgations")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote8aTab2(models.Model):
    _name = "optesis.note8a.tab2"

    name = fields.Char("Libelles")
    compte1 = fields.Char("Comptes")
    montant1 = fields.Float("Montants")
    compte2 = fields.Char("Comptes")
    montant2 = fields.Float("Montants")
    compte3 = fields.Char("Comptes")
    montant3 = fields.Float("Montants")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote9(models.Model):
    _name = "optesis.note9"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote10(models.Model):
    _name = "optesis.note10"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote11(models.Model):
    _name = "optesis.note11"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote12Tab1(models.Model):
    _name = "optesis.note12.tab1"

    name = fields.Char("Libelles")
    Devises = fields.Char("Devises")
    Montant_en_D = fields.Float("Montant en devises")
    Cours_U_A_A = fields.Float("Cours UML Année acquisition")
    Cours_U = fields.Float("Cours UML 31/12")
    Variation = fields.Float("Variation en valeur absolue")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote12Tab2(models.Model):
    _name = "optesis.note12.tab2"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote13(models.Model):
    _name = "optesis.note13"

    name = fields.Char("Nom et Prénoms")
    Nationalite = fields.Char("Nationalité")
    Nature_des_actions = fields.Char("Nature des actions ou parts (ordinaires ou préférences)")
    Nombre = fields.Float("Nombre")
    Montant_total = fields.Float("Montant total")
    Cession = fields.Float("Cession ou remboursement en cours d’exercice")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote14(models.Model):
    _name = "optesis.note14"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation = fields.Float("Varitaion en valeur absolue")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote15A(models.Model):
    _name = "optesis.note15a"

    name = fields.Char("Libelles")
    note = fields.Char("NOTE")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_va = fields.Float("Varitaion en valeur absolue")
    variation_p = fields.Float("Variation en %")
    regim_fiscal = fields.Char("Régime fiscal")
    echeance = fields.Char("Echéance")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote15B(models.Model):
    _name = "optesis.note15b"

    name = fields.Char("Libelles")
    note = fields.Char("NOTE")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_va = fields.Float("Varitaion en valeur absolue")
    variation_p = fields.Float("Variation en %")
    echeance = fields.Float("Echéance")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote16A(models.Model):
    _name = "optesis.note16a"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_va = fields.Float("Varitaion en valeur absolue")
    variation_p = fields.Float("Variation en %")
    Dettes_1aP = fields.Float("Dettes à un an au plus")
    Dettes_2aP = fields.Float("Dettes à plus d’un an et à deux ans au plus")
    Dettes_P2a = fields.Float("Dettes à plus de deux ans")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote16BTab1(models.Model):
    _name = "optesis.note16b.tab1"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote16BTab2(models.Model):
    _name = "optesis.note16b.tab2"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote16BTab3(models.Model):
    _name = "optesis.note16b.tab3"

    name = fields.Char("Libelles")
    augmentationN = fields.Float("augmentation N")
    diminutionsN = fields.Float("diminutions N")
    augmentationN1 = fields.Float("augmentation N-1")
    diminutionsN1 = fields.Float("diminutions N-1")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote16BBISTab1(models.Model):
    _name = "optesis.note16bbis.tab1"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote16BBISTab2(models.Model):
    _name = "optesis.note16bbis.tab2"

    name = fields.Char("Libelles")
    RendementN = fields.Float("Rendement attendu N")
    juste_VAN = fields.Float("juste valeur des actifs N")
    RendementN1 = fields.Float("Rendement attendu N-1")
    juste_VAN1 = fields.Float("juste valeur des actifs N-1")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote16C(models.Model):
    _name = "optesis.note16c"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote17(models.Model):
    _name = "optesis.note17"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_p = fields.Char("Variation en %")
    Dettes_1aP = fields.Float("Dettes à un an au plus")
    Dettes_2aP = fields.Float("Dettes à plus d’un an et à deux ans au plus")
    Dettes_P2a = fields.Float("Dettes à plus de deux ans")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote18(models.Model):
    _name = "optesis.note18"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_va = fields.Float("Varitaion en valeur absolue")
    variation_p = fields.Char("Variation en %")
    Dettes_1aP = fields.Float("Dettes à un an au plus")
    Dettes_2aP = fields.Float("Dettes à plus d’un an et à deux ans au plus")
    Dettes_P2a = fields.Float("Dettes à plus de deux ans")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote19(models.Model):
    _name = "optesis.note19"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_va = fields.Float("Varitaion en valeur absolue")
    variation_p = fields.Float("Variation en %")
    Dettes_1aP = fields.Float("Dettes à un an au plus")
    Dettes_2aP = fields.Float("Dettes à plus d’un an et à deux ans au plus")
    Dettes_P2a = fields.Float("Dettes à plus de deux ans")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote20(models.Model):
    _name = "optesis.note20"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_p = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote21(models.Model):
    _name = "optesis.note21"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_p = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote22(models.Model):
    _name = "optesis.note22"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_p = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote23(models.Model):
    _name = "optesis.note23"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_p = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote24(models.Model):
    _name = "optesis.note24"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_p = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote25(models.Model):
    _name = "optesis.note25"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_p = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote26(models.Model):
    _name = "optesis.note26"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_p = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote27A(models.Model):
    _name = "optesis.note27a"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_p = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote28(models.Model):
    _name = "optesis.note28"

    name = fields.Char("SITUATION ET MOUVEMENTS NATURE")
    provision_ouverture = fields.Float("Provisions à l’ouverture de l’exercice")
    exploitation_augmentation = fields.Float("Augmentation: dotations Exploitation")
    financiers_augmentation = fields.Float("Augmentation: dotations Financiers")
    hors_activite_augmentation = fields.Float("Augmentation: dotations Hors activités ordinaire")
    exploitation_diminution = fields.Float("Diminution: reprises Exploitation")
    financiers_diminution = fields.Float("Diminution: reprises Financiers")
    hors_activite_diminution = fields.Float("Diminution: reprises Hors activités ordinaire")
    provision_cloturre = fields.Float("Provisions à la clôture de l’exercice")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote29(models.Model):
    _name = "optesis.note29"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote30(models.Model):
    _name = "optesis.note30"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote31(models.Model):
    _name = "optesis.note31"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    annee_n2 = fields.Float("Annee N-2")
    annee_n3 = fields.Float("Annee N-3")
    annee_n4 = fields.Float("Annee N-4")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote32(models.Model):
    _name = "optesis.note32"

    name = fields.Char("Désignation du produit")
    unite = fields.Char("Unite de quantite choisie")
    quantite_pays = fields.Float("PRODUCTION VENDUE DANS LE PAYS: Quantite")
    valeur_pays= fields.Float("PRODUCTION VENDUE DANS LE PAYS: Valeur")
    quantite_ohada = fields.Float("PRODUCTION VENDUE DANS LES AUTRES PAYS DE L’OHADA: Quantite")
    valeur_ohada= fields.Float("PRODUCTION VENDUE DANS LES AUTRES PAYS DE L’OHADA: Valeur")
    quantite_hors_ohada = fields.Float("PRODUCTION VENDUE HORS OHADA: Quantite")
    valeur_hors_ohada = fields.Float("PRODUCTION VENDUE HORS OHADA: Valeur")
    quantite_immo = fields.Float("PRODUCTION IMMOBILISEEE: Quantite")
    valeur_immo = fields.Float("PRODUCTION IMMOBILISEEE: Valeur")
    quantite_ouverture = fields.Float("STOCK OUVERTURE DE L’EXERCICE: Quantite")
    valeur_ouvertute = fields.Float("STOCK OUVERTURE DE L’EXERCICE: Valeur")
    quantite_cloture = fields.Float("STOCK CLÔTURE DE L’EXERCICE: Quantite")
    valeur_cloture = fields.Float("STOCK CLÔTURE DE L’EXERCICE: Valeur")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote33(models.Model):
    _name = "optesis.note33"

    name = fields.Char("Désignation ")
    unite = fields.Char("Unite de quantite choisie")
    quantite_pays = fields.Float("Prdouit de l’Etat: Quantite")
    valeur_pays = fields.Float("Prdouit de l’Etat: Val")
    quantite_etat = fields.Float("Achetes dans l’Etat: Quantite")
    valeur_etat= fields.Float("Achetes dans l’Etat: Valeur")
    quantite_hors_etat = fields.Float("Achetes hors de l’Eta: Quantite")
    valeur_hors_etat = fields.Float("Achetes hors de l’Eta: Valeur")
    variation = fields.Float("Variation des stocks")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote34(models.Model):
    _name = "optesis.note34"

    name = fields.Char("Libelle")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote37(models.Model):
    _name = "optesis.note37"

    name = fields.Char("Libelles")
    montant = fields.Float("Montant")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

