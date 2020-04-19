from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.contrib.contenttypes.fields import GenericRelation
from feed.models import Like

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
# Create your models here.

class Workout(models.Model):
    titlevid = models.CharField(max_length=200, unique=True)
    videofile = models.FileField(upload_to='', null=True, verbose_name="")
    caption = models.CharField(max_length=140,unique=False,default='caption')
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='workout_workouts')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = GenericRelation(Like,related_query_name="workout_likes")

    class Meta:
        ordering = ['-created_on']
    def save(self,*args,**kwargs):
        self.slug = slugify(self.titlevid)
        super(Workout,self).save(*args,**kwargs)

    def __str__(self):
        return self.titlevid+": "+str(self.videofile)

class WComment(models.Model):
    workout = models.ForeignKey(Workout,on_delete=models.CASCADE,related_name='comments')
    #name = models.CharField(max_length=80)
    #email = models.EmailField()
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='workout_comments')
    body = models.TextField(max_length=140)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)
        