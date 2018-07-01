from django.shortcuts import render
from django.http import HttpResponseRedirect
from users.models import Authuser
from django.contrib.auth import authenticate, login, logout


def signup(request):
    if request.method == 'GET':
        return render(request, 'users/signup.html', {})

    if request.method == 'POST':
        data = request.POST
        user = Authuser.save(data)
    return HttpResponseRedirect('/home/videos')


def auth_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user)
            print 'redirecting..........'
            return HttpResponseRedirect('/home/upload')
    if request.user.is_authenticated():
        return HttpResponseRedirect('home/upload')

    return render(request, 'users/login.html', {})


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('home/videos/')