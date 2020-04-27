from django.shortcuts import render,redirect
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Bio
from .decorators import unauthenticated_user, allowed_users
<<<<<<< HEAD
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

def formstart(request):
    return render(request,'formstart.html')

@api_view(['POST'])
def updatebio(request):
    try:
        x = list(Bio.objects.all().filter(user = request.user))
        
        if x==[]:
            Bio.objects.Create(user = request.user, firstname = request.POST['FirstName'], lastname = request.POST['LastName'], displayimage = request.POST['Profile'],status = request.POST['Description'])
        else:
            x = x[0]
            if request.POST['FirstName'] != '':x.firstname = request.POST['FirstName']
            if request.POST['LastName'] != '': x.lastname = request.POST['LastName']
            if request.POST['Profile'] != '': x.displayimage = request.POST['Profile']
            if request.POST['Description']!='':x.status = request.POST['Description']
            x.save()
    except:return Response({'status':'error'}, status.HTTP_400_BAD_REQUEST)
    return Response({'status':'no error yay'},status = status.HTTP_201_CREATED)

@api_view(['POST'])
def addbio(request):
    try:
        Bio.objects.Create(user = request.user, firstname = request.POST['FirstName'], lastname = request.POST['LastName'], displayimage = request.POST['Profile'],status = request.POST['Description'])
    except:
        return Response({'status':'error'}, status.HTTP_400_BAD_REQUEST)
    return Response({'status':'no error yay'},status = status.HTTP_201_CREATED)

@unauthenticated_user  
=======
@unauthenticated_user
def landing(request):
    context = {
    'landed':True
    }
    return render(request,'startup-page.html',context)
@unauthenticated_user
>>>>>>> 304d06e9fb5479fd493256eda982e6045714edc1
def register(request):
    return render(request,'register.html')

@unauthenticated_user
def trainer_register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print("insideeee first ifff")
        if form.is_valid():
            user  = form.save()
            group = Group.objects.get(name = "trainers")
            user.groups.add(group)
            print("insideeee")
            return redirect('login')
    context = {
        'form' : form,
    }
    print("checkkkk")
    return render(request,'trainer_register.html',context)

@unauthenticated_user
def trainee_register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user  = form.save()
            group = Group.objects.get(name = "trainees")
            user.groups.add(group)

            return redirect('login')
    context = {
        'form' : form,
    }
    return render(request,'trainee_register.html',context)

@unauthenticated_user
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)


        if user is not None:
            login(request,user)
            return redirect('start-page')

        else:
            print("wrong password")
    context = {}
    return render(request,'login.html',context)

def logoutUser(request):
	logout(request)
	return redirect('landing')

@login_required(login_url='login')
@allowed_users(allowed_roles=['trainers'])
def trainer(request):
    context = {}
    return render(request,'trainer.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['trainees'])
def trainee(request):
    return render(request,'trainee.html')
