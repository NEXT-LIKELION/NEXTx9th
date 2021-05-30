from django.shortcuts import render, redirect
from .models import Cocktail, Place

# Create your views here.

def home(request):
    cocktails = Cocktail.objects.all()

    return render(request, 'home.html', {'cocktails' : cocktails})

def detail(request, post_pk):
    cocktail = Cocktail.objects.get(pk=post_pk)
    places = Place.objects.filter(cocktail=post_pk)
    return render(request, 'detail.html', {'cocktail':cocktail, 'places':places})

def survey(request):
    return render(request, 'survey.html')

def new(request):
    return render(request, 'new.html')

def testloading(request):
    return render(request, 'testloading.html')

def search(request):
    cocktails = Cocktail.objects.all()

    return render(request, 'search.html', {'cocktails' : cocktails})    

def result(request, result_pk):
    cocktail = Cocktail.objects.get(pk=result_pk)
    return render(request, 'result.html', {'cocktail' : cocktail})    