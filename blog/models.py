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


        #TODAY's workl

class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    movie = (
        ('S', 'Sahoo'),
        ('M', 'me tera hero'),
        ('L', 'Laal killa'),
    )
    Movie = models.CharField(max_length=1, choices=movie, default="sahoo")

    def __str__(self):
        return self.name

class Companies(models.Model):
    title = models.CharField(max_length=20)
    description=models.CharField(max_length=10)
    person= models.ForeignKey(Person,related_name='persons',on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class email(models.Model):
    email=models.EmailField()