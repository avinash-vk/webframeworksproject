from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog,Post
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from accounts.decorators import unauthenticated_user, allowed_users


@login_required(login_url='login')
@allowed_users(allowed_roles=['trainers'])
def index(request):
    #blog = Blog.objects.all() 
    posts = Post.objects.all()

    posts = {'posts' : posts,}

    return render(request,'index.html',posts)

