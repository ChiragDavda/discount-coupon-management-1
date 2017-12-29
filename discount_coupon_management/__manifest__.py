# -*- coding: utf-8 -*-
{
	'name':'Discount Coupon Management',
	'version':'1',
	'summary':'Manage Discount Coupon',
	'description':"""This is description for Discount Coupon Management!!! """,
	'depends':[
	'sale','sale_management'],
	'data':[
		'wizard/change_coupon_detail.xml',
		'views/make_discount_view.xml',
		'views/make_company_view.xml',
		'views/new_bill.xml',
		'views/coupon_detail.xml',
		],
	'demo':[],
	'qweb':[],
	'installable':True,
	'auto_install':False,
}
