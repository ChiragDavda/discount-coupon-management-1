# -*- coding: utf-8 -*-
from odoo import fields,models,api
class MakeBill(models.Model):
	_name="make.bill"
	_description="Register New Bill!!!"
	
	customer_name=fields.Char(string="Company Name:")	
	email=fields.Char(string="Email Address:")
	conatact_no=fields.Char(string="Contact Number:")
	bill_id=fields.Char(string="Bill Id:")
	amount=fields.Char(string="Amount:")