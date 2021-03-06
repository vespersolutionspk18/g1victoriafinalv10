# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "g1victoria"
app_title = "g1victoria"
app_publisher = "Vesper Solutions "
app_description = "g1victoria ERP"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "vespersolutionspk@gmail.com"
app_license = "Vesper Solutions"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/g1victoria/css/g1victoria.css"
# app_include_js = "/assets/g1victoria/js/g1victoria.js"

# include js, css files in header of web template
# web_include_css = "/assets/g1victoria/css/g1victoria.css"
# web_include_js = "/assets/g1victoria/js/g1victoria.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "g1victoria/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
#home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "g1victoria.install.before_install"
# after_install = "g1victoria.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "g1victoria.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"g1victoria.tasks.all"
# 	],
# 	"daily": [
# 		"g1victoria.tasks.daily"
# 	],
# 	"hourly": [
# 		"g1victoria.tasks.hourly"
# 	],
# 	"weekly": [
# 		"g1victoria.tasks.weekly"
# 	]
# 	"monthly": [
# 		"g1victoria.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "g1victoria.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "g1victoria.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "g1victoria.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]
