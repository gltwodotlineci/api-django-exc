from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser

def home(request):
    return render(request, 'origin/home.html', {})

def test(request):
    return render(request, 'rand/random.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('../api/api-games')
        else:
            #messages.success(request, ("Erreur de nom ou de mdp"))
            return redirect('login')
    elif request.method == 'GET':
        return render(request, 'origin/login.html', {})

def logout_user(request):
    logout(request)
    #messages.success(request, ("Vous vous êtes déconnectez"))
    return redirect('home')

