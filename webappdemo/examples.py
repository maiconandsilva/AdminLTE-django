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
def page404(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | 404 Error Page'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/examples/404.html', {'context': context})

def page500(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | 500 Error Page'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/examples/500.html', {'context': context})

def blank(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | Blank Page'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/examples/blank.html', {'context': context})

def invoice(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | Invoice'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/examples/invoice.html', {'context': context})

def invoice_print(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | Invoice'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/examples/invoice-print.html', {'context': context})

def lockscreen(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | Lockscreen'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/examples/lockscreen.html', {'context': context})

def loginpage(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | Login'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/examples/login.html', {'context': context})

def registerpage(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | Register'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/examples/register.html', {'context': context})

def pacepage(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | Pace Page'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/examples/pace.html', {'context': context})

def profile(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | Profile'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/examples/profile.html', {'context': context})
