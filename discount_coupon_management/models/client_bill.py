# -*- coding: utf-8 -*-
from odoo import fields,models,api,_
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
import re
from datetime import datetime
class MakeBill(models.Model):
	_name="make.bill"
	_description="Register New Bill!!!"
	
	customer_name=fields.Char(string="Customer Name:")
	email=fields.Char(string="Email Address:")
	conatact_no=fields.Char(string="Contact Number:")
	coupon_code=fields.Char(string="coupon code")	
	bill_id=fields.Char(string="Bill Id:")
	amount=fields.Integer(string="Amount:")

	
	@api.constrains('conatact_no')
	def check_phone_no(self):
		if not re.match("[0-9]{10}",self.conatact_no):
			raise ValidationError(_('Mobile number must be 10 digits!!!'))

	@api.constrains('email')
	def check_email(self):
		if not re.match("[^@]+@[^@]+\.[^@]+",self.email):
			raise ValidationError(_('Email Address is not valid!!!'))			

	@api.constrains('coupon_code')
	def check_coupon(self):
		obj=self.env['coupon.detail']
		data=obj.search([('coupon_id','=',self.coupon_code),('redeem','=',False),('valid_to','>=',datetime.now().date().strftime('%Y-%m-%d'))])
		if len(data)>0:			
			data.write({'redeem':True})			
		else:
			raise ValidationError(_('Coupon Code is Invalid!!! Maybe out dated!!!'))


	@api.constrains('amount')
	def check_amount(self):
		if self.amount<=0:
			raise ValidationError(_('Amount will be more than zero!!!'))
