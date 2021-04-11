from django.shortcuts import render,redirect
from .models import Article
# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    return render(request, 'detail.html', {'article': article})


def new(request):
    if request.method == 'POST':
    #POST 요청일 경우
        print(request.POST) # data확인
        new_article = Article.objects.create(
            title= request.POST['title'],
            content = request.POST['content']
        )
        return redirect('detail', article_pk=new_article.pk)
    #POST 요청이 아닐 경우
    return render(request, 'new.html')