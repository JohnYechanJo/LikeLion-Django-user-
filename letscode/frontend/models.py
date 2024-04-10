from django.db import models

# Create your models here.
class Frontend(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField()
    content=models.TextField()
    def __str__(self):
        return self.title
    def __str__(self):
        return self.date
