# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core import serializers
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import apps.adminLteDjango


# Create your views here.
def widgets(request, error=None, info=None, success=None, warning=None):
    context = { 'title': 'AdminLTE 2 | Widgets' }
    if error:
        context['error'] = str(error)
    if info:
        context['info'] = str(info)
    if warning:
        context['warning'] = str(warning)
    if success:
        context['success'] = str(success)
    return render(request, 'webappdemo/pages/widgets.html', { 'context': context })
