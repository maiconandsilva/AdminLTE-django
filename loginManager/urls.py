from django.conf.urls import include, url
from django.contrib import admin

import views

app_name='loginManager'
urlpatterns = [
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^register/$', views.user_register, name='user_register'),
    url(r'^login/auth/$', views.login_user, name='login_user'),
    url(r'^user/check/$', views.check_userExists, name='check_user'),
    url(r'^register/user/$', views.register_user, name='register_user'),
    url(r'^forget/$', views.forget_user, name='forget_user'),
    url(r'^forgot/$', views.forgot_username, name='forgot_user'),
]
