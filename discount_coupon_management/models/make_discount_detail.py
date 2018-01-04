# -*- coding: utf-8 -*-
from odoo import api,fields, models,_
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
import string as st
import random
from datetime import date,datetime

class MakeDiscountCoupon(models.Model):
	_name="make.discount.coupon"
	_description="Making Discount Coupon Detail"
	company_name=fields.Many2one('make.company',string="Company Name:")
	#company_name=fields.Char(string='Company Name:',required=True)
	coupon_title=fields.Char(string='Coupon Title:')
	customer_name=fields.Char(string='Customer Name:')
	coupon_bunch=fields.Integer()
	coupon_type=fields.Selection([
		('seasson','Seassonly'),
		('silver','Silver'),
		('gold','Golden')
		])
	start_date=fields.Date(string="Starting From")
	valid_date=fields.Date(string="Valid Upto:")
	offer=fields.Char(string="Scheme Name:")
	
	@api.constrains('coupon_type')
	def check_date(self):
		if self.coupon_type=="silver":			
			if self.get_diff_date()!=1:
				raise UserError(_("For Couopn type Silver, Require to give range of year for 1 year!!!"))
		elif self.coupon_type=="gold":
			if self.get_diff_date()<2:
				raise UserError(_("For Couopn type Golden, Require to give at least range of year for 2 year!!!"))


	@api.constrains('valid_date')
	def check_valid_date(self):		
		if str(self.start_date) > str(self.valid_date):
			raise ValidationError(_("Ending date will be bigger than starting Date!!!"))


	@api.model
	def create(self,values):
		obj=super(MakeDiscountCoupon,self).create(values)
		obj1=self.env['coupon.detail']
		for i in range(int(values['coupon_bunch'])):
			code=str(random.choice(st.ascii_letters))+str(i**3)			
			obj1.create({'company_name':values['company_name'],'coupon_title':values['coupon_title'],'coupon_id':code,'redeem':False,'type_coupon':values['coupon_type'],'start_from':values['start_date'],'valid_to':values['valid_date']})
		return obj

	def get_diff_date(self):
		self.start_date=str(self.start_date)
		self.valid_date=str(self.valid_date)
		lst1=self.start_date.split("-")
		lst2=self.valid_date.split("-")
		sdate=date(int(lst1[0]),int(lst1[1]),int(lst1[2]))
		vdate=date(int(lst2[0]),int(lst2[1]),int(lst2[2]))
		diff_date=vdate-sdate
		return diff_date.days//365