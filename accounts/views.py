from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here
from .models import *
from .forms import CreateUserForm

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('profile')
            else:
                messages.info(request,'Username OR password is incorrect')
        context = {}
        return render(request,'accounts/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('loginPage')
def signupPage(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for ' + user)
                return redirect('loginPage')
        context = {'form': form}
        return render(request,'accounts/signup.html',context)

@login_required(login_url='loginPage')
def profile(request):
    context = {}
    return render(request,'accounts/profile.html',context)
