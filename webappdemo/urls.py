from django.conf.urls import include, url
from django.contrib import admin

import views

import dashboard
import calendar
import widgets
import charts
import tables
import examples
import ui
import mailbox
import forms_page

app_name='webappdemo'
urlpatterns = [
	url(r'^$', dashboard.index, name='dashboard'),
	url(r'^dashboard2/$', dashboard.index2, name='dashboard2'),

	url(r'^calendar/$', calendar.calendar, name='calendar'),
	url(r'^widgets/$', widgets.widgets, name='widgets'),

	##############
	### Charts ###
	##############
	url(r'^chartjs/$', charts.chartjs, name='chartjs'),
	url(r'^morris/$', charts.morrisCharts, name='morrisCharts'),
	url(r'^flot/$', charts.flotCharts, name='flotCharts'),
	url(r'^inline/$', charts.inlineCharts, name='inlineCharts'),

	################
	### Examples ###
	################
	url(r'^404/$', examples.page404, name='page404'),
	url(r'^500/$', examples.page500, name='page500'),
	url(r'^blank/$', examples.blank, name='blank'),
	url(r'^invoice/$', examples.invoice, name='invoice'),
	url(r'^invoice/print/$', examples.invoice_print, name='invoice-print'),
	url(r'^lockscreen/$', examples.lockscreen, name='lockscreen'),
	url(r'^login/$', examples.loginpage, name='login'),
	url(r'^register/$', examples.registerpage, name='register'),
	url(r'^page/$', examples.pacepage, name='pace'),
	url(r'^profile/$', examples.profile, name='profile'),

	##############
	### Forms ####
	##############

	url(r'^advanced/$', forms_page.advanced, name='advanced'),
	url(r'^editors/$', forms_page.editors, name='editors'),
	url(r'^general_forms/$', forms_page.general_forms, name='general_forms'),

	###############
	### Mailbox ###
	###############

	url(r'^compose/$', mailbox.compose, name='compose'),
	url(r'^mailbox/$', mailbox.mailbox, name='mailbox'),
	url(r'^read-mail/$', mailbox.read_mail, name='read-mail'),

	##############
	### Tables ###
	##############
	url(r'^simple/$', tables.simple, name='simple'),
	url(r'^data/$', tables.data, name='data'),

	##########
	### UI ###
	##########

	url(r'^buttons/$', ui.buttons, name='buttons'),
	url(r'^general/$', ui.general, name='general'),
	url(r'^icons/$', ui.icons, name='icons'),
	url(r'^modals/$', ui.modals, name='modals'),
	url(r'^sliders/$', ui.sliders, name='sliders'),
	url(r'^timeline/$', ui.timeline, name='timeline'),
]
