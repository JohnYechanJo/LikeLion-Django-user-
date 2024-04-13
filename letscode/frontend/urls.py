from django.contrib import admin
from django.urls import path
from django.http import HttpResponseNotFound
from frontend import views as front


urlpatterns = [
    path("<str:id>", front.detail, name="detail"),
    path("new/", front.new, name="new"),
    path("create/", front.create, name="create"),
    path("edit/<str:id>", front.edit, name="edit"),
    path("update/<str:id>", front.update, name="update"),
    path("delete/<str:id>", front.delete, name="delete"),
    
    path('favicon.ico', lambda request: HttpResponseNotFound()),
]