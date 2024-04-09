

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Frontend
# Create your views here.

def home(request):
    post = Frontend.objects.all()
    return render(request, "homepage.html")

def new(request):
    return render(request, "newpage.html")

def detail(request, id):
    content = get_object_or_404(Frontend, pk = id)
    return render(request, "detailpage.html", {"content": content})

def login(request):
    
    return render(request, "login.html")

def signup(request):
    
    return render(request, "signup.html")

def create(request):
    new_content=Frontend()
    new_content.title=request.POST['title']
    new_content.image=request.POST['image']
    new_content.content=request.POST['content']
    new_content.date=request.POST['date']
    new_content.pub_date=timezone.now()
    new_content.save()
    return redirect("detail", new_content.id)