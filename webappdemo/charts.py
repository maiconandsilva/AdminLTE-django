# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core import serializers
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import templateholder

# Create your views here.
def chartjs(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | ChartJS'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/charts/chartjs.html', {'context': context})

def morrisCharts(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | Morris Charts'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/charts/morris.html', {'context': context})

def flotCharts(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | Flot Charts'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/charts/flot.html', {'context': context})

def inlineCharts(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | Inline Charts'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/charts/inline.html', {'context': context})