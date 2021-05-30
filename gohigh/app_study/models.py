from django.db import models
from django.db.models.deletion import CASCADE
from app_registration.models import Profile
from django.contrib.auth.models import User
# Create your models here.

class Study(models.Model):
    name = models.CharField(max_length=20, blank=False)
    content = models.TextField(max_length=200, blank=False)
    period = models.TextField(max_length=200, blank=False)
    is_recruiting = models.BooleanField(default=True)
    location = models.CharField(max_length=30, blank=False)
    max_member = models.IntegerField(blank=False)
    num_member = models.IntegerField(blank=False)
    category = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.name

class Member(models.Model):
    # user -> manytomanyfield인지, foreignkey인지 몰겟음
    # user = models.ManyToManyField(Profile, on_delete=models.CASCADE, related_name="user", blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="joins")
    study = models.ForeignKey(Study, on_delete=models.CASCADE, blank=False, related_name="joins")
    is_accepted = models.BooleanField(default=False)