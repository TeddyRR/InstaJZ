from django.contrib import admin

from Insta.models import Post, PostTwo, InstaUser, Like, UserConnection

# Register your models here.
admin.site.register(Post)
admin.site.register(InstaUser)
admin.site.register(Like)
admin.site.register(UserConnection)

admin.site.register(PostTwo)