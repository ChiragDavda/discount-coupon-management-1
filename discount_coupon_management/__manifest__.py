# -*- coding: utf-8 -*-
{
	'name':'Discount Coupon Management',
	'version':'1',
	'summary':'Manage Discount Coupon',
	'description':"""This is description for Discount Coupon Management!!! """,
	'depends':[
	'web','mail'],
	'data':[
		'security/account_security.xml',
		'security/ir.model.access.csv',
		'wizard/change_coupon_detail.xml',
		'views/make_discount_view.xml',
		'views/make_company_view.xml',
		'views/new_bill.xml',
		'views/email_templates.xml',
		'views/coupon_detail.xml',
		'report/coupon_detail_report.xml',
		'report/coupon_detail_report_temp.xml',
		'report/customer_detail_template.xml',
		'report/wizard_action_report_coupon_detail.xml',
		'wizard/wizard_coupon_data.xml',
		'wizard/change_coupon_item.xml'
		],
	'demo':[
		'demo/discount_coupon.xml',
	],
	'qweb':[],
	'installable':True,
	'auto_install':False,
}
