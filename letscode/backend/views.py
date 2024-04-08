from django.shortcuts import render, get_object_or_404
from .models import Backend
# Create your views here.

# Create your views here.
def home(request):
    post = Backend.objects.all()
    return render(request, "homepage.html")

def new(request):
    return render(request, "newpage.html")

def detail(request, id):
    
    return render(request, "detailpage.html")

def login(request):
    
    return render(request, "login.html")

def signup(request):
    
    return render(request, "signup.html")