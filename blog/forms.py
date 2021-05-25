from django import forms
from django.db.models import fields
from django.db.models.base import Model
from .models import Post, Document


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
