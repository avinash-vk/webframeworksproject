from django.shortcuts import render,redirect,HttpResponseRedirect
from feed.views import set_like,set_save
# Create your views here.
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.views import generic
from .models import Post,Comment
from feed.models import Like,Tag
from django.contrib.auth.models import User
from django.contrib.auth.mixins import  LoginRequiredMixin
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post
from .forms import CommentForm,AddPostForm
from django.shortcuts import render, get_object_or_404

def blog_comment(request, slug):
    #template_name = 'picture_comment.html'
    blog = get_object_or_404(Post, slug=slug)
    user=request.user
    #comments = Comment.objects.filter(post = post)
    #comments = workout.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        new_comment=Comment(body=request.POST.get('messages'))
        #comment_form = CommentForm(data=request.POST)
        #if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            #new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
        #new_comment.body = body
        new_comment.post = blog
        new_comment.author = user
        new_comment.active = True
            # Save the comment to the database
        new_comment.save()
        #else:
        #   comment_form = CommentForm()
    return redirect('newsfeed')

def addtag(post):
    l = str(post.tagname).split(',')
    for i in l:
        Tag.objects.create(name = i,content_type=ContentType.objects.get_for_model(post),content_object=post)

def addblog(request):
    return render(request,'addpost.html')

def updateblog(request,slug):
    obj= get_object_or_404(Post,slug=slug)
    return render(request,'post_update.html',{'title':obj.title})

@api_view(['POST'])
def updatepost(request):
    try:
        x = list(Post.objects.all().filter(author = request.user).filter(title = request.POST['title']))
        print(x)
        if x==[]:
            Post.objects.Create(author = request.user, title = request.POST['title'], content = request.POST['content'], tagname = request.POST['tagname'])
        else:
            x = x[0]
            if request.POST['content'] != '': x.content = request.POST['content']
            #if request.POST['status'] != '': x.status = request.POST['status']
            if request.POST['tagname']!='':x.tagname = request.POST['tagname']
            x.save()
    except Exception as e:
        print("here",e)
        return Response({'status':'error'}, status.HTTP_400_BAD_REQUEST)
    return Response({'status':'no error yay'},status = status.HTTP_201_CREATED)

@api_view(['POST'])
def add_post(request):
    print("here")
    print(request.POST.dict())
    try:
        Post.objects.create(author = request.user, title = request.POST['title'], content = request.POST['content'], tagname = request.POST['tagname'])
    except Exception as e:
        print(e)
        return Response({'status':'error'}, status.HTTP_400_BAD_REQUEST)
    return Response({'status':'no error yay'},status = status.HTTP_201_CREATED)

def like_post(request,slug):
    set_like(request,slug,1)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def save_post(request,slug):
    set_save(request,slug,1)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    currentuser=request.user
    alllikescount=post.likes.count()
    alllikes=post.likes.all()
    likelist=[]
    for i in alllikes:
        likelist.append(i.liked_by)
    comments = Comment.objects.all().filter(post = post)
    #comments = post.comments;
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.author = currentuser
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'currentuser':currentuser,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'alllikescount':alllikescount,
                                           'likelist':likelist,
                                           })



def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('dashboard')
