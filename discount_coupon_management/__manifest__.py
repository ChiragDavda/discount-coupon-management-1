# -*- coding: utf-8 -*-
{
	'name':'Discount Coupon Management',
	'version':'1',
	'summary':'Manage Discount Coupon',
	'description':"""This is description for Discount Coupon Management!!! """,
	'depends':[
	'web',],
	'data':[
		'wizard/change_coupon_detail.xml',
		'views/make_discount_view.xml',
		'views/make_company_view.xml',
		'views/new_bill.xml',
		'views/coupon_detail.xml',
		'report/coupon_detail_report.xml',
		'report/coupon_detail_report_temp.xml',
		'report/customer_detail_template.xml',
		#'report/customer_detail.xml',
		'report/wizard_action_report_coupon_detail.xml',
		'wizard/wizard_coupon_data.xml',
		#'security/ir.model.access.csv',
		],
	'demo':[],
	'qweb':[],
	'installable':True,
	'auto_install':False,
}
