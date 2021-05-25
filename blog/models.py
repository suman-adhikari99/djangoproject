from django.conf import settings
from django.utils import timezone
from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class Document(models.Model):
    title = models.CharField(max_length=30)
    document = models.FileField(upload_to='images/')
    uploaded_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title


       

