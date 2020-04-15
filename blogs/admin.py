from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']
    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment,CommentAdmin)

=======
from .models import Blog
from .models import Post
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','description','author')
class PostAdmin(admin.ModelAdmin):
    list_display = ('image_url','caption')
admin.site.register(Post,PostAdmin)
admin.site.register(Blog,BlogAdmin)
>>>>>>> ef99cff9e7ad8f0fb4d1fe66578540b18f16eb55
