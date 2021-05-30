from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from colorfield.fields import ColorField
from django.urls import reverse

# Create your models here.
class Fotd(models.Model):
    picture = models.ImageField(upload_to='images/',blank = True)
    title = models.CharField(max_length=100,default="")
    content = models.TextField(max_length=300,default="")
    day = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default="")

    def __str__(self):
        return self.title

class Ootd(models.Model):
    picture = models.ImageField(upload_to='images/', blank = True)
    title = models.CharField(max_length=100,default="")
    content = models.TextField(max_length=300,default="")
    day = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default="")

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Totd(models.Model):
    COLOR_CHOICES = [
        ("#FDFBC7", "1"),
        ("#ECC5C7", "2"),
        ("#E29EAF", "3"),
        ("#A38FAB", "4"),
        ("#918DAB", "5"),
        ("#79849F", "6"),
    ]
    title = models.CharField(max_length=100,default="")
    content = models.TextField(max_length=300,default="")
    color = ColorField(choices=COLOR_CHOICES)
    day = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default="")

    def __str__(self):
        return self.title

class Motd(models.Model):
    OPTIONS = (
        ('1', '행벅'),
        ('2', '꿀꿀'),
        ('3', '짜증'),
        ('4', '우울'),
        ('5', '평온'),
        ('6', '나도 날 몰라')
    )

    title = models.CharField(max_length=100,default="")
    moods = models.CharField(choices=OPTIONS,max_length=50)
    content = models.TextField(max_length=1000,default="")
    day = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default="")

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile_user")
    nickname = models.CharField(max_length=40, blank=True)
    introduction = models.TextField(blank=True,default="")
    image = models.ImageField(upload_to='images/',blank=True)
    birthday = models.DateField(auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.nickname

class Like_Fotd(models.Model):
    fotd = models.ForeignKey(
        Fotd, on_delete=models.CASCADE, related_name= "like_fotd"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE ,related_name="like_fotd"
    )

class Like_Ootd(models.Model):
    ootd = models.ForeignKey(
        Ootd, on_delete=models.CASCADE, related_name= "like_ootd"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE ,related_name="like_ootd"
    )

class Event(models.Model):
    start_time = models.DateTimeField("시작시간")
    end_time = models.DateTimeField("마감시간")
    title = models.CharField("이벤트 이름", max_length=50)
    description = models.TextField("상세")

    class Meta:
        verbose_name = "이벤트 데이터"
        verbose_name_plural = "이벤트 데이터"

    def __str__(self):
        return self.title

    @property
    def get_html_url(self):
        url = reverse('edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'