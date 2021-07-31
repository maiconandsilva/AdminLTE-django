from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from apps.fileUpload.models import *


# Create your views here.
@login_required
def table(request):
    context = { 'title': 'Home' }
    # get_demo = YourModel.objects.all()
    # context['demoItems'] = serializers.serialize('json', get_demo)
    get_demo = File_Hashes.objects.defer('file')
    usernames = User.objects.filter(pk__in=get_demo.values('user'))
    print(get_demo)
    context['demoItems'] = serializers.serialize('json', get_demo, fields=('file_name', 'user', 'hash'))
    context['usernames'] = serializers.serialize('json', usernames, fields=('pk', 'username'))
    return render(request, 'app/dataTables/table.html', { 'context': context })
