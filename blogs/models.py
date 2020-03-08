from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 255)
    description = models.CharField(max_length = 1000)
    author = models.CharField(max_length = 100)
    #image_url = models.CharField(max_length = 2083)

class Post(models.Model):
    image_url = models.CharField(max_length = 2083)
    caption = models.CharField(max_length = 255)