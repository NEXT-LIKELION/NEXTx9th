from django.contrib import admin
from .models import Cocktail, Place
from django.contrib.auth.models import User
# Register your models here.

# class Cocktail_imageInline(admin.StackedInline):
#     model = Cocktail_images

class CocktailAdmin(admin.ModelAdmin):
    # inlines = [Cocktail_imageInline]
    list_display = ('pk','title', 'taste', 'alcohollevel', 'sweetlevel', 'old', 'info', 'image')
    list_filter = ['alcohollevel']

# class Place_imageInline(admin.StackedInline):
#     model = Place_images

class PlaceAdmin(admin.ModelAdmin):
    # inlines = [Place_imageInline]
    list_display = ('placetitle', 'address', 'rate', 'info', 'cocktail', 'image')
    # list_filter = ['rate']

admin.site.register(Cocktail, CocktailAdmin);
admin.site.register(Place, PlaceAdmin);
