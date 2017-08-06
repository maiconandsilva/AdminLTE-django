from django.shortcuts import render
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout

from .models import *

import json
import logging
import hashlib
import io

def file_exists_check(file_to_check):
	hashToCheck = hashlib.md5(file_to_check).hexdigest()
	if File_Hashes.objects.filter(hash = hashToCheck).exists():
		return True, hashToCheck
	else:
		return False, hashToCheck

# For Now, uploads files as base64 to sqlite db
def uploadFiles(request):
	if request.method == 'POST':
		for filename, file_to_check in request.FILES.iteritems():
			file_name = request.FILES[filename].name
			file_contents = file_to_check.read()
			file_converted = io.BytesIO(file_contents).getvalue()
			file_checked, hash_found = file_exists_check(file_converted)
			if not file_checked:
				#file_name = "/where You Would Define Server Path to Save File/" + file_name
				file_to_check.seek(0)
				#with open(file_name,'wb+') as destination:
				#	for chunk in file_to_check.chunks():
				#		destination.write(chunk)
				#data_row = File_Hashes(file_name=file_name,hash=hash_found)
				data_row = File_Hashes(file_name=file_name, file=file_converted, hash=hash_found, user=request.user)
				data_row.save()
		return HttpResponseRedirect('/')