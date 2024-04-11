from django.db import models

# Create your models here.
class Backend(models.Model):
    user_id=models.CharField(max_length=200)
    user_pw=models.CharField(max_length=200)
    user_pw_check=models.CharField(max_length=200)

    def __str__(self):
        return self.id
    
