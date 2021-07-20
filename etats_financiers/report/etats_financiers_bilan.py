# -*- coding: utf-8 -*-

import time
from odoo import api, models
from dateutil.parser import parse
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class ReportBilan(models.AbstractModel):
    _name = 'report.etats_financiers.report_bilan'

    @api.model
    def _get_report_values(self, docids, data=None):
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_id'))

        debut_n = docs.debut - relativedelta(years=+1)
        fin_n = docs.fin - relativedelta(years=+1)

        # Calcul AE

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '2181%' or sub.code like '211%' or sub.code like '2191%' \
                            group by sub.code) as query")
        ae_brut = self.env.cr.fetchone()[0] or 0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '2811%' or sub.code like '2818%' or sub.code like '2911%' or sub.code like '2918%' or sub.code like '2919%' \
                            group by sub.code) as query")
        ae_ad = self.env.cr.fetchone()[0] or 0

        ae_net = ae_brut - ae_ad

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '2181%' or sub.code like '211%' or sub.code like '2191%' \
                            group by sub.code) as query")
        aen_brut = self.env.cr.fetchone()[0] or 0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '2811%' or sub.code like '2818%' or sub.code like '2911%' or sub.code like '2918%' or sub.code like '2919%' \
                            group by sub.code) as query")
        aen_ad = self.env.cr.fetchone()[0] or 0

        aen_net = aen_brut - aen_ad

        # Calcul AF

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '212%' or sub.code like '213%' or sub.code like '214%' or sub.code like '2193%' \
                            group by sub.code) as query")
        af_brut = self.env.cr.fetchone()[0] or 0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '2812%' or sub.code like '2813%' or sub.code like '2814%' or sub.code like '2912%' or sub.code like '2913%' or sub.code like '2914%' or sub.code like '2919%' \
                            group by sub.code) as query")
        af_ad = self.env.cr.fetchone()[0] or 0

        af_net = af_brut - af_ad

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '212%' or sub.code like '213%' or sub.code like '214%' or sub.code like '2193%' \
                            group by sub.code) as query")
        afn_brut = self.env.cr.fetchone()[0] or 0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '2812%' or sub.code like '2813%' or sub.code like '2814%' or sub.code like '2912%' or sub.code like '2913%' or sub.code like '2914%' or sub.code like '2919%' \
                            group by sub.code) as query")
        afn_ad = self.env.cr.fetchone()[0] or 0

        afn_net = afn_brut - afn_ad

        # Calcul AG

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '215%' or sub.code like '216%' \
                            group by sub.code) as query")
        ag_brut = self.env.cr.fetchone()[0] or 0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '2815%' or sub.code like '2816%' or sub.code like '2915%' or sub.code like '2916%' \
                            group by sub.code) as query")
        ag_ad = self.env.cr.fetchone()[0] or 0

        ag_net = ag_brut - ag_ad

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '215%' or sub.code like '216%' \
                            group by sub.code) as query")
        agn_brut = self.env.cr.fetchone()[0] or 0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '2815%' or sub.code like '2816%' or sub.code like '2915%' or sub.code like '2916%' \
                            group by sub.code) as query")
        agn_ad = self.env.cr.fetchone()[0] or 0

        agn_net = agn_brut - agn_ad

        # Calcul AH

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '217%' or sub.code like '218%'and sub.code not like '2181%' or sub.code like '2198%'\
                            group by sub.code) as query")
        ah_brut = self.env.cr.fetchone()[0] or 0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '2817%' or sub.code like '2818%' or sub.code like '2917%' or sub.code like '2918%' or sub.code like '2919%' \
                            group by sub.code) as query")
        ah_ad = self.env.cr.fetchone()[0] or 0

        ah_net = ah_brut - ah_ad

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '217%' or sub.code like '218%' and sub.code not like '2181%' or sub.code like '2198%'\
                            group by sub.code) as query")
        ahn_brut = self.env.cr.fetchone()[0] or 0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '2817%' or sub.code like '2818%' or sub.code like '2917%' or sub.code like '2918%' or sub.code like '2919%' \
                            group by sub.code) as query")
        ahn_ad = self.env.cr.fetchone()[0] or 0

        ahn_net = ahn_brut - ahn_ad

        # Calcul AD

        ad_brut = ae_brut + af_brut + ag_brut + ah_brut
        ad_ad = ae_ad + af_ad + ag_ad + ah_ad
        ad_net = ae_net + af_net + ag_net + ah_net
        adn_net = aen_net + afn_net + agn_net + ahn_net

        # Calcul AJ

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '22%' \
                            group by sub.code) as query")
        aj_brut = self.env.cr.fetchone()[0] or 0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '282%' or sub.code like '292%' \
                            group by sub.code) as query")
        aj_ad = self.env.cr.fetchone()[0] or 0

        aj_net = aj_brut - aj_ad

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '22%' \
                            group by sub.code) as query")
        ajn_brut = self.env.cr.fetchone()[0] or 0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '282%' or sub.code like '292%' \
                            group by sub.code) as query")
        ajn_ad = self.env.cr.fetchone()[0] or 0

        ajn_net = ajn_brut - ajn_ad

        # Calcul AK

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '231%' or sub.code like '232%' or sub.code like '233%' or sub.code like '237%' or sub.code like '2391%' \
                            group by sub.code) as query")
        ak_brut = self.env.cr.fetchone()[0] or 0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '2831%' or sub.code like '2832%' or sub.code like '2833%' or sub.code like '2837%' or sub.code like '2931%' or sub.code like '2932%' or sub.code like '2933%' or sub.code like '2937%' or sub.code like '2939%' \
                            group by sub.code) as query")
        ak_ad = self.env.cr.fetchone()[0] or 0

        ak_net = ak_brut - ak_ad

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '231%' or sub.code like '232%' or sub.code like '233%' or sub.code like '237%' or sub.code like '2391%' \
                            group by sub.code) as query")
        akn_brut = self.env.cr.fetchone()[0] or 0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '2831%' or sub.code like '2832%' or sub.code like '2833%' or sub.code like '2837%' or sub.code like '2931%' or sub.code like '2932%' or sub.code like '2933%' or sub.code like '2937%' or sub.code like '2939%' \
                            group by sub.code) as query")
        akn_ad = self.env.cr.fetchone()[0] or 0

        akn_net = akn_brut - akn_ad

        # Calcul AL

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '234%' or sub.code like '235%' or sub.code like '238%' or sub.code like '2392%' or sub.code like '2393%' or sub.code like '2398%'\
                            group by sub.code) as query")
        al_brut = self.env.cr.fetchone()[0] or 0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '2834%' or sub.code like '2835%' or sub.code like '2838%' or sub.code like '2934%' or sub.code like '2935%' or sub.code like '2938%' \
                            group by sub.code) as query")
        al_ad = self.env.cr.fetchone()[0] or 0

        al_net = al_brut - al_ad

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '234%' or sub.code like '235%' or sub.code like '238%' or sub.code like '2392%' or sub.code like '2393%' or sub.code like '2398%'\
                            group by sub.code) as query")
        aln_brut = self.env.cr.fetchone()[0] or 0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '2834%' or sub.code like '2835%' or sub.code like '2838%' or sub.code like '2934%' or sub.code like '2935%' or sub.code like '2938%'\
                            group by sub.code) as query")
        aln_ad = self.env.cr.fetchone()[0] or 0

        aln_net = aln_brut - aln_ad

        # Calcul AM

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '24%' and sub.code not like '245%' and sub.code not like '2495%' \
                            group by sub.code) as query")
        am_brut = self.env.cr.fetchone()[0] or 0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '284%' and sub.code not like '2845%' or sub.code like '294%' and sub.code not like '2945%' \
                            group by sub.code) as query")
        am_ad = self.env.cr.fetchone()[0] or 0

        am_net = am_brut - am_ad

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '24%' and sub.code not like  '245%' and sub.code not like '2495%' \
                            group by sub.code) as query")
        amn_brut = self.env.cr.fetchone()[0] or 0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '284%' and sub.code not like '2845%' or sub.code like '294%' and sub.code not like '2945%' \
                            group by sub.code) as query")
        amn_ad = self.env.cr.fetchone()[0] or 0

        amn_net = amn_brut - amn_ad

        # Calcul AN

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '245%' or sub.code like '2495%' \
                            group by sub.code) as query")
        an_brut = self.env.cr.fetchone()[0] or 0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '2845%' or sub.code like '2945%' \
                            group by sub.code) as query")
        an_ad = self.env.cr.fetchone()[0] or 0

        an_net = an_brut - an_ad

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '245%' or sub.code like '2495%' \
                            group by sub.code) as query")
        ann_brut = self.env.cr.fetchone()[0] or 0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '2845%' or sub.code like '2945%' \
                            group by sub.code) as query")
        ann_ad = self.env.cr.fetchone()[0] or 0

        ann_net = ann_brut - ann_ad

        # Calcul AP

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '251%' or sub.code like '252%' \
                            group by sub.code) as query")
        ap_brut = self.env.cr.fetchone()[0] or 0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '2951%' or sub.code like '2952%' \
                            group by sub.code) as query")
        ap_ad = self.env.cr.fetchone()[0] or 0

        ap_net = ap_brut - ap_ad

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '251%' or sub.code like '252%' \
                            group by sub.code) as query")
        apn_brut = self.env.cr.fetchone()[0] or 0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '2951%' or sub.code like '2952%' \
                            group by sub.code) as query")
        apn_ad = self.env.cr.fetchone()[0] or 0

        apn_net = apn_brut - apn_ad

        # Calcul AI

        ai_brut = aj_brut + ak_brut + al_brut + am_brut + an_brut
        ai_ad = aj_ad + ak_ad + al_ad + am_ad + an_ad
        ai_net = aj_net + ak_net + al_net + am_net + an_net
        ain_net = ajn_net + akn_net + aln_net + amn_net + ann_net

        # Calcul AR

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '26%' \
                            group by sub.code) as query")
        ar_brut = self.env.cr.fetchone()[0] or 0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '296%' \
                            group by sub.code) as query")
        ar_ad = self.env.cr.fetchone()[0] or 0

        ar_net = ar_brut - ar_ad

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '26%' \
                            group by sub.code) as query")
        arn_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '296%' \
                            group by sub.code) as query")
        arn_ad = self.env.cr.fetchone()[0] or 0.0

        arn_net = arn_brut - arn_ad

        # Calcul AS

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '27%' \
                            group by sub.code) as query")
        as_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '297%' \
                            group by sub.code) as query")
        as_ad = self.env.cr.fetchone()[0] or 0.0

        as_net = as_brut - as_ad

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '27%' \
                            group by sub.code) as query")
        asn_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '297%' \
                            group by sub.code) as query")
        asn_ad = self.env.cr.fetchone()[0] or 0.0

        asn_net = asn_brut - asn_ad

        # Calcul AQ

        aq_brut = ar_brut + as_brut
        aq_ad = ar_ad + as_ad
        aq_net = ar_net + as_net
        aqn_net = arn_net + asn_net

        # Calcul AZ

        az_brut = ad_brut + ai_brut + aq_brut
        az_ad = ad_ad + ai_ad + aq_ad
        az_net = ad_net + ai_net + aq_net
        azn_net = adn_net + ain_net + aqn_net


        # Calcul BA

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '485%' or sub.code like '488%' \
                            group by sub.code) as query")
        ba_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '498%' \
                            group by sub.code) as query")
        ba_ad = self.env.cr.fetchone()[0] or 0.0

        ba_net = ba_brut - ba_ad

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '485%' or sub.code like '488%' \
                            group by sub.code) as query")
        ban_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '498%' \
                            group by sub.code) as query")
        ban_ad = self.env.cr.fetchone()[0] or 0.0

        ban_net = ban_brut - ban_ad

        # Calcul BB

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '31%' or sub.code like '32%' or sub.code like '33%' or sub.code like '34%' or sub.code like '35%' or sub.code like '36%' or sub.code like '37%' or sub.code like '38%' \
                            group by sub.code) as query")
        bb_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '39%' \
                            group by sub.code) as query")
        bb_ad = self.env.cr.fetchone()[0] or 0.0

        bb_net = bb_brut - bb_ad

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '31%' or sub.code like '32%' or sub.code like '33%' or sub.code like '34%' or sub.code like '35%' or sub.code like '36%' or sub.code like '37%' or sub.code like '38%' \
                            group by sub.code) as query")
        bbn_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '39%' \
                            group by sub.code) as query")
        bbn_ad = self.env.cr.fetchone()[0] or 0.0

        bbn_net = bbn_brut - bbn_ad

        # Calcul BH

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '409%' \
                            group by sub.code) as query")
        bh_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '490%' \
                            group by sub.code) as query")
        bh_ad = self.env.cr.fetchone()[0] or 0.0

        bh_net = bh_brut - bh_ad

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '409%' \
                            group by sub.code) as query")
        bhn_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '490%' \
                            group by sub.code) as query")
        bhn_ad = self.env.cr.fetchone()[0] or 0.0

        bhn_net = bhn_brut - bhn_ad

        # Calcul BI

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '41%' and sub.code not like '419%' \
                            group by sub.code) as query")
        bi_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '491%' \
                            group by sub.code) as query")
        bi_ad = self.env.cr.fetchone()[0] or 0.0

        bi_net = bi_brut - bi_ad

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '41%' or sub.code like '419%' \
                            group by sub.code) as query")
        bin_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '491%' \
                            group by sub.code) as query")
        bin_ad = self.env.cr.fetchone()[0] or 0.0

        bin_net = bin_brut - bin_ad

        # Calcul BJ

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '185%' or sub.code like '42%' or sub.code like '43%' or sub.code like '44%' or sub.code like '45%' or sub.code like '46%' or sub.code like '47%' and sub.code not like '478%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        bj_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '492%' or sub.code like '493%' or sub.code like '494%' or sub.code like '495%' or sub.code like '496%' or sub.code like '497%' \
                            group by sub.code) as query")
        bj_ad = self.env.cr.fetchone()[0] or 0.0

        bj_net = bj_brut - bj_ad

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '185%' or sub.code like '42%' or sub.code like '43%' or sub.code like '44%' or sub.code like '45%' or sub.code like '46%' or sub.code like '47%' and sub.code not like '478%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        bjn_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '492%' or sub.code like '493%' or sub.code like '494%' or sub.code like '495%' or sub.code like '496%' or sub.code like '497%' \
                            group by sub.code) as query")
        bjn_ad = self.env.cr.fetchone()[0] or 0.0

        bjn_net = bjn_brut - bjn_ad

        # Calcul BG

        bg_brut = bh_brut + bi_brut + bj_brut
        bg_ad = bh_ad + bi_ad + bj_ad
        bg_net = bh_net + bi_net + bj_net
        bgn_net = bhn_net + bin_net + bjn_net

        # Calcul BK

        bk_brut = ba_brut + bb_brut + bg_brut
        bk_ad = ba_ad + bb_ad + bg_ad
        bk_net = ba_net + bb_net + bg_net
        bkn_net = ban_net + bbn_net + bgn_net

        # Calcul BQ

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '50%' \
                            group by sub.code) as query")
        bq_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '590%' \
                            group by sub.code) as query")
        bq_ad = self.env.cr.fetchone()[0] or 0.0

        bq_net = bq_brut - bq_ad

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '50%' \
                            group by sub.code) as query")
        bqn_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '590%' \
                            group by sub.code) as query")
        bqn_ad = self.env.cr.fetchone()[0] or 0.0

        bqn_net = bqn_brut - bqn_ad

        # Calcul BR

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '51%' \
                            group by sub.code) as query")
        br_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '591%' \
                            group by sub.code) as query")
        br_ad = self.env.cr.fetchone()[0] or 0.0

        br_net = br_brut - br_ad

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '51%' \
                            group by sub.code) as query")
        brn_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '591%' \
                            group by sub.code) as query")
        brn_ad = self.env.cr.fetchone()[0] or 0.0

        brn_net = brn_brut - brn_ad

        # Calcul BS

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from\
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '52%' or sub.code like '53%' or sub.code like '54%' or sub.code like '55%' or sub.code like '57%' or sub.code like '581%' or sub.code like '582%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        bs_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '592%' or sub.code like '593%' or sub.code like '594%' \
                            group by sub.code) as query")
        bs_ad = self.env.cr.fetchone()[0] or 0.0

        bs_net = bs_brut - bs_ad

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '52%' or sub.code like '53%' or sub.code like '54%' or sub.code like '55%' or sub.code like '57%' or sub.code like '581%' or sub.code like '582%'\
                            group by sub.code having sum(sub.balance) > 0) as query")
        bsn_brut = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '592%' or sub.code like '593%' or sub.code like '594%' \
                            group by sub.code) as query")
        bsn_ad = self.env.cr.fetchone()[0] or 0.0

        bsn_net = bsn_brut - bsn_ad

        # Calcul BT

        bt_brut = bq_brut + br_brut + bs_brut
        bt_ad = bq_ad + br_ad + bs_ad
        bt_net = bq_net + br_net + bs_net
        btn_net = bqn_net + brn_net + bsn_net

        # Calcul BU

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '478%' \
                            group by sub.code) as query")
        bu_brut = self.env.cr.fetchone()[0] or 0.0

        bu_net = bu_brut

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '478%' \
                            group by sub.code) as query")
        bun_brut = self.env.cr.fetchone()[0] or 0.0

        bun_net = bun_brut

        # Calcul BZ

        bz_brut = az_brut + bk_brut + bt_brut + bu_brut
        bz_ad = az_ad + bk_ad + bt_ad
        bz_net = az_net + bk_net + bt_net + bu_net
        bzn_net = azn_net + bkn_net + btn_net + bun_net

        # BILAN PASSIF

        # Calcul CA

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '101%' or sub.code like '102%' or sub.code like '103%' or sub.code like '104%' \
                            group by sub.code) as query")
        ca_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '101%' or sub.code like '102%' or sub.code like '103%' or sub.code like '104%' \
                            group by sub.code) as query")
        can_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul CB

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '109%' \
                            group by sub.code) as query")
        cb_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '109%' \
                            group by sub.code) as query")
        cbn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul CD

        self.env.cr.execute("select sum(query.solde)  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '105%' \
                            group by sub.code) as query")
        cd_net = self.env.cr.fetchone()[0] or 0.0
        if cd_net > 0:
            cd_net = -cd_net

        self.env.cr.execute("select sum(query.solde)  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '105%' \
                            group by sub.code) as query")
        cdn_net = self.env.cr.fetchone()[0] or 0.0
        if cdn_net > 0:
            cdn_net = -cd_net

        # Calcul CE

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '106%' \
                            group by sub.code) as query")
        ce_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '106%' \
                            group by sub.code) as query")
        cen_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul CF

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '111%' or sub.code like '112%' or sub.code like '113%' \
                            group by sub.code) as query")
        cf_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '111%' or sub.code like '112%' or sub.code like '113%' \
                            group by sub.code) as query")
        cfn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul CG

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '118%' \
                            group by sub.code) as query")
        cg_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '118%' \
                            group by sub.code) as query")
        cgn_net = self.env.cr.fetchone()[0] or 0.0


        # Calcul CH

        self.env.cr.execute("select sum(query.solde)  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '121%' or sub.code like '129%' \
                            group by sub.code) as query")
        ch_net = self.env.cr.fetchone()[0] or 0.0

        if ch_net < 0:
            ch_net = -ch_net

        self.env.cr.execute("select sum(query.solde) from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '121%' or sub.code like '129%' \
                            group by sub.code) as query")
        chn_net = self.env.cr.fetchone()[0] or 0.0

        if chn_net > 0:
            chn_net = -chn_net

        # Calcul CJ

        self.env.cr.execute("select sum(query.solde) from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(docs.debut)+"' and  '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '6%' or sub.code like '7%' or sub.code like '8%' \
                            group by sub.code) as query")
        cj_net = -self.env.cr.fetchone()[0] or 0.0


        self.env.cr.execute("select sum(query.solde) from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date between '"+str(debut_n)+"' and  '"+str(fin_n)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '6%' or sub.code like '7%' or sub.code like '8%' \
                            group by sub.code) as query")
        cjn_net = -self.env.cr.fetchone()[0] or 0.0


        # Calcul CL

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '14%' \
                            group by sub.code) as query")
        cl_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '14%' \
                            group by sub.code) as query")
        cln_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul CM

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '15%' \
                            group by sub.code) as query")
        cm_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '15%' \
                            group by sub.code) as query")
        cmn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul CP
        cp_net = ca_net + cb_net + cd_net + ce_net + cf_net + cg_net + ch_net + cj_net + cl_net + cm_net
        cpn_net = can_net + cbn_net + cdn_net + cen_net + cfn_net + cgn_net + chn_net + cjn_net + cln_net + cmn_net

        # Calcul DA

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '16%' or sub.code like '181%' or sub.code like '182%' or sub.code like '183%' or sub.code like '184%' \
                            group by sub.code) as query")
        da_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '16%' or sub.code like '181%' or sub.code like '182%' or sub.code like '183%' or sub.code like '184%' \
                            group by sub.code) as query")
        dan_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul DB

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '17%' \
                            group by sub.code) as query")
        db_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '17%' \
                            group by sub.code) as query")
        dbn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul DC

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '19%' \
                            group by sub.code) as query")
        dc_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '19%' \
                            group by sub.code) as query")
        dcn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul DD
        dd_net = da_net + db_net + dc_net
        ddn_net = dan_net + dbn_net + dcn_net

        # Calcul DF
        df_net = cp_net + dd_net
        dfn_net = cpn_net + ddn_net

        # Calcul DH

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '481%' or sub.code like '482%' or sub.code like '484%' or sub.code like '4998%' \
                            group by sub.code) as query")
        dh_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '481%' or sub.code like '482%' or sub.code like '484%' or sub.code like '4998%' \
                            group by sub.code) as query")
        dhn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul DI

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '419%' \
                            group by sub.code) as query")
        di_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '419%' \
                            group by sub.code) as query")
        din_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul DJ

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '40%' and sub.code not like '409%' \
                            group by sub.code) as query")
        dj_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '40%' and sub.code not like '409%' \
                            group by sub.code) as query")
        djn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul DK

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '42%' or sub.code like '43%' or sub.code like '44%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        dk_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '42%' or sub.code like '43%' or sub.code like '44%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        dkn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul DM

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '185%' or sub.code like '45%' or sub.code like '46%' or sub.code like '47%' and sub.code not like '479%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        dm_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '185%' or sub.code like '45%' or sub.code like '46%' or sub.code like '47%' and sub.code not like '479%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        dmn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul DN

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '499%' or sub.code like '599%' and sub.code not like '4998%' \
                            group by sub.code) as query")
        dn_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '499%' or sub.code like '599%' and sub.code not like '4998%' \
                            group by sub.code) as query")
        dnn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul DP
        dp_net = dh_net + di_net + dj_net + dk_net + dm_net + dn_net
        dpn_net = dhn_net + din_net + djn_net + dkn_net + dmn_net + dnn_net


        # Calcul DQ

        self.env.cr.execute("select abs(sum(query.solde)) from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '564%' or sub.code like '565%' \
                            group by sub.code) as query")
        dq_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '564%' or sub.code like '565%' \
                            group by sub.code) as query")
        dqn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul DR

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '52%' or sub.code like '53%' or sub.code like '561%' or sub.code like '566%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        dr_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '52%' or sub.code like '53%' or sub.code like '561%' or sub.code like '566%'\
                            group by sub.code having sum(sub.balance) < 0) as query")
        drn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul DT
        dt_net = dq_net + dr_net
        dtn_net = dqn_net + drn_net

        # Calcul DV

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date <= '"+str(docs.fin)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '479%' \
                            group by sub.code) as query")
        dv_net = self.env.cr.fetchone()[0] or 0.0

        self.env.cr.execute("select abs(sum(query.solde))  from (select sum(sub.balance) solde from \
                            (select * from account_move_line aml, account_account aa, account_move am where aml.account_id = aa.id and aml.move_id = am.id and aml.date < '"+str(docs.debut)+"' and aml.company_id = '"+str(docs.company_id.id)+"') as sub\
                            where sub.code like '479%' \
                            group by sub.code) as query")
        dvn_net = self.env.cr.fetchone()[0] or 0.0

        # Calcul DZ
        dz_net = df_net + dp_net + dt_net + dv_net
        dzn_net = dfn_net + dpn_net + dtn_net + dvn_net

        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'docs': docs,
            'time': time,
            'ae_brut': ae_brut,
            'ae_ad': ae_ad,
            'ae_net':ae_net,
            'aen_net':aen_net,
            'af_brut': af_brut,
            'af_ad': af_ad,
            'af_net':af_net,
            'afn_net':afn_net,
            'ag_brut': ag_brut,
            'ag_ad': ag_ad,
            'ag_net':ag_net,
            'agn_net':agn_net,
            'ah_brut': ah_brut,
            'ah_ad': ah_ad,
            'ah_net':ah_net,
            'ahn_net':ahn_net,
            'ad_brut': ad_brut,
            'ad_ad': ad_ad,
            'ad_net':ad_net,
            'adn_net':adn_net,
            'aj_brut': aj_brut,
            'aj_ad': aj_ad,
            'aj_net':aj_net,
            'ajn_net':ajn_net,
            'ak_brut': ak_brut,
            'ak_ad': ak_ad,
            'ak_net':ak_net,
            'akn_net':akn_net,
            'al_brut': al_brut,
            'al_ad': al_ad,
            'al_net':al_net,
            'aln_net':aln_net,
            'am_brut': am_brut,
            'am_ad': am_ad,
            'am_net':am_net,
            'amn_net':amn_net,
            'an_brut': an_brut,
            'an_ad': an_ad,
            'an_net':an_net,
            'ann_net':ann_net,
            'ap_brut': ap_brut,
            'ap_ad': ap_ad,
            'ap_net':ap_net,
            'apn_net':apn_net,
            'ai_brut': ai_brut,
            'ai_ad': ai_ad,
            'ai_net':ai_net,
            'ain_net':ain_net,
            'ar_brut': ar_brut,
            'ar_ad': ar_ad,
            'ar_net':ar_net,
            'arn_net':arn_net,
            'as_brut': as_brut,
            'as_ad': as_ad,
            'as_net':as_net,
            'asn_net':asn_net,
            'aq_brut': aq_brut,
            'aq_ad': aq_ad,
            'aq_net':aq_net,
            'aqn_net':aqn_net,
            'az_brut': az_brut,
            'az_ad': az_ad,
            'az_net':az_net,
            'azn_net':azn_net,
            'ba_brut':ba_brut,
            'ba_ad': ba_ad,
            'ba_net':ba_net,
            'ban_net':ban_net,
            'bb_brut':bb_brut,
            'bb_ad': bb_ad,
            'bb_net':bb_net,
            'bbn_net':bbn_net,
            'bg_brut':bg_brut,
            'bg_ad': bg_ad,
            'bg_net':bg_net,
            'bgn_net':bgn_net,
            'bh_brut':bh_brut,
            'bh_ad': bh_ad,
            'bh_net':bh_net,
            'bhn_net':bhn_net,
            'bi_brut':bi_brut,
            'bi_ad': bi_ad,
            'bi_net':bi_net,
            'bin_net':bin_net,
            'bj_brut':bj_brut,
            'bj_ad': bj_ad,
            'bj_net':bj_net,
            'bjn_net':bjn_net,
            'bk_brut':bk_brut,
            'bk_ad': bk_ad,
            'bk_net':bk_net,
            'bkn_net':bkn_net,
            'bq_brut':bq_brut,
            'bq_ad': bq_ad,
            'bq_net':bq_net,
            'bqn_net':bqn_net,
            'br_brut':br_brut,
            'br_ad': br_ad,
            'br_net':br_net,
            'brn_net':brn_net,
            'bs_brut':bs_brut,
            'bs_ad': bs_ad,
            'bs_net':bs_net,
            'bsn_net':bsn_net,
            'bt_brut':bt_brut,
            'bt_ad': bt_ad,
            'bt_net':bt_net,
            'btn_net':btn_net,
            'bu_brut':bu_brut,
            'bu_net':bu_net,
            'bun_net':bun_net,
            'bz_brut':bz_brut,
            'bz_ad': bz_ad,
            'bz_net':bz_net,
            'bzn_net':bzn_net,
            'ca_net':ca_net,
            'can_net':can_net,
            'cb_net':cb_net,
            'cbn_net':cbn_net,
            'cd_net':cd_net,
            'cdn_net':cdn_net,
            'ce_net':ce_net,
            'cen_net':cen_net,
            'cf_net':cf_net,
            'cfn_net':cfn_net,
            'cg_net':cg_net,
            'cgn_net':cgn_net,
            'ch_net':ch_net,
            'chn_net':chn_net,
            'cj_net':cj_net,
            'cjn_net':cjn_net,
            'cl_net':cl_net,
            'cln_net':cln_net,
            'cm_net':cm_net,
            'cmn_net':cmn_net,
            'cp_net':cp_net,
            'cpn_net':cpn_net,
            'da_net':da_net,
            'dan_net':dan_net,
            'db_net':db_net,
            'dbn_net':dbn_net,
            'dc_net':dc_net,
            'dcn_net':dcn_net,
            'dd_net':dd_net,
            'ddn_net':ddn_net,
            'df_net':df_net,
            'dfn_net':dfn_net,
            'dh_net':dh_net,
            'dhn_net':dhn_net,
            'di_net':di_net,
            'din_net':din_net,
            'dj_net':dj_net,
            'djn_net':djn_net,
            'dk_net':dk_net,
            'dkn_net':dkn_net,
            'dm_net':dm_net,
            'dmn_net':dmn_net,
            'dn_net':dn_net,
            'dnn_net':dnn_net,
            'dp_net':dp_net,
            'dpn_net':dpn_net,
            'dq_net':dq_net,
            'dqn_net':dqn_net,
            'dr_net':dr_net,
            'drn_net':drn_net,
            'dt_net':dt_net,
            'dtn_net':dtn_net,
            'dv_net':dv_net,
            'dvn_net':dvn_net,
            'dz_net':dz_net,
            'dzn_net':dzn_net,
        }
        return docargs
