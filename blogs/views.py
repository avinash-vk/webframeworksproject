from django.shortcuts import render,redirect

# Create your views here.
from django.views import generic
from .models import Post,Comment
from likes.models import Like
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
def likeSet(request,slug):
    global likelist
    object_liked = Post.objects.get(slug=slug)
    object_liker = User.objects.all().filter(username=request.user).first()
    like_set = Like.objects.all().filter(post_likes__liked_by = object_liker).filter(post_likes__content_object=object_liked)
    if list(like_set)==[]:
       object_liked.likes.create(post_likes__content_type=ContentType.objects.get_for_model(object_liked),post_likes__content_object=object_liked,post_likes__liked_by = object_liker)
    else:
        my_obj = object_liked.likes.get(post_likes__liked_by = object_liker, post_likes__content_object=object_liked)
        my_obj.delete()
    return redirect('/blogs/'+slug)

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    currentuser=request.user;
    alllikescount=post.likes.count();
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
