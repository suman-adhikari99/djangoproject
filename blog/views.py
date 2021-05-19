
from django.utils import timezone

from django.http import HttpResponse
from .models import Post
from django import forms
from .forms import PostForm
from django.shortcuts import redirect, render, get_list_or_404

# Create your views here.



def post_list(request):
    posts=Post.objects.all()
    return render(request, 'post_list.html',{'posts':posts})
def post_detail(request,pk):
    post=Post.objects.get(pk=pk)
    return render(request,'post_detail.html',{'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()    
            return redirect('post_list')
            
    else:
         form = PostForm()
    return render(request, 'post_new.html', {'form':form})
            

    

   
