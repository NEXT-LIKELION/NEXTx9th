import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from django.db import models
from django.contrib.auth.models import User
from account.models import Profile, Lecture, PLR

# Create your models here.
class Post(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name="posts", default=None)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts", default=None)
    title = models.CharField(max_length=200, default=None)
    content = models.TextField(default=None)
    created_at = models.DateTimeField(default=None)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", default=None)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="comments", default=None)
    content = models.TextField(default=None)
    created_at = models.DateTimeField(default=None)


class Chatroom(models.Model):
    profile1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="chatrooms1", default=None)
    profile2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="chatrooms2", default=None)

class Chat(models.Model):
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE, related_name="chats", default=None)
    pfrom = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="send_chats", default=None)
    pto = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="receive_chats", default=None)
    content = models.TextField(default=None)
    created_at = models.DateTimeField(default=None)
    read = models.BooleanField(default=False)

