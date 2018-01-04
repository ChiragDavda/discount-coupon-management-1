#-*- coding: utf-8 -*-
from . import common
from datetime import datetime
class check_date(Exception):
	pass
class TestBillDetail(common.Common):
	def test_check_phone_no(self):
		self.make_bill.check_phone_no()

	def test_check_email(self):
		self.make_bill.check_email()

	def test_name(self):
		self.assertNotEquals(self.make_bill.customer_name,"","Value will not be empty!!!")

	def test_date(self):
		
		
		try:
			if self.make_coupon1.valid_date<datetime.now().date().strftime('%Y-%m-%d'):
				raise check_date
		except check_date:
			print("\n\n\n!!!!!!Date is invalid!!!!\n\n")