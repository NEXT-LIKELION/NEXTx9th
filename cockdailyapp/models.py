from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cocktail(models.Model) :
    title = models.CharField(max_length=200, verbose_name="술 이름")
    taste = models.CharField(max_length=200, verbose_name="맛")
    alcohollevel = models.IntegerField(verbose_name="도수",blank=True,null=True)
    sweetlevel = models.IntegerField(verbose_name="당도",blank=True,null=True)
    old = models.TextField(verbose_name="one line description", null=True,blank=True)
    info = models.TextField(verbose_name="설명")
    image = models.ImageField(upload_to='images/',null=True, blank=True)

    def __str__(self):
        return f'{self.title} | {self.taste} | {self.alcohollevel} | {self.sweetlevel} | {self.old} | {self.info} | {self.image}'

class Place(models.Model):
    placetitle = models.CharField(max_length=200, verbose_name="가게 이름")
    address = models.TextField(verbose_name="주소")
    rate = models.IntegerField(verbose_name="네이버 평점", blank=True)
    info = models.TextField(verbose_name="설명")
    cocktail = models.IntegerField(verbose_name="칵테일fk")    
    image = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.placetitle} | {self.address} | {self.rate} | {self.info} | {self.cocktail} | {self.image}'