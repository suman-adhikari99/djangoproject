from django import forms
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from .models import Post, Document,Comment, employee, form


class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=('title','text')

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields= ['title','document']


class Subscribe(forms.Form):
    Email=forms.EmailField()
    #name=forms.CharField(max_length=29)
    #chooseFile=forms.FileField()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')
class employeeform(forms.ModelForm):
    class Meta:
        model= employee
        fields= ('name','position','address')