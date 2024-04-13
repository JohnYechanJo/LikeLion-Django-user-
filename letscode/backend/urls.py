from django.contrib import admin
from django.urls import path
from django.http import HttpResponseNotFound
from backend import views as back


urlpatterns = [
    path("login/", back.login, name="login"),
    path("signup/", back.signup, name="signup"),
    
    path('favicon.ico', lambda request: HttpResponseNotFound()),
]