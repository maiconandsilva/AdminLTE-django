from django.conf.urls import include, url
from django.contrib import admin

import views

app_name='fileUpload'
urlpatterns = [
	url(r'^uploadFiles/$', views.uploadFiles, name='upload_files'),

]
