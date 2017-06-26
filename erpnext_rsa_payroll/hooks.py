# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_rsa_payroll"
app_title = "RSA Payroll"
app_publisher = "Zefa Consulting"
app_description = "Extension of the erpnext payroll system with South African requirements"
app_icon = "icon-book"
app_color = "blue"
app_email = "info@zefagroup.xyz"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_rsa_payroll/css/erpnext_rsa_payroll.css"
# app_include_js = "/assets/erpnext_rsa_payroll/js/erpnext_rsa_payroll.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_rsa_payroll/css/erpnext_rsa_payroll.css"
# web_include_js = "/assets/erpnext_rsa_payroll/js/erpnext_rsa_payroll.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpnext_rsa_payroll.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_rsa_payroll.install.before_install"
# after_install = "erpnext_rsa_payroll.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_rsa_payroll.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Salary Slip": {
 		"validate": "erpnext_rsa_payroll.rsa_payroll.paye_calculation.calculate_paye"
	}
}

fixtures = [{
	"doctype": "DocType",
            "filters": { "custom" : ["=", "1"] }
           },
    	"Custom Field",
    	"Custom Script",
    	"Property Setter",
        "Print Format"
    ]

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnext_rsa_payroll.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_rsa_payroll.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_rsa_payroll.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_rsa_payroll.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_rsa_payroll.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_rsa_payroll.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_rsa_payroll.event.get_events"
# }

