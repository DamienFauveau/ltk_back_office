from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import LoginForm
from .models import UserProfile


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:login"))


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("artworks:artworks_list"))
    elif 'username' in request.POST and 'password' in request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next') is not None:
                    return redirect(request.GET['next'])
                else:
                    return HttpResponseRedirect(reverse("artworks:artworks_list"))
            else:
                return render(
                    request,
                    'users/login.html',
                    {
                        "auth_error": True,
                        'form':form,
                    }
                )
    else:
        form = LoginForm()
        return render(
            request,
            'users/login.html',
            {
                'form':form,
            }
        )