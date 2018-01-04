#-*- coding: utf-8 -*-
from . import common
class TestMakeCompany(common.Common):

	def test_email_address(self):
		self.make_company1.check_email()

	def test_phone_no(self):
	 	self.make_company1.check_phone_no()

	def test_name(self):
		self.assertNotEquals(self.make_company1.name,"","Value will not be empty!!!")