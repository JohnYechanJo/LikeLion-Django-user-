from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Backend
# Create your views here.

def login(request):
    
    return render(request, "login.html")

def signup(request):
    
    return render(request, "signup.html")

def create(request):
    new_user = Backend()
    new_user.user_id=request.POST['id']
    new_user.user_pw=request.POST['pw']
    new_user.user_pw_check=request.POST['pw_check']
    new_user.save()
    return redirect('login')