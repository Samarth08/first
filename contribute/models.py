from django.db import models

# Create your models here.
class SignUp(models.Model):
    title = models.CharField(max_length=200, blank=False, null=True)
    body = models.TextField(max_length=2000, blank=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __unicode__(self):
        return self.body

 
