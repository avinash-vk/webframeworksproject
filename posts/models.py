from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
# Create your models here.

class Picture(models.Model):
    titlepic = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='', null=True, verbose_name="")
    caption = models.CharField(max_length=140,unique=False,default='caption')
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='picture_pictures')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']
    def save(self,*args,**kwargs):
        self.slug = slugify(self.titlepic)
        super(Picture,self).save(*args,**kwargs)
        

    def __str__(self):
        return self.titlepic+": "+str(self.image)

class PComment(models.Model):
    picture = models.ForeignKey(Picture,on_delete=models.CASCADE,related_name='comments')
    #name = models.CharField(max_length=80)
    #email = models.EmailField()
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='picture_comments')
    body = models.TextField(max_length=140)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)
        