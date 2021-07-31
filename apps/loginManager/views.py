from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core import serializers
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.conf import settings

from .forms import *
from . import utils


# Create your views here.
def user_login(request, error=None, info=None, success=None, warning=None):
    context = { 'title': 'AdminLTE 2 | Login' }
    logout(request)
    if error:
        context['error'] = str(error)
    if info:
        context['info'] = str(info)
    if warning:
        context['warning'] = str(warning)
    if success:
        context['success'] = str(success)
    return render(request, 'app/loginManager/login.html', { 'context': context, 'loginForm': LoginPage })


def user_register(request, error=None, info=None, success=None, warning=None, form=None):
    context = { 'title': 'AdminLTE 2 | Register' }
    if error:
        context['error'] = str(error)
    if info:
        context['info'] = str(info)
    if warning:
        context['warning'] = str(warning)
    if success:
        context['success'] = str(success)
    if form:
        return render(request, 'app/loginManager/register.html',
                      { 'context': context, 'registerForm': RegisterPage, 'form': form })
    return render(request, 'app/loginManager/register.html', { 'context': context, 'registerForm': RegisterPage })


def login_user(request):
    error = None
    if request.method == 'POST':
        form = LoginPage(request.POST)
        if form.is_valid():
            error = "valid"
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if form.cleaned_data['remember_me']:
                    settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
                return HttpResponseRedirect(reverse('dataTables:table'))
            else:
                error = "User doesn't exist or invalid password"
        else:
            error = "Form isn't valid"
    return user_login(request, error)


def check_userExists(request):
    if request.method == 'POST':
        reg_username = utils.check_post(request, 'username').lower()
        if User.objects.filter(username=reg_username).exists():
            return HttpResponse("false")
        else:
            return HttpResponse("true")


# TODO: send New User email congrats on signing up
def register_user(request):
    if request.method == 'POST':
        form = RegisterPage(request.POST)
        if form.is_valid():
            error = "valid"
            reg_email = form.cleaned_data['reg_email']
            reg_username = form.cleaned_data['reg_username'].lower()
            reg_password = form.cleaned_data['reg_password']
            user = User.objects.create_user(reg_username, reg_email, reg_password)
            user.save()
            return user_login(request, None, None, "Sign in!")
        else:
            return user_register(request, form=form)
    else:
        error = "Something went horribly wrong"
        return user_login(request, error)


def forget_user(request):
    if request.method == 'POST':
        form = ForgetPage(request.POST)
        if form.is_valid():
            error = "valid"
            forget_email = form.cleaned_data['forget_email']
            forget_username = form.cleaned_data['forget_username']
            user = User.objects.get(email=forget_email, username=forget_username)
            if user:
                npassword = utils.random_strgen()
                user.set_password(npassword)
                user.save()
                from_email = "Mailgun Support Email  <support@domain.com>"
                to_email = forget_email
                sub = "Your password has been reset"
                msg = "Your new password is " + npassword
                utils.send_simple_message(from_email, to_email, sub, msg)
                return user_login(request, None, "Check your email")
            else:
                error = "Username doesn't exist or email doesn't exist"
                return user_login(request, error)
        else:
            error = "Form isn't valid"
            return user_login(request, error)
    else:
        error = "Something went horribly wrong"
        return user_login(request, error)


def forgot_username(request):
    if request.method == 'POST':
        form = ForgotPage(request.POST)
        if form.is_valid():
            error = "valid"
            forget_email = form.cleaned_data['forgot_email']
            user = User.objects.get(email=forget_email)
            if user:
                from_email = "Mailgun Support Email  <support@domain.com>"
                to_email = forget_email
                sub = "Hey got your username"
                msg = "Your username is " + user.username
                utils.send_simple_message(from_email, to_email, sub, msg)
                return user_login(request, None, "Check your email")
            else:
                error = "User doesn't exist"
                return user_login(request, error)
        else:
            error = "Form isn't valid"
            return user_login(request, error)
    else:
        error = "Something went horribly wrong"
        return user_login(request, error)
