
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate,login,logout)
from .forms import RegisterForm
from django.contrib.auth.forms import (PasswordChangeForm)
# Password changed user stays logged in, so this will provided by update_session_auth_hash
from django.contrib.auth import (update_session_auth_hash)
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = RegisterForm()
    return render(request,'register.html',{'form': form})



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('/')
    return render(request,'login.html')



def logout_user(request):
    logout(request)
    return redirect('/login/')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Password changed successfully')
            return redirect('/')
           
            # return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'change_password.html',{'form': form})