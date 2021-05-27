
from os import name
from django.utils import timezone

from django.http import HttpResponse
from .models import Post,form,Comment
from django import forms
from .forms import PostForm, DocumentForm,Subscribe,Comments
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


#def post_detail(request,pk):
   # post=Post.objects.get(pk=pk)
    #return render(request,'post_detail.html',{'post':post})

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




# added for django mail sending   
from firstproject.settings import EMAIL_HOST_USER
from django.core.mail import message, send_mail, send_mass_mail
import imghdr

def subscribe(request):
    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST,request.FILES)
        subject = 'Welcome to Achievers Group'
        message = 'You are viewing demo'
        recepient = str(sub['Email'].value())
           
        print(recepient)
        send_mail(subject,message,EMAIL_HOST_USER,[recepient], fail_silently = False)
        if sub.is_valid():
            name=sub.cleaned_data['name']
            email=sub.cleaned_data['Email']
            file=sub.cleaned_data['chooseFile']
            #print(name)
            #print(email)
            print(file)
            form1=form(email=email, name=name,file=file)
            form1.save()
        return render(request,'success.html',{'recepient': recepient})
       
        
    return render(request, 'email.html', {'form':sub})
   
def fetch(request):
    sub=Subscribe()
    if request.method == 'POST':
        sub=Subscribe(request.POST)
        if sub.is_valid():
            name=sub.cleaned_data['name']
            email=sub.cleaned_data['Email']
            #print(name)
            #print(email)
            form1=form(email=email, name=name)
            form1.save()
    
        
    return render(request, 'email.html', {'form':sub})



def mailmass(request):
    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        recepient = str(sub['Email'].value())
        message1 = ('Subject here', 'Here is the message', EMAIL_HOST_USER, [recepient])
        message2 = ('Another Subject', 'Here is another message', EMAIL_HOST_USER, [recepient])
        send_mass_mail((message1, message2), fail_silently=False)
        
        print(recepient)
        #send_mail(subject,message,EMAIL_HOST_USER,[recepient], fail_silently = False)
        return render(request,'success.html',{'recepient': recepient})
    return render(request, 'email.html', {'form':sub})



from django.core.mail import EmailMessage
def attach(request):
    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        subject = 'Welcome to Achievers Group'
        message = 'You are viewing demo'
        recepient = str(sub['Email'].value())
        print(recepient)
        file=open('D:/djangoproject/blog/templates/attach.html').read()
       
        #send_mail(subject,message,EMAIL_HOST_USER,[recepient], fail_silently = False)
        email = EmailMessage('Hello', file, EMAIL_HOST_USER, [recepient])
        email.content_subtype='html'
        with open('D:/Pictures/zMessenger_Lite/53395e8f1a1b188101ed33305b241c23.0.jpg','r',encoding='Latin-1') as attachfile:
            image_name= attachfile.name
            image_type=imghdr.what(attachfile.name)
            image_data=attachfile.read()
            email.attach('suman',image_data)  # may be because of this line, when i send mail and open it 'no preview' issue is occur. 
        #email.attach_file('D:/Pictures/zMessenger_Lite/53395e8f1a1b188101ed33305b241c23.0.jpg')
        email.send()
    
    
    
def post_detail(request,pk):
    post=get_list_or_404(Post,pk=pk)
    comments=post.comments.filter(active=True)
    new_comment= None

    if request.method=='POST':
        comment_form=Comments(request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()

        else:
            comment_form=comments()
        return render(request,'post_detail.html',{'post':post, 'comments':comments, 'new_comment':new_comment})

    
    
    

       # return render(request,'success.html',{'recepient': recepient})
    # render(request, 'email.html', {'form':sub})