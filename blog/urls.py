from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
  
    #path('post/new/post/new/',views.post_list, name="post_new"),
    path('post/new/',views.post_new, name="post_new"),
    path('file_upload/' , views.upload, name="upload"),
    path('email/' , views.subscribe, name="subscribe"),
    path('mailmass/' , views.mailmass, name="mailmass"),
    path('attach/' , views.attach, name="attach"),
    path('form/' , views.fetch, name="form"),



]
