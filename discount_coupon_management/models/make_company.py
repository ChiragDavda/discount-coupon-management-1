# -*- coding: utf-8 -*-
from odoo import fields,models,api
class MakeCompany(models.Model):
	_name="make.company"
	_description="Register New Company!!!"
	
	company_name=fields.Char(string="Company Name:")	
	address=fields.Text(string="Address:")
	email=fields.Char(string="Email Address:")
	conatact_no=fields.Char(string="Contact Number:")
	licence_no=fields.Char(string="Licene Number:")
