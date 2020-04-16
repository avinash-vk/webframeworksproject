from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
class Like(models.Model):

    liked_by = models.ForeignKey(User, on_delete= models.CASCADE,related_name='like')
    created_at = models.DateTimeField(auto_now_add=True)
    # Listed below are the mandatory fields for a generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(blank=True,null=True)
    content_object = GenericForeignKey('content_type','object_id')
    def __str__(self):
        return '{} liked {}'.format(self.liked_by,self.content_object)
