from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog,Post
# Create your views here.

def index(request):
    #blog = Blog.objects.all() 
    posts = Post.objects.all()

    posts = {'posts' : posts,}

    
    return render(request,'index.html',posts)