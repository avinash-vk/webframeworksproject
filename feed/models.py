from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Follow(models.Model):
    user_from = models.ForeignKey(User,on_delete=models.CASCADE ,related_name = "follow_ing")
    user_to = models.ForeignKey(User,on_delete=models.CASCADE ,related_name="follow_er")
    created = models.DateTimeField(auto_now_add = True,db_index = True)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return "{} follows {}".format(self.user_from,self.user_to)

