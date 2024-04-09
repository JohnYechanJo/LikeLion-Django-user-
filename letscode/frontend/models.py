from django.db import models

# Create your models here.
class Frontend(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField()
    content=models.TextField()
    date=models.DateTimeField()
    def __str__(self):
        return self.title
    def date(self):
        return self.date