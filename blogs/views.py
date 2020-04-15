from django.shortcuts import render,redirect

# Create your views here.
from django.views import generic
from .models import Post,Comment
from django.contrib.auth.models import User
from django.contrib.auth.mixins import  LoginRequiredMixin


from .models import Post
from .forms import CommentForm,AddPostForm
from django.shortcuts import render, get_object_or_404

def addpost(request):
    template_name='addpost.html'
    user=request.user
    '''user=get_object_or_404(User)
    posts=post.filter(status=1,author=user)'''
    new_post=None
    if request.method=='POST':
        addpost_form =AddPostForm(data=request.POST)
        if addpost_form.is_valid():
            new_post=addpost_form.save(commit=False)
            new_post.author=user
            new_post.save()
        return redirect('dashboard')
    else:
        addpost_form=AddPostForm()
    return render(request,template_name,{
                                    'user':user,
                                    'new_post':new_post,
                                    'addpost_form':addpost_form})

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    #comments = Comment.objects.filter(post = post)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def post_update(request,slug):
    obj= get_object_or_404(Post,slug=slug)
    form = AddPostForm(request.POST or None, instance= obj)
    context= {'form': form}
    if request.method=='POST':
        if form.is_valid():
            obj= form.save(commit= False)
            obj.save()
            return redirect('dashboard')
        else:
            context= {'form': form,'error': 'The form was not updated successfully. Please enter in a title and content'}
    return render(request, 'post_update.html', context)


def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('dashboard')
