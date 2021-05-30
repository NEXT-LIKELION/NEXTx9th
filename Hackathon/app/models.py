from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lecturedata(models.Model):
    subject_id = models.CharField(primary_key=True, max_length = 50)
    subject_name = models.CharField(max_length = 50)
    prof = models.CharField(max_length = 50)
    student = models.ManyToManyField(User)

    def __str__(self):
        return self.subject_name

# 각 채팅방에 달리는 코멘트
class Chat(models.Model):
    room = models.ForeignKey(Lecturedata, on_delete=models.CASCADE, related_name="rooms", null=True, default=None)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chat", null=True, default=None)
    time = models.TimeField(auto_now_add=True)