from django.db import models

# Create your models here.

class art(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    picture= models.FileField(upload_to='media/')



    def __str__(self):
        return self.title

