# -*- coding: utf-8 -*-

import time
from odoo import api, models
from dateutil.parser import parse
from odoo.exceptions import UserError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class ReportCompteResultat(models.AbstractModel):
    _name = 'report.etats_financiers.report_compte_resultat'

    @api.model
    def _get_report_values(self, docids, data=None):
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_id'))

        debut_n = docs.debut - relativedelta(years=+1)
        fin_n = docs.fin - relativedelta(years=+1)

        # Calcul TA

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '701%'")
        ta_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '701%'")
        tan_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul RA

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '601%'")
        ra_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '601%'")
        ran_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul RB

        self.env.cr.execute("select sum(sub.balance) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '6031%'")
        rb_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select sum(sub.balance) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '6031%'")
        rbn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul XA

        xa_net = ta_net - ra_net + rb_net
        xan_net = tan_net - ran_net + rbn_net

        # Calcul TB

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '702%' or sub.code like '703%' or sub.code like '704%'")
        tb_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '702%' or sub.code like '703%' or sub.code like '704%'")
        tbn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul TC

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '705%' or sub.code like '706%'")
        tc_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '705%' or sub.code like '706%'")
        tcn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul TD

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '707%'")
        td_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '707%'")
        tdn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul XB

        xb_net = ta_net + tb_net + tc_net + td_net
        xbn_net = tan_net + tbn_net + tcn_net + tdn_net

        # Calcul TE

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '73%'")
        te_net = self.env.cr.fetchone()[0] or 0.0
        if te_net > 0:
            te_net = -te_net

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '73%'")
        ten_net = self.env.cr.fetchone()[0] or 0.0
        
        # Calcul TF

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '72%'")
        tf_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '72%'")
        tfn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul TG

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '71%'")
        tg_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '71%'")
        tgn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul TH

        self.env.cr.execute("select sum(sub.balance) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '75%'")
        th_net = self.env.cr.fetchone()[0] or 0.0
        if th_net:
            th_net = -th_net

        self.env.cr.execute("select sum(sub.balance) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '75%'")
        thn_net = self.env.cr.fetchone()[0] or 0.0
        if thn_net:
            thn_net = -thn_net

        # Calcul TI

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '781%'")
        ti_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '781%'")
        tin_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul RC

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '602%'")
        rc_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '602%'")
        rcn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul RD

        self.env.cr.execute("select sum(sub.balance) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '6032%'")
        rd_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select sum(sub.balance) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '6032%'")
        rdn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul RE

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '604%' or sub.code like '605%' or sub.code like '608%'")
        re_net = -self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '604%' or sub.code like '605%' or sub.code like '608%'")
        ren_net = -self.env.cr.fetchone()[0] or 0.0

        # Calcul RF

        self.env.cr.execute("select sum(sub.balance) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '6033%'")
        rf_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select sum(sub.balance) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '6033%'")
        rfn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul RG

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '61%'")
        rg_net = -self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '61%'")
        rgn_net = -self.env.cr.fetchone()[0] or 0.0

        # Calcul RH

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '62%' or sub.code like '63%'")
        rh_net = -self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '62%' or sub.code like '63%'")
        rhn_net = -self.env.cr.fetchone()[0] or 0.0

        # Calcul RI

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '64%'")
        ri_net = -self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '64%'")
        rin_net = -self.env.cr.fetchone()[0] or 0.0

        # Calcul RJ

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '65%'")
        rj_net = -self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '65%'")
        rjn_net = -self.env.cr.fetchone()[0] or 0.0

        # Calcul XC

        xc_net = ra_net + rb_net + xb_net + te_net + tf_net + tg_net + th_net + ti_net + rc_net + rd_net + re_net + rf_net + rg_net + rh_net + ri_net + rj_net
        xcn_net = ran_net + rbn_net + xbn_net + ten_net + tfn_net + tgn_net + thn_net + tin_net + rcn_net + rdn_net + ren_net + rfn_net + rgn_net + rhn_net + rin_net + rjn_net

        # Calcul RK

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '66%'")
        rk_net = -self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '66%'")
        rkn_net = -self.env.cr.fetchone()[0] or 0.0

        # Calcul XD

        xd_net = xc_net + rk_net
        xdn_net = xcn_net + rkn_net

        # Calcul TJ

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '791%' or sub.code like '798%' or sub.code like '799%'")
        tj_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '791%' or sub.code like '798%' or sub.code like '799%'")
        tjn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul RL

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '681%' or sub.code like '691%'")
        rl_net = -self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '681%' or sub.code like '691%'")
        rln_net = -self.env.cr.fetchone()[0] or 0.0


        # Calcul XE

        xe_net = xd_net + tj_net + rl_net
        xen_net = xdn_net + tjn_net + rln_net

        # Calcul TK

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '77%'")
        tk_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '77%'")
        tkn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul TL

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '797%'")
        tl_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '797%'")
        tln_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul TM

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '787%'")
        tm_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '787%'")
        tmn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul RM

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '67%'")
        rm_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '67%'")
        rmn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul RN

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '697%'")
        rn_net = self.env.cr.fetchone()[0] or 0.0
        if rn_net:
            rn_net = -rn_net

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '697%'")
        rnn_net = self.env.cr.fetchone()[0] or 0.0
        if rnn_net:
            rnn_net = -rnn_net

        # Calcul XF

        xf_net = tk_net + tl_net + tm_net + rm_net + rn_net
        xfn_net = tkn_net + tln_net + tmn_net + rmn_net + rnn_net

        # Calcul XG

        xg_net = xe_net + xf_net
        xgn_net = xen_net + xfn_net

        # Calcul TN

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '82%'")
        tn_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '82%'")
        tnn_net = self.env.cr.fetchone()[0] or 0.

        # Calcul TO

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '84%' or sub.code like '86%' or sub.code like '88%'")
        to_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '84%' or sub.code like '86%' or sub.code like '88%'")
        ton_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul RO

        self.env.cr.execute("select sum(sub.balance) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '81%'")
        ro_net = self.env.cr.fetchone()[0] or 0.0
        if ro_net > 0:
            ro_net = -ro_net

        self.env.cr.execute("select sum(sub.balance) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '81%'")
        ron_net = self.env.cr.fetchone()[0] or 0.0
        if ron_net > 0:
            ron_net = -ron_net
        # Calcul RP

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '83%' or sub.code like '85%'")
        rp_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '83%' or sub.code like '85%'")
        rpn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul XH

        xh_net = tn_net + to_net + ro_net + rp_net
        xhn_net = tnn_net + ton_net + ron_net + rpn_net

        # Calcul RQ

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '87%'")
        rq_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '87%'")
        rqn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul RS

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '89%'")
        rs_net = -self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(sub.balance)) from \
                            (Select * from account_move_line aml, account_account aa, account_move am  where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '89%'")
        rsn_net = -self.env.cr.fetchone()[0] or 0.0

        # Calcul XI

        xi_net = xg_net + xh_net + rq_net + rs_net
        xin_net = xgn_net + xhn_net + rqn_net + rsn_net



        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'docs': docs,
            'time': time,
            'ta_net':ta_net,
            'tan_net':tan_net,
            'ra_net':ra_net,
            'ran_net':ran_net,
            'rb_net':rb_net,
            'rbn_net':rbn_net,
            'xa_net':xa_net,
            'xan_net':xan_net,
            'tb_net':tb_net,
            'tbn_net':tbn_net,
            'tc_net':tc_net,
            'tcn_net':tcn_net,
            'td_net':td_net,
            'tdn_net':tdn_net,
            'xb_net':xb_net,
            'xbn_net':xbn_net,
            'te_net':te_net,
            'ten_net':ten_net,
            'tf_net':tf_net,
            'tfn_net':tfn_net,
            'tg_net':tg_net,
            'tgn_net':tgn_net,
            'th_net':th_net,
            'thn_net':thn_net,
            'ti_net':ti_net,
            'tin_net':tin_net,
            'rc_net':rc_net,
            'rcn_net':rcn_net,
            'rd_net':rd_net,
            'rdn_net':rdn_net,
            're_net':re_net,
            'ren_net':ren_net,
            'rf_net':rf_net,
            'rfn_net':rfn_net,
            'rg_net':rg_net,
            'rgn_net':rgn_net,
            'rh_net':rh_net,
            'rhn_net':rhn_net,
            'ri_net':ri_net,
            'rin_net':rin_net,
            'rj_net':rj_net,
            'rjn_net':rjn_net,
            'xc_net':xc_net,
            'xcn_net':xcn_net,
            'rk_net':rk_net,
            'rkn_net':rkn_net,
            'xd_net':xd_net,
            'xdn_net':xdn_net,
            'tj_net':tj_net,
            'tjn_net':tjn_net,
            'rl_net':rl_net,
            'rln_net':rln_net,
            'xe_net':xe_net,
            'xen_net':xen_net,
            'tk_net':tk_net,
            'tkn_net':tkn_net,
            'tl_net':tl_net,
            'tln_net':tln_net,
            'tm_net':tm_net,
            'tmn_net':tmn_net,
            'rm_net':rm_net,
            'rmn_net':rmn_net,
            'rn_net':rn_net,
            'rnn_net':rnn_net,
            'xf_net':xf_net,
            'xfn_net':xfn_net,
            'xg_net':xg_net,
            'xgn_net':xgn_net,
            'tn_net':tn_net,
            'tnn_net':tnn_net,
            'to_net':to_net,
            'tpn_net':ton_net,
            'ro_net':ro_net,
            'ron_net':ron_net,
            'rp_net':rp_net,
            'rpn_net':rpn_net,
            'xh_net':xh_net,
            'xhn_net':xhn_net,
            'rq_net':rq_net,
            'rqn_net':rqn_net,
            'rs_net':rs_net,
            'rsn_net':rsn_net,
            'xi_net':xi_net,
            'xin_net':xin_net,

        }
        return docargs
