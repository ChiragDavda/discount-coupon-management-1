# -*- coding: utf-8 -*-
import re
from odoo import fields,models,api,_
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
class MakeCompany(models.Model):
	_name="make.company"
	_description="Register New Company!!!"
	
	name=fields.Char(string="Company Name:")
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
