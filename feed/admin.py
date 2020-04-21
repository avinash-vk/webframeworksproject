from django.contrib import admin
from .models import Follow,Like,Tag,Save
# Register your models here.
admin.site.register(Follow)
admin.site.register(Like)
admin.site.register(Tag)
admin.site.register(Save)
