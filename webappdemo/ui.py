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
def buttons(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | Buttons'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/UI/buttons.html', {'context': context})

def general(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | General'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/UI/general.html', {'context': context})

def icons(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | Icons'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/UI/icons.html', {'context': context})

def modals(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | Modals'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/UI/modals.html', {'context': context})

def sliders(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | Sliders'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/UI/sliders.html', {'context': context})

def timeline(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | Timeline'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/UI/timeline.html', {'context': context})