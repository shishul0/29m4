from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse
from .forms import ExtendedUserCreationForm

def my_login(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'app_auth/login.html')
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is None:
        return render(request, 'app_auth/login.html', {"error": "Пользователь не найден"})
    
    login(request, user)
    return redirect(reverse("main-page"))

def my_logout(request: WSGIRequest):
    logout(request)
    return redirect(reverse("login"))

def my_register(request: WSGIRequest):
    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=request.POST['password1'])
            login(request, user=user)
            return redirect(reverse('profile'))
    else:
      form = ExtendedUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'app_auth/register.html', context)

def my_profile(request: WSGIRequest):
    return render(request, 'app_auth/profile.html')
