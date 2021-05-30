from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, default=None)
    introduction = models.CharField(max_length=200, default=None)
    content = models.TextField(default=None)
    target = models.CharField(max_length=200, default=None)
    logo = models.ImageField(blank=True, upload_to='')
    apply_start = models.DateTimeField(null=True, blank=True)
    apply_end = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True, default=None)
    category = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.title

class Post_comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments', default=None)
    content = models.TextField(default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_comments', null=True, default=None)

class Lecture(models.Model):
    title = models.CharField(max_length=200, default=None)
    introduction = models.CharField(max_length=200)
    content = models.TextField(default=None)
    thumbnail = models.ImageField(blank=True, upload_to='')
    price = models.CharField(max_length=200, default=None)
    construct = models.CharField(max_length=200, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lectures', null=True, default=None)
    category = models.CharField(max_length=200, default=None)
    
    def __str__(self):
        return self.title


class Lecture_comment(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name='lecture_comments', default=None)
    content = models.TextField(default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lecture_comments', null=True, default=None)

class Scrap(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="scraps")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="scraps")