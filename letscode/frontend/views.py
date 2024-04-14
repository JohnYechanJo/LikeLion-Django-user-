from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Frontend
from django.http import HttpResponseNotFound
# Create your views here.

def home(request):
    posts = Frontend.objects.all()
    return render(request, "homepage.html", {"posts": posts})
#############################################################
def new(request):
    title=request.GET.get("title")
    content=request.GET.get("content")
    image=request.GET.get("image")
    return render(request, "postpage/newpage.html", {"title":title, "content":content})
#######################################################################################
#detailpage.html을 보여줌
def detail(request, id):
    frontend = get_object_or_404(Frontend, id = id)
    return render(request, "postpage/detailpage.html", {"frontend": frontend})
#새로운 게시물을 데이터베이스에 저장함
def create(request):
    new_frontend=Frontend()
    new_frontend.title=request.POST['title']
    new_frontend.content=request.POST['content']
    new_frontend.image=request.FILES['image']
    new_frontend.pub_date=timezone.now()
    new_frontend.save()
    return redirect("detail", new_frontend.id)
##############################################
#editpage.html을 보여줌
def edit(request, id):
    edit_frontend = get_object_or_404(Frontend, pk = id)
    return render(request, "postpage/editpage.html", {"frontend":edit_frontend})
#수정한 게시물을 데이터베이스에 적용함
def update(request, id):
    update_frontend = get_object_or_404(Frontend, pk = id)
    update_frontend.title=request.POST["title"]
    update_frontend.content=request.POST["content"]
    update_frontend.pub_date=timezone.now()
    update_frontend.save()
    return redirect("detail", update_frontend.id)
#################################################
#게시물 삭제하기
def delete(request, id):
    delete_frontend = Frontend.objects.get(id = id)
    delete_frontend.delete()
    return redirect("home")

def login(request):
    
    return render(request, "login.html")

def signup(request):
    
    return render(request, "signup.html")