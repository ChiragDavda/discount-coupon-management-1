# -*- coding: utf-8 -*-
import time
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class CouponDetailsSummary(models.TransientModel):

    _name = 'coupon.detail.summary'

    date_from = fields.Date(string='From', required=True, default=lambda *a: time.strftime('%Y-%m-01'))
    date_to = fields.Date(string='To', required=True,
                            default=lambda *a: time.strftime('%Y-%m-31'))

    @api.multi
    def print_report(self):
        self.ensure_one()
        [data] = self.read()
        coupon = self.env['coupon.detail'].search([('start_from','>=',data['date_from']),('valid_to','<=',data['date_to'])])
        # datas = {
        #     'ids': [],
        #     'model': 'coupon.detail',
        #     'form': data
        # }
        print(">>>>>>>>>>>>>>>>>>>data: ",data)
        print(">>>>>>>>>>>>>>>>>>>coupon: ",coupon)
        if not coupon:
        	raise UserError(_("No Data found from given dates!!!Try Again!!"))
        else:
	        return self.env.ref(
	            'discount_coupon_management.wizard_action_report_coupon_detail'
	            '').report_action(coupon)