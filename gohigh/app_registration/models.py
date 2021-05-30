from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

# class University(models.Model):
#     name = models.CharField(max_length=30, blank=False)

# class Department(models.Model):
#     university_ID = models.CharField(max_length=30, blank=False)
#     name = models.CharField(max_length=30, blank=False)

# class LikeStudy(models.Model):
#     name = models.CharField(max_length=30, blank=False)

# class GiftCategory(models.Model):
#     name = models.CharField(max_length=30, blank=False)

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null = True)
    nickname = models.CharField(max_length=500, blank=False, null = True, default=None)
    location = models.CharField(max_length=30, blank=False, null = True, default=None)
    # image = models.TextField(default=None, null = True)
    # point = models.CharField(max_length = 100, null=True)
    university = models.CharField(max_length=30, blank=False, null = True, default=None)
    department = models.CharField(max_length=30, blank=False, null = True, default=None)
    likeStudy = models.CharField(max_length=30, blank=False, null = True, default=None)
    # likeGift = models.ForeignKey(GiftCategory, on_delete=models.CASCADE, related_name="likeGift", blank=False, default=None, null = True)
    # myGift = models.ForeignKey(GiftCategory, on_delete=models.CASCADE, related_name="myGift", blank=False, default=None, null = True)
    
    def __str__(self):
        return self.nickname
