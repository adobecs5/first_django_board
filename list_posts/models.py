from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 30)
    writer = models.CharField(max_length = 10)
    contents = models.CharField(max_length = 1000)
    postNum = models.AutoField(primary_key = True)
    created = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, related_name = "comments")
    commentNum = models.IntegerField()
    writer = models.CharField(max_length = 10)
    contents = models.CharField(max_length = 1000)
    created = models.DateTimeField(auto_now_add=True)
