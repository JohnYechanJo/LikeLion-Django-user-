from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Frontend
# Create your views here.

def home(request):
    post = Frontend.objects.all()
    return render(request, "homepage.html", {"post": post})

def new(request):
    title=request.GET.get("title")
    content=request.GET.get("content")
    return render(request, "postpage/newpage.html", {"title":title, "content":content})

def detail(request, id):
    frontend = get_object_or_404(Frontend, pk = id)
    title=request.GET.get("title")
    content=request.GET.get("content")
    return render(request, "postpage/detailpage.html", {"frontend": frontend, "title":title, "content":content})

def create(request):
    new_frontend=Frontend()
    new_frontend.title=request.POST['title']
    new_frontend.content=request.POST['content']
    new_frontend.save()
    return redirect("detail", new_frontend.id)

def edit(request, id):
    edit_frontend = get_object_or_404(Frontend, pk = id)
    return render(request, "postpage/editpage.html", {"edit_frontend":edit_frontend})

def update(request, id):
    update_frontend = get_object_or_404(Frontend, pk = id)
    update_frontend.title=request.POST["title"]
    update_frontend.content=request.POST["content"]
    update_frontend.save()
    return redirect("detail", update_frontend.id)

def delete(request, id):
    delete_frontend = Frontend.objects.get(id = id)
    delete_frontend.delete()
    return redirect("home")