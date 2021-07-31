from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'dataTables'
urlpatterns = [
    url(r'^table/$', views.table, name='table'),
]
