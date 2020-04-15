from .models import Workout, WComment
from django import forms


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ('titlevid', 'videofile','caption')


class CommentForm(forms.ModelForm):
    class Meta:
        model = WComment
        fields = ('body',)
