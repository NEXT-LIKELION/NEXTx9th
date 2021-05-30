from django.db import models
from app_registration.models import Profile
# from app_study.models import Study
# Create your models here.

class Mypage(models.Model):
    study = models.TextField(max_length=200, blank=False)
    # study = models.ForeignKey(Study, on_delete=models.CASCADE, related_name= "mine", blank=False)
    # Profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name= "mine", blank=False)