from django.contrib import admin
from .models import Backend
from .models import Comment
# Register your models here.
admin.site.register(Backend)
admin.site.register(Comment)