from django.shortcuts import render,redirect
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from accounts.decorators import unauthenticated_user, allowed_users
# Create your views here.
@login_required(login_url='login')
def startup(request):
    context = {
        'name' : request.user.username,
    }
    return render(request,'startup-page.html',context)

@login_required(login_url='login')
def dashboard(request):
    user = request.user
    group = request.user.groups.all()[0].name
    x = 'dashboard-te.html'
    if group == "trainers":
        x = 'dashboard-tr.html'
    return render(request,x)

@login_required(login_url='login')
def explore(request):
    return render(request,'explore.html')

@login_required(login_url='login')
def newsfeed(request):
    return render(request,'newsfeed.html')

