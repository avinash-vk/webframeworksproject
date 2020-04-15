from .models import Comment,Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','status')
