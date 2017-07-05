from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout

from .models import *

# Create your views here.
def table(request):
	context = {'title':'Home'}
	#get_demo = AES_Tracking_Summary.objects.all()
	#context['demoItems'] = serializers.serialize('json', get_demo)
	return render(request, 'app/dataTables/table.html', {'context': context})