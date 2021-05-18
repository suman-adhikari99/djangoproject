from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
posts= [
    {
    'author':'suman',
    'title':"blog-post1",
    'content':'firts post content',
    'date-posted':'dec-20'
},
{
    'author':'susmita',
    'title':"blog-post2",
    'content':'second post content',
    'date-posted':'dec-21'
}
]
def home(request):
    contex={
        'posts':posts
    }
    return render(request,'index.html',contex, )

def post_list(request):
    posts=Post.objects.all()
    return render(request, 'post_list.html',{'posts':posts})
def post_detail(request,pk):
    post=Post.objects.get(pk=pk)
    return render(request,'post_detail.html',{'post':post})