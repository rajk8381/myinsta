from django.contrib import admin

# Register your models here.
from .models import Post,Comment,Follow





class FollowAdmin(admin.ModelAdmin):
    list_display = ['user','follow_user','created_at']
    list_filter = ['created_at']
admin.site.register(Follow,FollowAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['desc','user','post_type','created_at','status']
    list_filter = ['post_type','status']
admin.site.register(Post,PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment','created_at','status','post','user']
    list_filter = ['post']


admin.site.register(Comment,CommentAdmin)