# -*- coding: utf-8 -*-
from odoo import api,fields, models

class CouponDetail(models.Model):
	#_inherit="res.partner"
	
	_name="coupon.detail"
	_sql_constratints=[('Unique Coupon Code','unique(coupon_id)','Please enter unique code.')]
	_rec_name="coupon_id"
	_description="Discount Coupon Detail"	

	#state=fields.Selection([('open', 'Waiting for Approval'), ('confirm', 'Approved')], string='Status',default='open')
	company_name=fields.Many2one('make.company',string="Company Name:")
	coupon_title=fields.Char(string='Coupon Title:')
	coupon_id=fields.Char(string="Coupon Code")
	redeem=fields.Boolean(string="Redeem(y/n)")
	type_coupon=fields.Selection([
		('seasson','Seassonly'),
		('silver','Silver'),
		('gold','Golden')
		])
	start_from=fields.Date(string="Start From")
	valid_to=fields.Date(string="Valid upto")

	@api.constrains('coupon_id')
	def check_couopn_code(self):
		pass

