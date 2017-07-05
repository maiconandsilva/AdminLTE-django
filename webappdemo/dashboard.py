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
def index(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | Dashboard'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str()
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/adminLTE_contentWrapper.html', {'context': context})

def index2(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | Dashboard 2'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str()
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/index2.html', {'context': context})