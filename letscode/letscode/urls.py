"""
URL configuration for letscode project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from frontend import views as front
from backend import views as back

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", front.home, name="home"),
    path("<str:id>", front.detail, name="detail"),
    path("new/", front.new, name="new"),
    path("login/", back.login, name="login"),
    path("signup/", back.signup, name="signup"),
    path("create/", front.create, name="create"),
    path("edit/<str:id>", front.edit, name="edit"),
    path("update/<str:id>", front.update, name="update"),
    path("delete/<str:id>", front.delete, name="delete")
]
