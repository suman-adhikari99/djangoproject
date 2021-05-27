from django.contrib import admin
from .models import Document, Post,form,Comment
admin.site.register(Post)

# Register your models here.

admin.site.register(Document)
admin.site.register(form)
admin.site.register(Comment)

