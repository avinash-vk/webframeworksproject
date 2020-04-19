from django.db import models
from django.contrib.auth.models import User
class Bio(models.Model):
    fullname = models.CharField(max_length=200, unique=True,default='fullname unupdated')
    displayimage = models.ImageField(upload_to='', null=True, verbose_name="",default='defaultprofilepic.png')
    status = models.CharField(max_length=140,unique=False,default='status unupdated')
    user = models.ForeignKey(User, on_delete= models.CASCADE,related_name='bio_user')
    email = models.EmailField(max_length=254,default='email unupdated')
    def save(self,*args,**kwargs):
        super(Bio,self).save(*args,**kwargs)
    def __str__(self):
        return self.fullname+": "+str(self.displayimage)
