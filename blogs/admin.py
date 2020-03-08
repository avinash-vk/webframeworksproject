from django.contrib import admin
from .models import Blog
from .models import Post
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','description','author')
class PostAdmin(admin.ModelAdmin):
    list_display = ('image_url','caption')
admin.site.register(Post,PostAdmin)
admin.site.register(Blog,BlogAdmin)