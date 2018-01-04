#-*- coding: utf-8 -*-
from . import common
class TestMakeCoupon(common.Common):
	def test_date(self):
		self.make_coupon1.check_valid_date()
		print(self.make_coupon1)
	def test_type_date(self):
		self.make_coupon1.check_date()


	def test_name(self):
		self.assertNotEquals(self.make_coupon1.customer_name,"","Value will not be empty!!!")

	# def test_name1(self):
	# 	self.assertNotIn(self.make_coupon1.coupon_bunch,[50,100,200,300,400,500],"Value will be 50 100 200 300 400 500!!")

