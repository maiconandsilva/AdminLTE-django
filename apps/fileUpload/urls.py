from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'fileUpload'
urlpatterns = [
    url(r'^uploadFiles/$', views.uploadFiles, name='upload_files'),

]
