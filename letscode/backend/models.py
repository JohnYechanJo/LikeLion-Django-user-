from django.db import models

# Create your models here.
class Backend(models.Model):
    id=models.CharField(max_length=200)
    pw=models.CharField(max_length=200)
    pw_check=models.CharField(max_length=200)
    def __str__(self):
        return self.id
    
