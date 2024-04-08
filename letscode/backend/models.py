from django.db import models

# Create your models here.
class Backend(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField()
    content=models.TextField()
    date=models.DateTimeField()
    def __str__(self):
        return self.title
    
class Comment(models.Model, Backend):
    def __init__(self, title):
        self.title=title
    comment=models.TextField()
    def __str__(self):
        return self.title, self.comment