from django.contrib import admin
from .models import Post, Post_comment, Lecture, Lecture_comment, Scrap

# Register your models here.
admin.site.register(Post)
admin.site.register(Post_comment)
admin.site.register(Lecture)
admin.site.register(Lecture_comment)
admin.site.register(Scrap)