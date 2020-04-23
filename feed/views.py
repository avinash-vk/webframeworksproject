from django.shortcuts import render,redirect
# Create your views here.
from recommender import get_recommendation
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group,User
from django.db.models import Q
from .forms import BioForm
from accounts.decorators import unauthenticated_user, allowed_users
from .models import Follow,Like,Tag,Saves
from blogs.models import Post
from accounts.models import Bio
from spotify.models import Playlist
from workout.models import Workout, WComment
from posts.models import Picture, PComment
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
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
    bio= Bio.objects.filter(user=request.user)
    if not bio==[]:
        Bio.objects.create(user=request.user,fullname="fullname unupdated",displayimage="defaultprofilepic.png",email="email unupdated",status="status unupdated")
        bio= Bio.objects.filter(user=request.user)
    x = 'dashboard.html'
    post_list = Post.objects.filter(author=request.user)
    workout_list = Workout.objects.filter(author=request.user)
    picture_list = Picture.objects.filter(author=request.user)
    playlist_list = Playlist.objects.filter(author=request.user)
    cw=[]
    pl = []
    ps=[]
    postlikelist = []
    postsavelist=[]
    worklikelist = []
    worksavelist =[]
    for post in post_list:
        postlikescount=post.likes.count()
        alllikes=post.likes.all()
        allsaves=post.saves.all()
        l = []
        for i in alllikes:
            if i.liked_by == request.user:
                pl.append(post)
        for i in allsaves:
            if i.saved_by == request.user:
                ps.append(post)

    for j in workout_list:
        alllikes=j.likes.all()
        allsaves=j.saves.all()
        for i in alllikes:
            if i.liked_by == request.user:
                worklikelist.append(j)
        for i in allsaves:
            if i.saved_by == request.user:
                worksavelist.append(j)
        cw += list(WComment.objects.all().filter(workout = j))

    pc=[]
    for j in picture_list:
        alllikes=j.likes.all()
        allsaves=j.saves.all()
        for i in alllikes:
            if i.liked_by == request.user:
                postlikelist.append(j)
        for i in allsaves:
            if i.saved_by == request.user:
                postsavelist.append(j)
        pc += list(PComment.objects.all().filter(picture = j))
        editable=True
    context = {
        'groupname': group ,
        'obj' : post_list,
        'workouts' : workout_list,
        'comments' : cw,
        'pictures' : picture_list,
        'playlists':playlist_list,
        'piccomments' : pc,
        'likelist' : pl,
        'savelist':ps,
        'postlike' : postlikelist,
        'postsave' : postsavelist,
        'worklike' : worklikelist,
        'worksave' : worksavelist,
        'editable':editable,
        'bio':bio
        }
    return render(request,x,context)
def bio_update(request):
    obj = Bio.objects.filter(user=request.user).first()
    form = BioForm(request.POST or None, instance= obj)
    context= {'form': form}
    if request.method=='POST':
        if form.is_valid():
            obj= form.save(commit= False)
            obj.save()
            return redirect('dashboard')
        else:
            context= {'form': form,'error': 'The form was not updated successfully. Please enter in a title and content'}
    return render(request, 'bio_update.html', context)
def profile(request,username):
    user = request.user
    profileuser = User.objects.all().filter(username=username)[0]
    bio= Bio.objects.filter(user=profileuser)
    if not bio:
        bio=Bio.objects.create(user=profileuser,fullname="unupdated",displayimage="defaultprofilepic.png",email="unupdated",status="unupdated")
        bio= Bio.objects.filter(user=request.user)
    group="trainers"
    x = 'dashboard.html'
    post_list = Post.objects.filter(author=profileuser)
    workout_list = Workout.objects.filter(author=profileuser)
    picture_list = Picture.objects.filter(author=profileuser)
    playlist_list = Playlist.objects.filter(author=profileuser)
    cw=[]
    pl = []
    ps=[]
    postlikelist = []
    postsavelist=[]
    worklikelist = []
    worksavelist =[]
    for post in post_list:
        postlikescount=post.likes.count()
        alllikes=post.likes.all()
        allsaves=post.saves.all()
        l = []
        for i in alllikes:
            if i.liked_by == request.user:
                pl.append(post)
        for i in allsaves:
            if i.saved_by == request.user:
                ps.append(post)

    for j in workout_list:
        alllikes=j.likes.all()
        allsaves=j.saves.all()
        for i in alllikes:
            if i.liked_by == request.user:
                worklikelist.append(j)
        for i in allsaves:
            if i.saved_by == request.user:
                worksavelist.append(j)
        cw += list(WComment.objects.all().filter(workout = j))

    pc=[]
    for j in picture_list:
        alllikes=j.likes.all()
        allsaves=j.saves.all()
        for i in alllikes:
            if i.liked_by == request.user:
                postlikelist.append(j)
        for i in allsaves:
            if i.saved_by == request.user:
                postsavelist.append(j)
        pc += list(PComment.objects.all().filter(picture = j))
        editable=False
    context = {
        'editable': editable,
        'groupname': group ,
        'obj' : post_list,
        'workouts' : workout_list,
        'comments' : cw,
        'pictures' : picture_list,
        'playlists':playlist_list,
        'piccomments' : pc,
        'likelist' : pl,
        'savelist':ps,
        'postlike' : postlikelist,
        'postsave' : postsavelist,
        'worklike' : worklikelist,
        'worksave' :worksavelist,
        'bio':bio
        }
    return render(request,x,context)
@login_required(login_url='login')
def explore(request):
    b = []
    if request.method == 'POST':
        b = get_follow_set(request,True)
    else:
        b = get_follow_set(request,False)
    q = Tag.objects.all()
    l = get_recommendation(request.user)
    pictures =[]
    workouts =[]
    obj = []
    for i in l:
        if i.__class__ == Post:
            obj.append(i)
        elif i.__class__ == Workout:
            workouts.append(i)
        else:
            pictures.append(i)
    pl=[]
    ps=[]
    for post in obj:
            postlikescount=post.likes.count()
            alllikes=post.likes.all()
            allsaves=post.saves.all()
            l = []
            for i in alllikes:
                if i.liked_by == request.user:
                    pl.append(post)
            for i in allsaves:
                if i.saved_by == request.user:
                    ps.append(post)
    worklikelist=[]
    worksavelist=[]
    cw=[]
    for j in workouts:
            alllikes=j.likes.all()
            allsaves=j.saves.all()
            for i in alllikes:
                if i.liked_by == request.user:
                    worklikelist.append(j)
            for i in allsaves:
                if i.saved_by == request.user:
                    worksavelist.append(j)
            cw += list(WComment.objects.all().filter(workout = j))

    pc=[]
    postlikelist=[]
    postsavelist=[]
    for j in pictures:
            alllikes=j.likes.all()
            allsaves=j.saves.all()
            for i in alllikes:
                if i.liked_by == request.user:
                    postlikelist.append(j)
            for i in allsaves:
                if i.saved_by == request.user:
                    postsavelist.append(j)
            pc += list(PComment.objects.all().filter(picture = j))
    context = {
        'followers' : b,
        'list' : q,
        'obj':obj,
        'piccomments' : pc,
        'comments':cw,
        'likelist' : pl,
        'savelist':ps,
        'postlike' : postlikelist,
        'postsave': postsavelist,
        'worklike' : worklikelist,
        'worksave' : worksavelist,
        'pictures':pictures,
        'workouts':workouts,
    }
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

def set_like(request,slug,type):
    if type==1:
        object_liked = Post.objects.get(slug=slug)
    elif type==3:
        object_liked = Workout.objects.get(slug=slug)
    else:
        object_liked = Picture.objects.get(slug=slug)

    l=[]
    like_set = Like.objects.all()
    for i in like_set:
        if i.liked_by == request.user and i.content_object == object_liked:
            l.append(i)
    like_set = l
    if list(like_set)==[]:
       Like.objects.create(content_type=ContentType.objects.get_for_model(object_liked),content_object=object_liked,liked_by = request.user)

    else:
        l = []
        o = object_liked.likes.all()
        for i in o:
            if i.liked_by == request.user and i.content_object == object_liked:
                l.append(i)
        my_obj = l[0]
        my_obj.delete()
def set_save(request,slug,type):
    if type==1:
        object_saved = Post.objects.get(slug=slug)
    elif type==3:
        object_saved = Workout.objects.get(slug=slug)
    else:
        object_saved = Picture.objects.get(slug=slug)

    l=[]
    save_set = Saves.objects.all()
    for i in save_set:
        if i.saved_by == request.user and i.content_object == object_saved:
            l.append(i)
    save_set = l
    if list(save_set)==[]:
       Saves.objects.create(content_type=ContentType.objects.get_for_model(object_saved),content_object=object_saved,saved_by = request.user)

    else:
        l = []
        o = object_saved.saves.all()
        for i in o:
            if i.saved_by == request.user and i.content_object == object_saved:
                l.append(i)
        my_obj = l[0]
        my_obj.delete()





@login_required(login_url='login')
def newsfeed(request):
    d = get_all_followers(request)
    postlikelist = []
    worklikelist = []
    postsavelist=[]
    worksavelist=[]
    p = []
    w = []
    pic = []
    cw = []
    pc = []
    pl = []
    ps=[]
    for i in d:
        p += list(Post.objects.all().filter(author = i))
        w += list(Workout.objects.all().filter(author = i))
        pic += list(Picture.objects.all().filter(author = i))
    for post in p:
        alllikes=post.likes.all()
        allsaves=post.saves.all()
        for i in alllikes:
            if i.liked_by == request.user:
                pl.append(post)
        for i in allsaves:
            if i.saved_by == request.user:
                ps.append(post)
    for j in w:
        alllikes=j.likes.all()
        allsaves=j.saves.all()
        for i in alllikes:
            if i.liked_by == request.user:
                worklikelist.append(j)
        for i in allsaves:
            if i.saved_by == request.user:
                worksavelist.append(j)
    for j in pic:
        alllikes=j.likes.all()
        allsaves=j.saves.all()
        for i in alllikes:
            if i.liked_by == request.user:
                postlikelist.append(j)
        for i in allsaves:
            if i.saved_by == request.user:
                postsavelist.append(j)
        pc += list(PComment.objects.all().filter(picture = j))
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
        'likelist' : pl,
        'savelist':ps,
        'postlike' : postlikelist,
        'postsave': postsavelist,
        'worklike' : worklikelist,
        'worksave' : worksavelist,

    }
    return render(request,'newsfeed.html', context )
def saved(request):
    d = Saves.objects.all().filter(saved_by=request.user)
    postlikelist = []
    worklikelist = []
    postsavelist=[]
    worksavelist=[]
    p = []
    w = []
    pic = []
    cw = []
    pc = []
    pl = []
    ps=[]
    for i in d:
        if i.content_object.__class__==Post:
            p.append(i.content_object)
        elif i.content_object.__class__==Workout:
            w.append(i.content_object)
        else:
            pic.append(i.content_object)
    for post in p:
        alllikes=post.likes.all()
        allsaves=post.saves.all()
        for i in alllikes:
            if i.liked_by == request.user:
                pl.append(post)
        for i in allsaves:
            if i.saved_by == request.user:
                ps.append(post)
    for j in w:
        alllikes=j.likes.all()
        allsaves=j.saves.all()
        for i in alllikes:
            if i.liked_by == request.user:
                worklikelist.append(j)
        for i in allsaves:
            if i.saved_by == request.user:
                worksavelist.append(j)
    for j in pic:
        alllikes=j.likes.all()
        allsaves=j.saves.all()
        for i in alllikes:
            if i.liked_by == request.user:
                postlikelist.append(j)
        for i in allsaves:
            if i.saved_by == request.user:
                postsavelist.append(j)
        pc += list(PComment.objects.all().filter(picture = j))
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
        'likelist' : pl,
        'savelist':ps,
        'postlike' : postlikelist,
        'postsave': postsavelist,
        'worklike' : worklikelist,
        'worksave' : worksavelist,

    }
    return render(request,'saved.html', context )


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


def tagView(request):
    q = Tag.objects.all()
    l = get_recommendation(request.user)

    pictures =[]
    workouts =[]
    obj = []

    for i in l:
        if i.__class__ == Post:
            obj.append(i)
        elif i.__class__ == Workout:
            workouts.append(i)
        else:
            pictures.append(i)
    context = {
        'list' : q,
        'obj':obj,
        'pictures':pictures,
        'workouts':workouts,
    }
    return render(request,"tagview.html", context)
