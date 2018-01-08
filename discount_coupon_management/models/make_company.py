# -*- coding: utf-8 -*-
import re
from odoo import fields,models,api,_
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
class MakeCompany(models.Model):
	_name="make.company"
	_description="Register New Company!!!"
	_inherit = ['mail.thread']
	name=fields.Char(string="Company Name:")
	#name=fields.One2many('coupon.detail','company_name',string="Company Name:")
	address=fields.Text(string="Address:")
	email=fields.Char(string="Email Address:")
	conatact_no=fields.Char(string="Contact Number:")
	licence_no=fields.Char(string="Licene Number:")


	@api.constrains('conatact_no')
	def check_phone_no(self):
		if not re.match("[0-9]{10}",self.conatact_no):
			raise ValidationError(_('Mobile number must be 10 digits!!!'))

	@api.constrains('email')
	def check_email(self):
		if not re.match("[^@]+@[^@]+\.[^@]+",self.email):
			raise ValidationError(_('Email Address is not valid!!!'))

	@api.multi
	def notify_user(self):
		template=self.env.ref('discount_coupon_management.session_details_changes',raise_if_not_found=False)
		print("\n\n>>>>>>>>>>>>>>>>\n\n",template)
		template.send_mail(self.id,force_send=True)

	@api.model
	def create(self,values):
		obj=super(MakeCompany,self).create(values)
		obj.notify_user()
		return obj
	# @api.one
 #    def notify_user(self):
 #    	template = self.env.ref('discount_coupon_management.session_details_changes',raise_if_not_found=False)
	# 	template.send_mail(self.id)
