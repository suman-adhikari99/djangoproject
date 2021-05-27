from django.conf import settings
from django.db.models.deletion import CASCADE
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


class form(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=29,default="")
    file=models.FileField(upload_to='images/',default="")

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='Comments')
    name=models.CharField(max_length=20)
    email=models.EmailField()
    body=models.CharField(max_length=1000) 
    created_on =models.DateField(timezone.now)
    active=models.BooleanField(default=True)

    class meta:
        ordering=['created_on']

    def __str__(self):
        return 'comment() by {}'.format(self.body,self.name)

