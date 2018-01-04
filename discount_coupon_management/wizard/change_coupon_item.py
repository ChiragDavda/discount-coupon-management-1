# -*- coding: utf-8 -*-

from odoo import models, api, fields


class ChangeCouponBunch(models.TransientModel):
    _name = 'change.coupon.detail'
    _description = 'Wizard for Coupon'

    bunch=fields.Integer("How many Coupon you want???")
    @api.multi
    def state_bunch(self):
    	# print(self.env.context['active_ids'])
    	# print(self.bunch)
    	active_ids = self.env.context['active_ids']
    	lines = self.env['make.discount.coupon'].search([('id', 'in', active_ids)])
    	for line in lines:
    	 	line.write({'coupon_bunch':self.bunch})