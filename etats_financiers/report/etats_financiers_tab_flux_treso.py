# -*- coding: utf-8 -*-

import time
from odoo import api, models
from dateutil.parser import parse
from odoo.exceptions import UserError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class ReportTabFluxTreso(models.AbstractModel):
    _name = 'report.etats_financiers.report_tab_flux_treso'

    @api.model
    def _get_report_values(self, docids, data=None):
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_id'))
        
        debut_n = docs.debut - relativedelta(years=+1)
        fin_n = docs.fin - relativedelta(years=+1)
        
        debut_n2 = docs.debut - relativedelta(years=+2)
        fin_n2 = docs.fin - relativedelta(years=+2)
        
        bilan = self.env['report.etats_financiers.report_bilan']._get_report_values(docids)
        compte = self.env['report.etats_financiers.report_compte_resultat']._get_report_values(docids)
        
        
        #CALCUL ZA
        
        # BQ
                
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '50%' \
                            group by sub.code) as query")
        bqn_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '590%' \
                            group by sub.code) as query")
        bqn_ad = self.env.cr.fetchone()[0] or 0.0
        
        bqn_net = bqn_brut - bqn_ad
        
        # BR
                
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '51%' \
                            group by sub.code) as query")
        brn_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '591%' \
                            group by sub.code) as query")
        brn_ad = self.env.cr.fetchone()[0] or 0.0
        
        brn_net = brn_brut - brn_ad
        
        # BS
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '52%' or sub.code like '53%' or sub.code like '54%' or sub.code like '55%' or sub.code like '57%' or sub.code like '581%' or sub.code like '582%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        bsn_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '592%' or sub.code like '593%' or sub.code like '594%' \
                            group by sub.code) as query")
        bsn_ad = self.env.cr.fetchone()[0] or 0.0

        bsn_net = bsn_brut - bsn_ad
        
        # ZAV1
        
        zav1 = bilan.get('bqn_net') + bilan.get('brn_net') + bilan.get('bsn_net')
        zav1n = bqn_net + brn_net + bsn_net
        
        # ZAV2
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4726%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        zav2 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4726%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        zav2n = self.env.cr.fetchone()[0] or 0.0
        
        # DQ
                
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '564%' or sub.code like '565%' \
                            group by sub.code) as query")
        dqn_net = self.env.cr.fetchone()[0] or 0.0
        
        # DR
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '52%' or sub.code like '53%' or sub.code like '561%' or sub.code like '566%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        drn_net = self.env.cr.fetchone()[0] or 0.0
        
        # ZAV3
        
        zav3 = bilan.get('dqn_net') + bilan.get('drn_net')
        zav3n = dqn_net + drn_net
        
        # ZA
        
        za = zav1 - zav2 - zav3
        zan = zav1n - zav2n - zav3n
        
        # CALCUL FA
        
        fa = compte.get('xi_net') + compte.get('rl_net') + compte.get('rn_net') - compte.get('tj_net') - compte.get('tl_net')
        fan = compte.get('xin_net') + compte.get('rln_net') + compte.get('rnn_net') - compte.get('tjn_net') - compte.get('tln_net')
        
        # CALCUL FB
        
        # BA
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <='"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '485%' or sub.code like '488%' \
                            group by sub.code) as query")
        ban_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <='"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '498%' \
                            group by sub.code) as query")
        ban_ad = self.env.cr.fetchone()[0] or 0.0

        ban_net = ban_brut - ban_ad
        
        # FBV1
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '485%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fbv1 = self.env.cr.fetchone()[0] or 0.0 
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '485%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fbv1n = self.env.cr.fetchone()[0] or 0.0
        
        # FBV2
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '485%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fbv2 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <='"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '485%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fbv2n = self.env.cr.fetchone()[0] or 0.0
        
        # FBV3
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '47818%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fbv3 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '47818%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fbv3n = self.env.cr.fetchone()[0] or 0.0
        
        # FBV4
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '47918%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        fbv4 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '47918%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        fbv4n = self.env.cr.fetchone()[0] or 0.0
        
        # FB
        
        fb = bilan.get('ba_net') - bilan.get('ban_net') - fbv1 + fbv2 + fbv3 - fbv4
        fbn = bilan.get('ban_net') - ban_net - fbv1 + fbv2 + fbv3 - fbv4
        
        # CALCUL FC
        
        # BB
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <='"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '31%' or sub.code like '32%' or sub.code like '33%' or sub.code like '34%' or sub.code like '35%' or sub.code like '36%' or sub.code like '37%' or sub.code like '38%' \
                            group by sub.code) as query")
        bbn_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <='"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '39%' \
                            group by sub.code) as query")
        bbn_ad = self.env.cr.fetchone()[0] or 0.0

        bbn_net = bbn_brut - bbn_ad
        
        # FC
        
        fc = bilan.get('bb_net') - bilan.get('bbn_net')
        fcn = bilan.get('bbn_net') - bbn_net
        
        # CALCUL FD
        
        # BH
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '409%' \
                            group by sub.code) as query")
        bhn_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '490%' \
                            group by sub.code) as query")
        bhn_ad = self.env.cr.fetchone()[0] or 0.0

        bhn_net = bhn_brut - bhn_ad
        
        # BI
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '41%' or sub.code like '419%' \
                            group by sub.code) as query")
        bin_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '491%' \
                            group by sub.code) as query")
        bin_ad = self.env.cr.fetchone()[0] or 0.0

        bin_net = bin_brut - bin_ad
        
        # BJ
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '185%' or sub.code like '42%' or sub.code like '43%' or sub.code like '44%' or sub.code like '45%' or sub.code like '46%' or sub.code like '47%' and sub.code not like '478%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        bjn_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '492%' or sub.code like '493%' or sub.code like '494%' or sub.code like '495%' or sub.code like '496%' or sub.code like '497%' \
                            group by sub.code) as query")
        bjn_ad = self.env.cr.fetchone()[0] or 0.0

        bjn_net = bjn_brut - bjn_ad
        
        # FDV1
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '414%' or sub.code like '4494%' or sub.code like '458%' or sub.code like '461%' or sub.code like '467%' or sub.code like '4752%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fdv1 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '414%' or sub.code like '4494%' or sub.code like '458%' or sub.code like '461%' or sub.code like '467%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fdv1n = self.env.cr.fetchone()[0] or 0.0
        
        #FDV2
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '414%' or sub.code like '4494%' or sub.code like '458%' or sub.code like '461%' or sub.code like '467%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fdv2 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '414%' or sub.code like '4494%' or sub.code like '458%' or sub.code like '461%' or sub.code like '467%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fdv2n = self.env.cr.fetchone()[0] or 0.0       
        
        # FDV3
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '47811%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fdv3 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '47811%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fdv3n = self.env.cr.fetchone()[0] or 0.0
        
        # FDV4
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '47911%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        fdv4 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '47911%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        fdv4n = self.env.cr.fetchone()[0] or 0.0
        
        
        # FDV5
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '2714%'\
                            group by sub.code) as query")
        fdv5 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '2714%'\
                            group by sub.code) as query")
        fdv5n = self.env.cr.fetchone()[0] or 0.0
        
        
        # FD
        
        fd = bilan.get('bh_net') + bilan.get('bi_net') + bilan.get('bj_net') - bilan.get('bhn_net') - bilan.get('bin_net') - bilan.get('bjn_net') - fdv1 + fdv2 + fdv3 - fdv4 + fdv5
        fdn = bilan.get('bhn_net') + bilan.get('bin_net') + bilan.get('bjn_net') - bhn_net - bin_net - bjn_net - fdv1n + fdv2n + fdv3n - fdv4n + fdv5n
        
        # CALCUL FE
        
        # DH

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '481%' or sub.code like '482%' or sub.code like '484%' or sub.code like '4998%' \
                            group by sub.code) as query")
        dhn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul DI

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '419%' \
                            group by sub.code) as query")
        din_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul DJ

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '40%' and sub.code not like '409%' \
                            group by sub.code) as query")
        djn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul DK

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '42%' or sub.code like '43%' or sub.code like '44%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        dkn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul DM

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '185%' or sub.code like '45%' or sub.code like '46%' or sub.code like '47%' and sub.code not like '479%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        dmn_net = self.env.cr.fetchone()[0] or 0.0

        # DN

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '499%' or sub.code like '599%' and sub.code not like '4998%' \
                            group by sub.code) as query")
        dnn_net = self.env.cr.fetchone()[0] or 0.0

        # DP
        
        dpn_net = dhn_net + din_net + djn_net + dkn_net + dmn_net + dnn_net
        
        # FEV1
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '404%' or sub.code like '461%' or sub.code like '465%' or sub.code like '4726%' or sub.code like '481%' or sub.code like '482%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        fev1 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '404%' or sub.code like '461%' or sub.code like '465%' or sub.code like '4726%' or sub.code like '481%' or sub.code like '482%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        fev1n = self.env.cr.fetchone()[0] or 0.0
        
        # FEV2
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '404%' or sub.code like '461%' or sub.code like '465%' or sub.code like '4726%' or sub.code like '481%' or sub.code like '482%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        fev2 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '404%' or sub.code like '461%' or sub.code like '465%' or sub.code like '4726%' or sub.code like '481%' or sub.code like '482%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        fev2n = self.env.cr.fetchone()[0] or 0.0
        
        # FEV3
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4793%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        fev3 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4793%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        fev3n = self.env.cr.fetchone()[0] or 0.0
        
        # FEV4
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4783%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fev4 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4783%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fev4n = self.env.cr.fetchone()[0] or 0.0
        
        # FEV5
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4752%'\
                            group by sub.code) as query")
        fev5 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4752%'\
                            group by sub.code) as query")
        fev5n = self.env.cr.fetchone()[0] or 0.0
        
        # FEV6
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4752%'\
                            group by sub.code) as query")
        fev6 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4752%'\
                            group by sub.code) as query")
        fev6n = self.env.cr.fetchone()[0] or 0.0
        
        # FE 
        
        fe = bilan.get('dp_net') - bilan.get('dpn_net') - fev1 + fev2 + fev3 - fev4 + fev5 - fev6
        fen = bilan.get('dpn_net') - dpn_net - fev1n + fev2n + fev3n - fev4n + fev5n - fev6n
        
        # CALCUL VAR
        
        var = -fb - fc - fd + fe
        varn = -fbn - fcn - fdn + fen
        
        # CALCUL ZB
        
        zb = fa - fb - fc - fd + fe
        zbn = fan - fbn - fcn - fdn + fen
        
        # CALCUL FF
        
        # AE

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '2181%' or sub.code like '211%' or sub.code like '2191%' \
                            group by sub.code) as query")
        aen_brut = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '2181%' or sub.code like '211%' or sub.code like '2191%' \
                            group by sub.code) as query")
        aen2_brut = self.env.cr.fetchone()[0] or 0.0

        # AF
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '212%' or sub.code like '213%' or sub.code like '214%' or sub.code like '2193%' \
                            group by sub.code) as query")
        afn_brut = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '212%' or sub.code like '213%' or sub.code like '214%' or sub.code like '2193%' \
                            group by sub.code) as query")
        afn2_brut = self.env.cr.fetchone()[0] or 0.0
        

        # AG
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '215%' or sub.code like '216%' \
                            group by sub.code) as query")
        agn_brut = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '215%' or sub.code like '216%' \
                            group by sub.code) as query")
        agn2_brut = self.env.cr.fetchone()[0] or 0.0

        # AH

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '217%' or sub.code like '218%' and sub.code not like '2181%' or sub.code like '2198%'\
                            group by sub.code) as query")
        ahn_brut = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '217%' or sub.code like '218%' and sub.code not like '2181%' or sub.code like '2198%'\
                            group by sub.code) as query")
        ahn2_brut = self.env.cr.fetchone()[0] or 0.0

        # AD
        
        adn_brut = aen_brut + afn_brut + agn_brut + ahn_brut
        adn2_brut = aen2_brut + afn2_brut + agn2_brut + ahn2_brut
        
        # FFV1
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '251%'\
                            group by sub.code) as query")
        ffv1 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '251%'\
                            group by sub.code) as query")
        ffv1n = self.env.cr.fetchone()[0] or 0.0
        
        # FFV2
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '251%'\
                            group by sub.code) as query")
        ffv2 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '251%'\
                            group by sub.code) as query")
        ffv2n = self.env.cr.fetchone()[0] or 0.0
        
        # FFV3
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4041%' or sub.code like '4046%' or sub.code like '4811%' or sub.code like '48161%' or sub.code like '48171%' or sub.code like '48181%' or sub.code like '4821%' or sub.code like '6541%' or sub.code like '281%'\
                            group by sub.code) as query")
        ffv3 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4041%' or sub.code like '4046%' or sub.code like '4811%' or sub.code like '48161%' or sub.code like '48171%' or sub.code like '48181%' or sub.code like '4821%' or sub.code like '6541%' or sub.code like '281%'\
                            group by sub.code) as query")
        ffv3n = self.env.cr.fetchone()[0] or 0.0
        
        # FFV4
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4041%' or sub.code like '4046%' or sub.code like '4811%' or sub.code like '48161%' or sub.code like '48171%' or sub.code like '48181%' or sub.code like '4821%'\
                            group by sub.code) as query")
        ffv4 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4041%' or sub.code like '4046%' or sub.code like '4811%' or sub.code like '48161%' or sub.code like '48171%' or sub.code like '48181%' or sub.code like '4821%'\
                            group by sub.code) as query")
        ffv4n = self.env.cr.fetchone()[0] or 0.0
        
        
        # FFV5
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '6541%' or sub.code like '811%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        ffv5 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '6541%' or sub.code like '811%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        ffv5n = self.env.cr.fetchone()[0] or 0.0
        
        
        
        # FF
        
        ff = bilan.get('ad_brut') - adn_brut + ffv1n - ffv2n + ffv3n - ffv4n + ffv5
        ffn = adn_brut - adn2_brut + ffv1n - ffv2n + ffv3n - ffv4n + ffv5n
        
        # CALCUL FG
        
        # AJ

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '22%' \
                            group by sub.code) as query")
        ajn_brut = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '22%' \
                            group by sub.code) as query")
        ajn2_brut = self.env.cr.fetchone()[0] or 0.0

        # AK

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '231%' or sub.code like '232%' or sub.code like '233%' or sub.code like '237%' or sub.code like '2391%' \
                            group by sub.code) as query")
        akn_brut = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '231%' or sub.code like '232%' or sub.code like '233%' or sub.code like '237%' or sub.code like '2391%' \
                            group by sub.code) as query")
        akn2_brut = self.env.cr.fetchone()[0] or 0.0

        # AL

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '234%' or sub.code like '235%' or sub.code like '238%' or sub.code like '2392%' or sub.code like '2393%' \
                            group by sub.code) as query")
        aln_brut = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '234%' or sub.code like '235%' or sub.code like '238%' or sub.code like '2392%' or sub.code like '2393%' \
                            group by sub.code) as query")
        aln2_brut = self.env.cr.fetchone()[0] or 0.0

        # AM

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <='"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '24%' and sub.code not like  '245%' and sub.code not like '2495%' \
                            group by sub.code) as query")
        amn_brut = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <='"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '24%' and sub.code not like  '245%' and sub.code not like '2495%' \
                            group by sub.code) as query")
        amn2_brut = self.env.cr.fetchone()[0] or 0.0

        # AN

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <='"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '245%' or sub.code like '2495%' \
                            group by sub.code) as query")
        ann_brut = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <='"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '245%' or sub.code like '2495%' \
                            group by sub.code) as query")
        ann2_brut = self.env.cr.fetchone()[0] or 0.0

        # AP

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <='"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '251%' or sub.code like '252%' \
                            group by sub.code) as query")
        apn_brut = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <='"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '251%' or sub.code like '252%' \
                            group by sub.code) as query")
        apn2_brut = self.env.cr.fetchone()[0] or 0.0

        # AI

        ain_brut = ajn_brut + akn_brut + aln_brut + amn_brut + ann_brut
        ain2_brut = ajn2_brut + akn2_brut + aln2_brut + amn2_brut + ann2_brut
        
        # FGV1
        
        fgv1 = bilan.get('ai_brut') + bilan.get('ap_brut')
        fgv1n = ain_brut + apn_brut
        
        # FGV2
        
        fgv2 = ain_brut + apn_brut
        fgv2n = ain2_brut + apn2_brut       
        
        
        # FGV3
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '252%'\
                            group by sub.code) as query")
        fgv3 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '252%'\
                            group by sub.code) as query")
        fgv3n = self.env.cr.fetchone()[0] or 0.0
        
        # FGV4
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '252%'\
                            group by sub.code) as query")
        fgv4 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '252%'\
                            group by sub.code) as query")
        fgv4n = self.env.cr.fetchone()[0] or 0.0
        
        # FGV5
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4042%' or sub.code like '4047%' or sub.code like '4812%' or sub.code like '48162%' or sub.code like '48172%' or sub.code like '48182%' or sub.code like '4822%' or sub.code like '282%' or sub.code like '283%' or sub.code like '284%'\
                            group by sub.code) as query")
        fgv5 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4042%' or sub.code like '4047%' or sub.code like '4812%' or sub.code like '48162%' or sub.code like '48172%' or sub.code like '48182%' or sub.code like '4822%' or sub.code like '282%' or sub.code like '283%' or sub.code like '284%'\
                            group by sub.code) as query")
        fgv5n = self.env.cr.fetchone()[0] or 0.0
        
        # FGV6
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '17%' or sub.code like '19842%' or sub.code like '4042%' or sub.code like '4047%' or sub.code like '4812%' or sub.code like '48162%' or sub.code like '48172%' or sub.code like '48182%' or sub.code like '4822%'\
                            group by sub.code) as query")
        fgv6 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '17%' or sub.code like '19842%' or sub.code like '4042%' or sub.code like '4047%' or sub.code like '4812%' or sub.code like '48162%' or sub.code like '48172%' or sub.code like '48182%' or sub.code like '4822%'\
                            group by sub.code) as query")
        fgv6n = self.env.cr.fetchone()[0] or 0.0
        
        # FGV7
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '106%' or sub.code like '154%'\
                            group by sub.code) as query")
        fgv7 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '106%' or sub.code like '154%'\
                            group by sub.code) as query")
        fgv7n = self.env.cr.fetchone()[0] or 0.0
        
        # FGV8
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '6542%' or sub.code like '812%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fgv8 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '6542%' or sub.code like '812%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fgv8n = self.env.cr.fetchone()[0] or 0.0
        
        
        # FG
        
        fg = fgv1 - fgv2 - fgv3 + fgv4 + fgv5 - fgv6 - fgv7 + fgv8
        fgn = fgv1n - fgv2n - fgv3n + fgv4n + fgv5n - fgv6n - fgv7n + fgv8n
        
        
        # CALCUL FH
        
        # FHV1
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '26%' or sub.code like '27%' and sub.code not like '2714%' and sub.code not like '276%'\
                            group by sub.code) as query")
        fhv1 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '26%' or sub.code like '27%' and sub.code not like '2714%' and sub.code not like '276%'\
                            group by sub.code) as query")
        fhv1n = self.env.cr.fetchone()[0] or 0.0
        
        # FHV2
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4813%'\
                            group by sub.code) as query")
        fhv2 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4813%'\
                            group by sub.code) as query")
        fhv2n = self.env.cr.fetchone()[0] or 0.0
        
        # FHV3
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4813%'\
                            group by sub.code) as query")
        fhv3 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4813%'\
                            group by sub.code) as query")
        fhv3n = self.env.cr.fetchone()[0] or 0.0
        
        # FHV4
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '106%' or sub.code like '154%'\
                            group by sub.code) as query")
        fhv4 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '106%' or sub.code like '154%'\
                            group by sub.code) as query")
        fhv4n = self.env.cr.fetchone()[0] or 0.0
        
        # FHV5
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4782%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fhv5 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4782%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fhv5n = self.env.cr.fetchone()[0] or 0.0
        
        # FHV6
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4792%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        fhv6 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4792%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        fhv6n = self.env.cr.fetchone()[0] or 0.0
        
        # FH 
        
        fh = fhv1 + fhv2 - fhv3 - fhv4 + fhv5 - fhv6
        fhn = fhv1n + fhv2n - fhv3n - fhv4n + fhv5n - fhv6n
        
        # CALCUL FI
        
        # FIV1
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '754%' or sub.code like '821%' or sub.code like '822%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        fiv1 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '754%' or sub.code like '821%' or sub.code like '822%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        fiv1n = self.env.cr.fetchone()[0] or 0.0
        
        # FIV2
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '414%' or sub.code like '485%' and sub.code not like '4856%'\
                            group by sub.code) as query")
        fiv2 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '414%' or sub.code like '485%' and sub.code not like '4856%'\
                            group by sub.code) as query")
        fiv2n = self.env.cr.fetchone()[0] or 0.0
        
        # FIV3
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '414%' or sub.code like '485%' and sub.code not like '4856%'\
                            group by sub.code) as query")
        fiv3 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '414%' or sub.code like '485%' and sub.code not like '4856%'\
                            group by sub.code) as query")
        fiv3n = self.env.cr.fetchone()[0] or 0.0
        
        # FI
        
        fi = fiv1 - fiv2 + fiv3
        fin = fiv1n - fiv2n + fiv3n
        
        # CALCUL FJ
        
        # FJV1
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '826%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        fjv1 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '826%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        fjv1n = self.env.cr.fetchone()[0] or 0.0
        
        # FJV2
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '27%' or sub.code like '2766%'\
                            group by sub.code) as query")
        fjv2 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '27%' or sub.code like '2766%'\
                            group by sub.code) as query")
        fjv2n = self.env.cr.fetchone()[0] or 0.0
        
        # FJV3
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4856%'\
                            group by sub.code) as query")
        fjv3 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4856%'\
                            group by sub.code) as query")
        fjv3n = self.env.cr.fetchone()[0] or 0.0
        
        # FJV4
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4856%'\
                            group by sub.code) as query")
        fjv4 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4856%'\
                            group by sub.code) as query")
        fjv4n = self.env.cr.fetchone()[0] or 0.0
        
        # FJ
        
        fj = fjv1 + fjv2 - fjv3 + fjv4
        fjn = fjv1n + fjv2n - fjv3n + fjv4n
        
        # ZC
        
        zc = -ff - fg - fh + fi + fj
        zcn = -ffn - fgn - fhn + fin + fjn
        
        # CALCUL FK
        
        # FKV1
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '101%' or sub.code like '102%' or sub.code like '1051%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        fkv1 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '101%' or sub.code like '102%' or sub.code like '1051%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        fkv1n = self.env.cr.fetchone()[0] or 0.0
        
        
        # FKV2
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '101%' or sub.code like '102%' or sub.code like '1051%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        fkv2 = self.env.cr.fetchone()[0] or 0.0
        
        
        # FKV3
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '109%' or sub.code like '4613%' or sub.code like '467%' or sub.code like '4581%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fkv3 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '109%' or sub.code like '4613%' or sub.code like '467%' or sub.code like '4581%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fkv3n = self.env.cr.fetchone()[0] or 0.0
        
        # FKV4
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '11%' or sub.code like '12%' or sub.code like '131%'\
                            group by sub.code) as query")
        fkv4 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '11%' or sub.code like '12%' or sub.code like '131%'\
                            group by sub.code) as query")
        fkv4n = self.env.cr.fetchone()[0] or 0.0
        
        
        # FKV5
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '103%' or sub.code like '104%' or sub.code like '11%' or sub.code like '12%' or sub.code like '139%' or sub.code like '4619%' or sub.code like '465%'\
                            group by sub.code) as query")
        fkv5 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '103%' or sub.code like '104%' or sub.code like '11%' or sub.code like '12%' or sub.code like '139%' or sub.code like '4619%' or sub.code like '465%'\
                            group by sub.code) as query")
        fkv5n = self.env.cr.fetchone()[0] or 0.0
        
        # FK
        
        fk = fkv1 - fkv1n - fkv3 - fkv4 + fkv5
        fkn = fkv1n - fkv2 - fkv3n - fkv4n + fkv5n
        
        # CALCUL FL
        
        #FLV1
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '14%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        flv1 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '14%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        flv1n = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n2)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '14%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        flv1n2 = self.env.cr.fetchone()[0] or 0.0
        
        
        #FLV2
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '799%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        flv2 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '799%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        flv2n = self.env.cr.fetchone()[0] or 0.0
        
        
        #FLV3
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4494%' or sub.code like '4582%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        flv3 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4494%' or sub.code like '4582%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        flv3n = self.env.cr.fetchone()[0] or 0.0        
        
        #FL
        
        fl = flv1 - flv1n + flv2 - flv3
        fln = flv1n - flv1n2 + flv2n - flv3n
        
        # CALCUL FM
        
        #FMV1
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4619%'\
                            group by sub.code) as query")
        fmv1 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4619%'\
                            group by sub.code) as query")
        fmv1n = self.env.cr.fetchone()[0] or 0.0
        
        
        #FMV2
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '103%' or sub.code like '104%'\
                            group by sub.code) as query")
        fmv2 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '103%' or sub.code like '104%'\
                            group by sub.code) as query")
        fmv2n = self.env.cr.fetchone()[0] or 0.0
        
        #FM
        
        fm = fmv1 + fmv2
        fmn = fmv1n + fmv2
        
        # CALCUL FN
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '465%'\
                            group by sub.code) as query")
        fn = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '465%'\
                            group by sub.code) as query")
        fnn = self.env.cr.fetchone()[0] or 0.0   
        
        # CALCUL ZD
        
        zd = fk + fl - fm - fn
        zdn = fkn + fln -fmn - fnn
        
        
        # CALCUL FO
        
        #FOV1
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '161%' or sub.code like '162%'\
                            group by sub.code) as query")
        fov1 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '161%' or sub.code like '162%'\
                            group by sub.code) as query")
        fov1n = self.env.cr.fetchone()[0] or 0.0
        
        # FOV2
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4713%'\
                            group by sub.code) as query")
        fov2 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4713%'\
                            group by sub.code) as query")
        fov2n = self.env.cr.fetchone()[0] or 0.0
        
        # FOV3
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4784%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fov3 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4784%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fov3n = self.env.cr.fetchone()[0] or 0.0
        
        fo = fov1 - fov2 - fov3
        fon = fov1n - fov2n - fov3n
        
        # CALCUL FP
        
        #FPV1
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '163%' or sub.code like '164%' or sub.code like '165%' or sub.code like '167%' or sub.code like '168%' or sub.code like '181%' or sub.code like '182%'\
                            group by sub.code) as query")
        fpv1 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.credit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '163%' or sub.code like '164%' or sub.code like '165%' or sub.code like '167%' or sub.code like '168%' or sub.code like '181%' or sub.code like '182%'\
                            group by sub.code) as query")
        fpv1n = self.env.cr.fetchone()[0] or 0.0
        
        #FPV2
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4784%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fpv2 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4784%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fpv2n = self.env.cr.fetchone()[0] or 0.0
        
        #FP
        
        fp = fpv1 - fpv2
        fpn = fpv1n - fpv2n
        
        # CALCUL FQ
        
        #FQV1
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '16%' or sub.code like '17%' or sub.code like '181%' or sub.code like '182%'\
                            group by sub.code) as query")
        fqv1 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.debit) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '16%' or sub.code like '17%' or sub.code like '181%' or sub.code like '182%'\
                            group by sub.code) as query")
        fqv1n = self.env.cr.fetchone()[0] or 0.0
        
        #FQV2
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4794%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fqv2 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4794%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        fqv2n = self.env.cr.fetchone()[0] or 0.0
        
        #FQ
        
        fq = fqv1 - fqv2
        fqn = fqv1n - fqv2n
        
        # CALCUL ZE
        
        ze = fo + fp - fq
        zen = fon + fpn - fqn
        
        # CALCUL ZF
        
        zf = zd + ze
        zfn = zdn + zen
        
        # CALCUL ZG
        
        zg = zb + zc + zf
        zgn = zbn + zcn + zfn
        
        # CALCUL ZH
        
        #ZHV1
        
        zhv1 = bilan.get('bq_net') + bilan.get('br_net') + bilan.get('bs_net')
        zhv1n = bilan.get('bqn_net') + bilan.get('brn_net') + bilan.get('bsn_net')
        
        #ZHV2
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4726%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        zhv2 = self.env.cr.fetchone()[0] or 0.0
        
        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '4726%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        zhv2n = self.env.cr.fetchone()[0] or 0.0
        
        #ZHV3
        
        zhv3 = bilan.get('dq_net') + bilan.get('dr_net')
        zhv3n = bilan.get('dqn_net') + bilan.get('drn_net')
        
        #ZH
        
        zh = zhv1 - zhv2 - zhv3
        zhn = zhv1n - zhv2n - zhv3n
        
        
        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'docs': docs,
            'za':za,
            'zan':zan,
            'fa':fa,
            'fan':fan,
            'fb':fb,
            'fbn':fbn,
            'fc':fc,
            'fcn':fcn,
            'fd':fd,
            'fdn':fdn,
            'fe':fe,
            'fen':fen,
            'var':var,
            'varn':varn,
            'zb':zb,
            'zbn':zbn,
            'ff':ff,
            'ffn':ffn,
            'fg':fg,
            'fgn':fgn,
            'fh':fh,
            'fhn':fhn,
            'fi':fi,
            'fin':fin,
            'fj':fj,
            'fjn':fjn,
            'zc':zc,
            'zcn':zcn,
            'fk':fk,
            'fkn':fkn,
            'fl':fl,
            'fln':fln,
            'fm':fm,
            'fmn':fmn,
            'fn':fn,
            'fnn':fnn,
            'zd':zd,
            'zdn':zdn,
            'fo':fo,
            'fon':fon,
            'fp':fp,
            'fpn':fpn,
            'fq':fq,
            'fqn':fqn,
            'ze':ze,
            'zen':zen,
            'zf':zf,
            'zfn':zfn,
            'zg':zg,
            'zgn':zgn,
            'zh':zh,
            'zhn':zhn,
        }
        return docargs
