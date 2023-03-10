from django.urls import reverse

from .models import *
from django.shortcuts import render, redirect
from rest_framework.response import Response


def log_in(request):
    if 'username' in request.session:
        return redirect(reverse('observer:home'))
    else:
        if request.method == "POST":

            u_name = request.POST['username']
            p_word = request.POST['password']

            try:
                user = User.objects.get(username=u_name)
            except:
                request.session.clear()
                return redirect(reverse('login'))

            if user.username == u_name and user.password == p_word and user.admin == True:
                create_session(request, u_name)
                return redirect(reverse('observer:home'))

    return render(request, 'login.html')


def create_session(request, username):
    request.session['username'] = username


def delete_session(request):
    request.session.flush()
    request.session.clear_expired()
    return redirect(log_in)


def logout_request(request):
    delete_session(request)
    return redirect(log_in)
