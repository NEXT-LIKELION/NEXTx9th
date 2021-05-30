from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def home(request):
    # if request.method == 'POST':
    #     picture = Post.objects.create(

    #     )
    #     return redirect('detail', picture.pk)
    return render(request, 'home.html')


def mypage(request):
    return render(request, 'mypage.html')


def signup(request):
    if (request.method == 'POST'):
        found_user = User.objects.filter(username=request.POST['username'])
        if(len(found_user) > 0):
            error = 'username이 이미 존재합니다'
            return render(request, 'registration/signup.html', {'error': error})
        new_user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        auth.login(request, new_user,
                   backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')

    return render(request, 'registration/signup.html')


def login(request):
    if (request.method == 'POST'):
        found_user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )

        if (found_user is None):
            error = '아이디 또는 비밀번호가 틀렸습니다'
            return render(request, 'registration/login.html', {
                'error': error
            })
        auth.login(request, found_user)
        return redirect('home')

    return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def detail(request, final_select_num):
    return render(request, 'detail.html', {'final_select_num': final_select_num})
