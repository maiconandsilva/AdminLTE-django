from django.conf.urls import include, url
from django.contrib import admin

import views

app_name='webappdemo'
urlpatterns = [
	url(r'^$', views.index, name='dashboard'),
	url(r'^dashboard2/$', views.index2, name='dashboard2'),

	url(r'^calendar/$', views.calendar, name='calendar'),
	url(r'^widgets/$', views.widgets, name='widgets'),

	##############
	### Charts ###
	##############
	url(r'^chartjs/$', views.chartjs, name='chartjs'),
	url(r'^morris/$', views.morrisCharts, name='morrisCharts'),
	url(r'^flot/$', views.flotCharts, name='flotCharts'),
	url(r'^inline/$', views.inlineCharts, name='inlineCharts'),
	
	##############
	### Tables ###
	##############
	url(r'^simple/$', views.simple, name='simple'),
	url(r'^data/$', views.data, name='data'),
]
