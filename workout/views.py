from django.shortcuts import render,redirect
from django.views import generic
from .models import Workout, WComment
from feed.views import set_like,set_save
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.mixins import  LoginRequiredMixin
from .forms import WorkoutForm, CommentForm
from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
def like_post(request,slug):
    set_like(request,slug,3)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def save_post(request,slug):
    set_save(request,slug,3)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def workout_detail(request, slug):
    template_name = 'workout_detail.html'
    workout = get_object_or_404(Workout, slug=slug)
    currentuser=request.user
    alllikescount=workout.likes.count()
    alllikes=workout.likes.all()
    likelist=[]
    for i in alllikes:
        likelist.append(i.liked_by)
    comments = WComment.objects.all().filter(workout = workout)
    #comments = post.comments;
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.workout = workout
            new_comment.author = currentuser
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'workout': workout,
                                           'comments': comments,
                                           'currentuser':currentuser,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'alllikescount':alllikescount,
                                           'likelist':likelist,
                                           })


def addworkout(request):
    return render(request,'addworkout.html')

def workout_update(request,slug):
    obj= get_object_or_404(Workout,slug=slug)
    print("hhere",obj)
    return render(request,'workout_update.html',{'title':obj.title})

@api_view(['POST'])
def updateworkout(request):
    try:
        x = list(Workout.objects.all().filter(author = request.user).filter(title = request.POST['title']))
        print(x)
        if x==[]:
            Workout.objects.create(author = request.user, title = request.POST['title'], videofile = request.FILES['videofile'], caption = request.POST['caption'])
        else:
            x = x[0]
            if request.FILES['videofile'] != '': x.videofile = request.FILES['videofile']
            if request.POST['caption'] != '': x.caption = request.POST['caption']
            x.save()
    except Exception as e:
        print("here",e)
        return Response({'status':'error'}, status.HTTP_400_BAD_REQUEST)
    return Response({'status':'no error yay'},status = status.HTTP_201_CREATED)

@api_view(['POST'])
def add_workout(request):
    try:
        Workout.objects.create(author = request.user, title = request.POST['title'], videofile = request.FILES['videofile'], caption = request.POST['caption'])
    except Exception as e:
        print(e)
        return Response({'status':'error'}, status.HTTP_400_BAD_REQUEST)
    return Response({'status':'no error yay'},status = status.HTTP_201_CREATED)


'''
def addworkout(request):
    template_name='addworkout.html'
    user=request.user
    ''''''user=get_object_or_404(User)
    posts=post.filter(status=1,author=user)''''''
    new_workout=None
    if request.method=='POST':
        addworkout_form =WorkoutForm(request.POST,request.FILES)
        if addworkout_form.is_valid():
            new_workout=addworkout_form.save(commit=False)
            new_workout.author=user
            new_workout.save()
        return redirect('dashboard')
    else:
        addworkout_form=WorkoutForm()
    return render(request,template_name,{
                                    'user':user,
                                    'new_workout':new_workout,
                                    'addworkout_form':addworkout_form})

def workout_update(request,slug):
    obj = get_object_or_404(Workout,slug=slug)
    form = WorkoutForm(request.POST or None, request.FILES or None, instance= obj)
    context= {'form': form}
    if request.method=='POST':
        if form.is_valid():
            obj= form.save(commit= False)
            obj.save()
            return redirect('dashboard')
        else:
            context= {'form': form,'error': 'The form was not updated successfully. Please enter in a title and content'}
    return render(request, 'workout_update.html', context)

'''
def workout_delete(request, slug):
    workout = get_object_or_404(Workout, slug=slug)
    workout.delete()
    return redirect('dashboard')


def workout_comment(request, slug):
    workout = get_object_or_404(Workout, slug=slug)
    user=request.user
    #comments = Comment.objects.filter(post = post)
    #comments = workout.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        new_comment=WComment(body=request.POST.get('messages'))
        #comment_form = CommentForm(data=request.POST)
        #if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            #new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
        #new_comment.body = body
        new_comment.workout = workout
        new_comment.author = user
        new_comment.active = True
            # Save the comment to the database
        new_comment.save()
        #else:
        #   comment_form = CommentForm()
    #return redirect('newsfeed')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
