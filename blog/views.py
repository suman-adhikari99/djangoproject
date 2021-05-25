
from django.utils import timezone

from django.http import HttpResponse
from .models import Post,Person ,Companies,email
from django import forms
from .forms import PostForm, DocumentForm,Subscribe
from django.shortcuts import redirect, render, get_list_or_404
from django.core.paginator import Paginator , PageNotAnInteger

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    # print(paginator.num_pages)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
        # print(posts)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return render(request, 'post_list.html', {'page':page, 'posts':posts})


#def post_list(request):
 #   posts=Post.objects.all()
#    return render(request, 'post_list.html',{'posts':posts})


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
            
def upload(request):
    if request.method=="POST":
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form=DocumentForm()
    return render(request, 'form_upload.html',{'form':form})


    
from firstproject.settings import EMAIL_HOST_USER
from django.core.mail import message, send_mail

def subscribe(request):
    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        subject = 'Welcome to Achievers Group'
        message = 'You are viewing demo'
        recepient = str(sub['Email'].value())
        print(recepient)
        send_mail(subject,message,EMAIL_HOST_USER,[recepient], fail_silently = False)
        return render(request,'success.html',{'recepient': recepient})
    return render(request, 'email.html', {'form':sub})
   
