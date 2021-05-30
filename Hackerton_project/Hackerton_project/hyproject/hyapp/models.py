from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Subject(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE, default = 1, related_name="subjects")
  subject = models.CharField(max_length=255)
  professor = models.CharField(max_length=255)
  day1 = models.CharField(max_length=3, blank=True)
  day2 = models.CharField(max_length=3, blank=True)
  start_time = models.TimeField(blank=True, null=True)
  finish_time = models.TimeField(blank=True, null=True)
  record_choices = models.CharField(max_length=255, default ="collaborate")

  record = models.BooleanField(default=False, blank=True, null=True)


class Recordings(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = 1)
    date = models.DateField(auto_now_add=True)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE, related_name = 'recording')
    record = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)

class Fake_password(models.Model):
    password= models.CharField(max_length=30, default="", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fake_password')