from django.contrib import admin
from .models import Document, Post,Companies, Person 
admin.site.register(Post)

# Register your models here.

admin.site.register(Document)
admin.site.register(Companies)
admin.site.register(Person )