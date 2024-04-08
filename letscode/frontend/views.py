from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "homepage.html")

def new(request):
    return render(request, "newpage.html")

def detail(request, id):
    
    return render(request, "detailpage.html")

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")
