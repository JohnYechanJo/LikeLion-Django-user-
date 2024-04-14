from django.urls import path
from django.http import HttpResponseNotFound
from .views import *

urlpatterns = [
    #유저
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="signup"),

]