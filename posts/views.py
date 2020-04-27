from django.shortcuts import render,redirect
from django.views import generic
from .models import Picture, PComment
from django.contrib.auth.models import User
from django.contrib.auth.mixins import  LoginRequiredMixin
from .forms import PictureForm, CommentForm
from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from feed.views import set_like,set_save
def like_post(request,slug):
    set_like(request,slug,2)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def save_post(request,slug):
    set_save(request,slug,2)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def picture_detail(request, slug):
    template_name = 'picture_detail.html'
    picture = get_object_or_404(Picture, slug=slug)
    currentuser=request.user
    alllikescount=picture.likes.count()
    alllikes=picture.likes.all()
    likelist=[]
    for i in alllikes:
        likelist.append(i.liked_by)
    comments = PComment.objects.all().filter(picture = picture)
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

    return render(request, template_name, {'picture': picture,
                                           'piccomments': comments,
                                           'currentuser':currentuser,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'alllikescount':alllikescount,
                                           'likelist':likelist,
                                           })


def addpicture(request):
    return render(request,'addpicture.html')

def picture_update(request,slug):
    obj= get_object_or_404(Picture,slug=slug)
    print("hhere",obj)
    return render(request,'picture_update.html',{'title':obj.title})

@api_view(['POST'])
def apiupdatepicture(request):
    try:
        x = list(Picture.objects.all().filter(author = request.user).filter(title = request.POST['title']))
        print(x)
        if x==[]:
            Picture.objects.create(author = request.user, title = request.POST['title'], image = request.POST['image'], caption = request.POST['caption'])
        else:
            x = x[0]
            if request.POST['image'] != '': x.image = request.POST['image']
            if request.POST['caption'] != '': x.caption = request.POST['caption']
            x.save()
    except Exception as e:
        print("here",e)
        return Response({'status':'error'}, status.HTTP_400_BAD_REQUEST)
    return Response({'status':'no error yay'},status = status.HTTP_201_CREATED)

@api_view(['POST'])
def apiaddpicture(request):
    try:
        Picture.objects.create(author = request.user, title = request.POST['title'], image = request.POST['image'], caption = request.POST['caption'])
    except Exception as e:
        print(e)
        return Response({'status':'error'}, status.HTTP_400_BAD_REQUEST)
    return Response({'status':'no error yay'},status = status.HTTP_201_CREATED)



def picture_delete(request, slug):
    picture = get_object_or_404(Picture, slug=slug)
    picture.delete()
    return redirect('dashboard')


def picture_comment(request, slug):
    #template_name = 'picture_comment.html'
    picture = get_object_or_404(Picture, slug=slug)
    user=request.user
    #comments = Comment.objects.filter(post = post)
    #comments = workout.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        new_comment=PComment(body=request.POST.get('messages'))
        #comment_form = CommentForm(data=request.POST)
        #if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            #new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
        #new_comment.body = body
        new_comment.picture = picture
        new_comment.author = user
        new_comment.active = True
            # Save the comment to the database
        new_comment.save()
        #else:
        #   comment_form = CommentForm()
    return redirect('newsfeed')
    '''
    return render(request, template_name, {'workout': workout,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
'''
