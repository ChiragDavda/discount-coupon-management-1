# -*- coding: utf-8 -*-

from odoo import models, api, fields


class ChangeCouponDetail(models.TransientModel):
    _name = 'make.coupon.detail'
    _description = 'Wizard for Coupon'

    @api.multi
    def state_redeem(self):
    	active_ids = self.env.context['active_ids']
    	lines = self.env['coupon.detail'].search([('id', 'in', active_ids)])
    	for line in lines:
    	 	line.write({'redeem':False})
