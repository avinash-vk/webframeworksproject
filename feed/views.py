from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group,User
from django.db.models import Q
from accounts.decorators import unauthenticated_user, allowed_users
from .models import Follow
from blogs.models import Post
from workout.models import Workout, WComment
from posts.models import Picture, PComment

# Create your views here.
current_search = []
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
    x = 'dashboard.html'
    post_list = Post.objects.filter(author=request.user)
    workout_list = Workout.objects.filter(author=request.user)
    picture_list = Picture.objects.filter(author=request.user)
    cw=[]
    for j in workout_list:
        cw += list(WComment.objects.all().filter(workout = j))
    pc=[]
    for j in picture_list:
        pc += list(PComment.objects.all().filter(picture = j))
    context = {
        'groupname': group ,
        'object_list' : post_list,
        'workouts' : workout_list,
        'comments' : cw,
        'pictures' : picture_list,
        'piccomments' : pc,
        }
    return render(request,x,context)

@login_required(login_url='login')
def explore(request):
    b = []
    if request.method == 'POST':
        b = get_follow_set(request,True)
    else:
        b = get_follow_set(request,False)
    context = {'followers' : b }
    return render(request,'explore.html',context)

def get_follow_set(request,flag):
    b = []
    global current_search
    if flag:
        q = User.objects.all().filter(username__icontains = request.POST['search'])
        current_search = [q]
    else:
        if current_search != []:
            q = current_search[0]
        else:
            q = []
    for i in q:
        x = Follow.objects.all().filter(user_to = i).filter(user_from = request.user)
        t = False
        if list(x) != []:
            t = True
        b.append(follow_tmp(request.user,i,t))
    return b

@login_required(login_url='login')
def newsfeed(request):
    d = get_all_followers(request)
    p = []
    w = []
    pic = []
    cw = []
    pc = []
    for i in d:
        p += list(Post.objects.all().filter(author = i))
        w += list(Workout.objects.all().filter(author = i))
        pic += list(Picture.objects.all().filter(author = i))
    for j in w:
        cw += list(WComment.objects.all().filter(workout = j))
    for j in pic:
        pc += list(PComment.objects.all().filter(picture = j))
    context = {
        'obj' : p,
        'workouts' : w,
        'comments' : cw,
        'pictures'  : pic,
        'piccomments' : pc,
    }
    return render(request,'newsfeed.html', context )


class follow_tmp:
    def __init__(self,follower,person,t):
        self.followed_by = follower
        self.followed_to = person
        self.follow_exists = t

def get_all_followers(request):
    q  = Follow.objects.all().filter(user_from = request.user)
    d = []
    for i in q:
        d.append(i.user_to)
    return d

def followSet(request, username):
    to_follow = User.objects.all().filter(username=username).first()
    follow_by = User.objects.all().filter(username=request.user).first()
    follow_set = Follow.objects.all().filter(user_to = to_follow).filter(user_from = follow_by)

    f = Follow(user_to = to_follow, user_from = follow_by)

    if list(follow_set)==[]:
        f.save()
    else:
        my_obj = Follow.objects.get(user_to = to_follow,user_from = follow_by)
        my_obj.delete()

    return redirect('explore')


def test(request):
    q = get_all_followers(request)
    return HttpResponse(q)
