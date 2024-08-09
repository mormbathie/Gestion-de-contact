from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import RegisterForm

# Create your views here.

def loginview(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/contact/')

    return render(request,'utilisateurs/login.html',{'form1':form})

def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = RegisterForm()
           
    return render(request,'utilisateurs/register.html', {'form':form})



