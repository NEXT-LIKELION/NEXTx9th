from django.shortcuts import render, redirect
from .models import Post, Post_comment, Lecture, Lecture_comment, Scrap
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

# Create your views here.
def main(request):
    posts = Post.objects.all()
    lectures = Lecture.objects.all()

    return render(request, 'main.html', {'posts': posts, 'lectures': lectures})

def signup(request):
    if (request.method == 'POST'):
        found_user = User.objects.filter(username=request.POST['username'])
        if (len(found_user) > 0):
            error = 'username이 이미 존재합니다'
            return render(request, 'signup.html', {
                'error' : error
                })
        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
        auth.login(request, new_user)
        return redirect('main')

    return render(request, 'signup.html')

def login(request):
    if (request.method == 'POST'):
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if (found_user is None):
            error = '아이디 또는 비밀번호가 틀렸습니다.'
            return render(request, 'login.html', {
                'error' : error
                })
        auth.login(request, found_user)
        return redirect('main')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)

    return redirect('main')

def mypage(request, user_pk):
    scraps = Scrap.objects.filter(user = User.objects.get(pk=user_pk))
    
    return render(request, 'mypage.html', {'scraps': scraps})


def category_business(request):
    posts = Post.objects.filter(category="business")

    return render(request, 'category_business.html', {'posts': posts})

def category_coding(request):
    posts = Post.objects.filter(category="coding")

    return render(request, 'category_coding.html', {'posts': posts})

def category_economics(request):
    posts = Post.objects.filter(category="economics")

    return render(request, 'category_economics.html', {'posts': posts})

def category_environengineer(request):
    posts = Post.objects.filter(category="environenginner")

    return render(request, 'category_environengineer.html', {'posts': posts})

def category_humanities(request):
    posts = Post.objects.filter(category="humanities")

    return render(request, 'category_humanities.html', {'posts': posts})

def category_law(request):
    posts = Post.objects.filter(category="law")

    return render(request, 'category_law.html', {'posts': posts})

def category_lifescience(request):
    posts = Post.objects.filter(category="lifescience")

    return render(request, 'category_lifescience.html', {'posts': posts})



def lecture_business(request):
    lectures = Lecture.objects.filter(category="business")

    return render(request, 'lecture_business.html', {'lectures': lectures})

def lecture_coding(request):
    lectures = Lecture.objects.filter(category="coding")

    return render(request, 'lecture_coding.html',{'lectures': lectures})

def lecture_economics(request):
    lectures = Lecture.objects.filter(category="economics")

    return render(request, 'lecture_economics.html', {'lectures': lectures})

def lecture_environengineer(request):
    lectures = Lecture.objects.filter(category="environenginner")

    return render(request, 'lecture_environengineer.html',{'lectures': lectures})

def lecture_humanities(request):
    lectures = Lecture.objects.filter(category="humanities")

    return render(request, 'lecture_humanities.html', {'lectures': lectures})

def lecture_law(request):
    lectures = Lecture.objects.filter(category="law")

    return render(request, 'lecture_law.html', {'lectures': lectures})

def lecture_lifescience(request):
    lectures = Lecture.objects.filter(category="lifescience")

    return render(request, 'lecture_lifescience.html', {'lectures': lectures})




def category(request):
    posts = Post.objects.all()

    return render(request, 'category.html', {'posts': posts})

def academy(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method=='POST':
        content = request.POST['content']
        Post_comment.objects.create(
            post = post,
            content = content,
            author = request.user
        )
        return redirect('academy', post_pk)

    return render(request, 'academy.html', {'post': post})

def delete_academy_comment(request, post_pk, post_comment_pk):
    post_comment = Post_comment.objects.get(pk=post_comment_pk)
    post_comment.delete()
    return redirect('academy', post_pk)

def lecture_main(request):
    lectures = Lecture.objects.all()
    return render(request, 'lecture_main.html', {'lectures': lectures})

def lecture_detail(request, lecture_pk):
    lecture = Lecture.objects.get(pk=lecture_pk)

    if request.method =='POST':
        content = request.POST['content']
        Lecture_comment.objects.create(
            lecture=lecture,
            content=content,
            author = request.user
        )
        return redirect('lecture_detail', lecture_pk)
    return render(request, 'lecture_detail.html' , {'lecture': lecture} )

def delete_lecture_comment(request, lecture_pk, lecture_comment_pk):
    lecture_comment = Lecture_comment.objects.get(pk=lecture_comment_pk)
    lecture_comment.delete()
    return redirect('lecture_detail', lecture_pk)

@login_required(login_url='/login')
def academy_form(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            introduction = request.POST['introduction'],
            apply_start = request.POST['apply_start'],
            apply_end = request.POST['apply_end'],
            category = request.POST['category'],
            target = request.POST['target'],
            logo = request.FILES['logo'],
            content = request.POST['content'],
            author = request.user
        )
        return redirect('academy', new_post.pk)
    return render(request, 'academy_form.html')

def academy_edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post.pk).update(
            title = request.POST['title'],
            introduction = request.POST['introduction'],
            apply_start = request.POST['apply_start'],
            apply_end = request.POST['apply_end'],
            category = request.POST['category'],
            target = request.POST['target'],
            logo = request.FILES['logo'],
            content = request.POST['content'],
            author = request.user
        )
        return redirect('academy', post_pk)
    return render(request, 'academy_edit.html', {'post': post})

def academy_delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('main')

@login_required(login_url='/login')
def lecture_form(request):
    if request.method == 'POST':
        new_lecture = Lecture.objects.create(
            title = request.POST['title'],
            introduction = request.POST['introduction'],
            price = request.POST['price'],
            construct = request.POST['construct'],
            category = request.POST['category'],
            thumbnail = request.FILES['thumbnail'],
            content = request.POST['content'],
            author = request.user
        )
        return redirect('lecture_detail', new_lecture.pk) ##이거 고쳐야됨##

    return render(request, 'lecture_form.html')


    

def lecture_edit(request, lecture_pk):
    lecture = Lecture.objects.get(pk=lecture_pk)

    if request.method == 'POST':
        Lecture.objects.filter(pk=lecture.pk).update(
            title = request.POST['title'],
            introduction = request.POST['introduction'],
            price = request.POST['price'],
            construct = request.POST['construct'],
            category = request.POST['category'],
            thumbnail = request.FILES['thumbnail'],
            content = request.POST['content'],
            author = request.user
        )
        return redirect('lecture_detail', lecture_pk)
    return render(request, 'lecture_edit.html', {'lecture': lecture})

def lecture_delete(request, lecture_pk):
    lecture = Lecture.objects.get(pk=lecture_pk)
    lecture.delete()
    return redirect('main')

@csrf_exempt
def scrap(request):
    if request.method == "POST":
        request_body = json.loads(request.body)
        post_pk = request_body['post_pk']

        existing_scrap = Scrap.objects.filter(
            post = Post.objects.get(pk=post_pk),
            user = request.user
        )

    if existing_scrap.count() > 0:
        existing_scrap.delete()

    else:
        Scrap.objects.create(
            post=Post.objects.get(pk=post_pk),
            user = request.user
        )

    post_scraps = Scrap.objects.filter(
        post = Post.objects.get(pk=post_pk)
    )

    response = {
        'scrap_count': post_scraps.count()
    }

    return HttpResponse(json.dumps(response))