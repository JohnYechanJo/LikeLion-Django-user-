from django.contrib import admin
from django.urls import path
from django.http import HttpResponseNotFound
from frontend.views import *


urlpatterns = [
    path("<str:id>", detail, name="detail"),
    #생성
    path("new/", new, name="new"),
    path("create/", create, name="create"),
    #수정
    path("edit/<str:id>", edit, name="edit"),
    path("update/<str:id>", update, name="update"),
    #삭제
    path("delete/<str:id>", delete, name="delete"),
    #유저
    path("login/", login, name="login"),
    path("signup/", signup, name="signup"),
    
    path('favicon.ico', lambda request: HttpResponseNotFound()),
]