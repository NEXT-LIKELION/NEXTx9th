from django.shortcuts import render, redirect
from .models import Lecturedata, Chat
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.mail import EmailMessage
import random

from django.views.generic import ListView, DetailView,TemplateView, FormView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from django.conf import settings

from app.models import Lecturedata

from app.forms import PostSearchForm
from django.db.models import Q

def home(request):
    return render(request, 'home.html')

def login(request):
    if (request.method == 'POST'):
        found_user = auth.authenticate(
            username = request.POST['id'],
            password = request.POST['password'],
        )
        if (found_user is None):
            error = '아이디 또는 비밀번호가 틀렸습니다'
            # render(request, 'login.html', {'error' : error})
            return JsonResponse({"done": False}) 
        auth.login(request, found_user)# 백엔드에서만 로그인이 된 상태로 변경
        # return redirect('home') # TODO: 패이지 생기면 수정
        return JsonResponse({"done": True}) # 프론트에 로그인된 상태를 알림
    return render(request, 'login.html')

def signup(request):
    if (request.method == 'POST'): # 폼 태그에서 넘어왔을 경우
        email = request.POST['email'] + '@korea.ac.kr'
        error = {}
        found_username = User.objects.filter(username=request.POST['id'])
        found_nickname = User.objects.filter(last_name=request.POST['nickname'])
        found_email = User.objects.filter(email=email)
        if (len(found_username) > 0):
            error['same_id'] = True
        if (request.POST['password'] != request.POST['password_confirm']):
            error['not_same_password'] = True
        if (len(found_nickname) > 0):
            error['same_nickname'] = True
        if (len(found_email) > 0):
            error['same_email'] = True
        if (request.session.get('opt') != request.POST['opt']):
            error['not_same_opt'] = True
        if (len(error) > 0):
            result = {"done": False, "error": error}
        else:
            new_user = User.objects.create_user(
                username = request.POST['id'], # id 사용
                first_name = request.POST['username'],
                password = request.POST['password'],
                last_name = request.POST['nickname'],
                email = email,
            )
            result = {"done": True}
        # auth.login(request, new_user)
        return JsonResponse(result) # Ajax로 Json형식으로 보내줌
    return render(request, 'signup.html')

def signup_done(request):
    return render(request, 'signup_done.html')

def email_opt(request): 
    email = request.GET['email'] + '@korea.ac.kr'
    try: #여섯가지 난수를 보내기 try문은 에러가 나도 except문이 실행됨
        opt = str(random.randrange(0, 10))
        opt += str(random.randrange(0, 10))
        opt += str(random.randrange(0, 10))
        opt += str(random.randrange(0, 10))
        opt += str(random.randrange(0, 10))
        opt += str(random.randrange(0, 10))
        print(opt)
        email = EmailMessage('KUGETHER OTP Code Message', opt, to=[email]) # 이메일에 들어가는 메시지
        if (email.send() == 1):
            result = {"done": True} # Ajax통신으로 프론트에 보내줄 값
            request.session['opt'] = opt #해당 브라우저마다 가지고 있는 고유의 백엔드 값
        else:
            result = {"done": False}
    except:
        result = {"done": False} # try문 안에서 오류가 날 경우 실행
    return JsonResponse(result)

def chat(request, lecture_pk):
    # 1. find lecture by lecture_pk
    # 2. filter chats by lecture_pk

    the_lecture = Lecturedata.objects.get(pk=lecture_pk)
    chats = Chat.objects.filter(room=the_lecture)

    if request.method == 'POST':
        content = request.POST['content']
        Chat.objects.create(
            room=the_lecture,
            # 3. set room attribute to the lecture
            content=content,
            author=request.user,
        )
        # 4. redirect with lecture_pk you know the reason? YES!
        
        return redirect('chat', lecture_pk)

    return render(request, 'chat.html', {'chats':chats, 'the_lecture' : the_lecture})

def add_lecture(request, lecture_pk):
    the_lecture = Lecturedata.objects.get(pk=lecture_pk)
    the_lecture.student.add(request.user)
    return redirect('mypage')

    # 1. find lecture by lecture_pk
    # 2. add user to the lecture that you found object.field.add() add what?
    # 3. redirect to mypage
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'lecture_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        lecture_list = Lecturedata.objects.filter(Q(subject_id__icontains=searchWord) | Q(subject_name__icontains=searchWord) | Q(prof__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = lecture_list

        return render(self.request, self.template_name, context)

def mypage(request):
    lectures = Lecturedata.objects.filter(student=request.user)
    return render(request, 'mypage.html', {'lectures':lectures})


def logout(request):
    auth.logout(request)

    return redirect('home')