from django.contrib import admin
from .models import Profile, Lecture, PLR

# Register your models here.
admin.site.register(Profile)
admin.site.register(Lecture)
admin.site.register(PLR)