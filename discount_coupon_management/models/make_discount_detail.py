# -*- coding: utf-8 -*-
from odoo import api,fields, models

class MakeDiscountCoupon(models.Model):
	_name="make.discount.coupon"
	_description="Making Discount Coupon Detail"
	
	company_name=fields.Char(string='Company Name:',required=True)
	coupon_title=fields.Char(string='Coupon Title:',required=True)
	customer_name=fields.Char(string='Customer Name:')
	coupon_bunch=fields.Selection([
		('50','50'),
		('100','100'),
		('200','200'),
		('300','300'),
		('400','400'),
		('500','500'),
		])
	valid_date=fields.Date(string="Valid Upto:",required=True)
	offer=fields.Char(string="Scheme Name:",required=True)
	
	
