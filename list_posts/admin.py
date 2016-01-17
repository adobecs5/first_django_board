from django.contrib import admin
from list_posts.models import Post, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "writer", "contents", "postNum"]
    list_filter = ["title", "writer", "contents"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "commentNum", "writer", "contents"]
    list_filter = list_display

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
