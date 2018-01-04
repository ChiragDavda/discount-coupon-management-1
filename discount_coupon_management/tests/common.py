#-*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase
class Common(TransactionCase):

	def setUp(self):
		super(Common,self).setUp()
		#self.make_company1=self.env['make.company']
		#print(self.make_company1)
		self.make_company1=self.env['make.company'].create({'name':'Streboo','address':'Ahmedabad','email':'streboo@gmail.com','conatact_no':'0792524261','licence_no':'AAAA12q'})
		self.make_coupon1=self.env['make.discount.coupon'].create({'company_name':self.make_company1.id,'coupon_title':'Summer Sale','customer_name':'Chirag','coupon_bunch':'100','coupon_type':'seasson','start_date':'2018-01-01','valid_date':'2018-01-01','offer':'20% off.'})
		self.coupon_detail=self.env['coupon.detail'].create({'company_name':self.make_company1.id,'coupon_id':'P1','type_coupon':'seasson','valid_to':'2018-02-01','coupon_title':'Summer Sale','redeem':False,'start_from':'2018-01-01'})
		self.make_bill=self.env['make.bill'].create({'customer_name':'Chirag','email':'chirag@gmail.com','conatact_no':'9558264679','coupon_code':'P1','bill_id':'11','amount':'1500'})
		# self.a=50
		# a=60
		# print(self.a)
		# print(a)
		# print(self.a)
		# self.b=""
		# self.c=False
	# def test(self):
	# 	pass
	# def test_01_second(self):
	# 	print(str(self.a)+":"+self.b+":"+str(self.c))
	# 	print("\n\n\nSecond Function!!!!")
	# 	self.a=2
	# 	self.b="2"
	# 	self.c=False
	# 	print(str(self.a)+":"+self.b+":"+str(self.c))

	# def test_00_first(self):
	# 	print(str(self.a)+":"+self.b+":"+str(self.c))
	# 	print("\n\n\nFirst Function!!!!")
	# 	self.a=1
	# 	self.b="1"
	# 	self.c=True
	# 	print(str(self.a)+":"+self.b+":"+str(self.c))