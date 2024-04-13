from django.db import models

# Create your models here.
class Frontend(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="blog/", blank=True, null=True)
    content=models.TextField()
    pub_date=models.DateTimeField()

    def __str__(self):
        return self.title
    def summary(self):
        return self.content[:100]
