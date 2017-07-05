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
def compose(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | Compose'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/mailbox/compose.html', {'context': context})

def mailbox(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | Mailbox'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/mailbox/mailbox.html', {'context': context})

def read_mail(request, error=None, info=None, success=None, warning=None):
	context = {'title':'AdminLTE 2 | Read Mail'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'webappdemo/pages/mailbox/read-mail.html', {'context': context})