from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile, Lecture, PLR
from django.contrib import admin, auth
from django.contrib.auth.decorators import login_required
import datetime
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from blackboard import crawling
# Create your views here.

#registration
def main(request):

    return render(request, '0_registration/main.html')

def signup(request):
    if (request.method == 'POST'):
        find_user = User.objects.filter(username=request.POST['username'])
        if (find_user):
            error = '중복되는 아이디입니다.'
            return render(request, '0_registration/signup.html', {'error': error})

        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password'],
        )
        auth.login(request, new_user)
        return redirect('welcome')

    return render(request, '0_registration/signup.html')


def welcome(request):

    return render(request, '0_registration/welcome.html')


def login(request):
    if (request.method == 'POST'):
        login_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if (login_user is None):
            error = '아이디 또는 비밀번호가 틀렸습니다.'
            return render(request, '0_registration/login.html', {'error': error})
        auth.login(request, login_user)
        return redirect('home')

    return render(request, '0_registration/login.html')

def logout(request):
    auth.logout(request)

    return redirect('home')


# main page
@login_required(login_url='login')
def home(request):
    nickname = request.user.profile.nickname
    plrs = PLR.objects.filter(profile=request.user.profile)
    days = ["월","화","수","목","금"]
    classes = []
    classLists = []
    nontable = []
    class_real = []
    limit_class = []
    
    for plr in plrs:
        if(plr.lecture.subtime is not None):
            if('토' in plr.lecture.subtime):
                classList = {}
                classList['subject'] = plr.lecture.subject  #str
                classList['subnum'] = plr.lecture.subnum    #str
                classList['professor'] = plr.lecture.professor  #str
                nontable.append(classList)
# 월:1.3//토:1.2.3
    for plr in plrs:
        if(plr.lecture.subtime is None):      #강의시간 없을 때
            classList = {}
            classList['subject'] = plr.lecture.subject  #str
            classList['subnum'] = plr.lecture.subnum    #str
            classList['professor'] = plr.lecture.professor  #str
            nontable.append(classList)
        else:
            if(plr.lecture.subtime.find('//')):
                dd = plr.lecture.subtime.split('//')
                for a in dd:
                    classList = {}
                    classList['subject'] = plr.lecture.subject  #str
                    classList['subnum'] = plr.lecture.subnum    #str
                    classList['professor'] = plr.lecture.professor  #str
                    b = a.split(':')
                    classList['day']=b[0]
                    if(b[1].find('.')):
                        cs = b[1].split('.')
                        class_real += cs
                    else:
                        cs=[]
                        cs.append(b[1])
                        class_real += cs
                    classList['class']=cs
                    classLists.append(classList)
            else:
                dd = []
                dd.append(plr.lecture.subtime)
                for a in dd:
                    classList = {}
                    classList['subject'] = plr.lecture.subject  #str
                    classList['subnum'] = plr.lecture.subnum    #str
                    classList['professor'] = plr.lecture.professor  #str
                    b = a.split(':')
                    classList['day']=b[0]
                    if(b[1].find('.')):
                        cs = b[1].split('.')
                        class_real += cs
                    else:
                        cs=[]
                        cs.append(b[1])
                        class_real += cs
                    classList['class']=cs
                    classLists.append(classList)

    n = list(set(class_real))
    for i in range(len(n)):
        limit_class.append(int(n[i]))
    limit_class.sort()

    if(len(limit_class)):
        last = limit_class.pop()
    else:
        last = 0

    for i in range(last):
        classes.append(f'{i+1}')

    return render(request, '2_home/home.html', {'plrs': plrs, 'classLists':classLists,'days':days, 'classes':classes, 'nontable':nontable, 'nickname':nickname})

    
@login_required(login_url='login')
def bblogin(request):
    if request.method == 'POST':
        bbid = request.POST['bbid']
        bbpassword = request.POST['bbpassword']
        find_id = Profile.objects.filter(portal_id=bbid)
        print(find_id is True)
        
        if(find_id):    #이미 있는 아이디
            if (request.user.profile.portal_id != bbid): #자기 아이디 아님
                error = '이미 등록된 아이디입니다.'
                return render(request, '2_home/error.html', {'error': error})
            else: # 자기 아이디임
                plrs = PLR.objects.filter(profile=request.user.profile)
                plrs.delete()
        else:       #아이디 중복 없음
            plrs = PLR.objects.filter(profile=request.user.profile)
            plrs.delete()
            Profile.objects.filter(user=request.user).update(portal_id = bbid)  #그 사람 프로필에 등록
            
        
        results = crawling(bbid, bbpassword)
        # print(results)

        if (results is False):
            error = "블랙보드 로그인 실패"
            return render(request, '2_home/error.html', {'error': error})

        if len(results) == 0:
            error = "이번 학기 강의가 없습니다"
            return render(request, '2_home/error.html', {'error': error})

        for result in results:
            PLR.objects.create(
                profile = request.user.profile,
                lecture = Lecture.objects.get(subnum=result)
            )

        return redirect('home')

################## my page #############################
@login_required(login_url='login')
def mypage(request):
    myprofile = Profile.objects.get(user=request.user)
    

    return render(request, "1_mypage/mypage.html", {"myprofile": myprofile} )

def profile(request):
    if(request.method == 'POST'):
        if(request.POST.getlist('major-hide')):
            major_open = True
        else:
            major_open = False
        
        if(request.POST.getlist('studentId-hide')):
            studentid_open = True
        else:
            studentid_open = False

        if(request.POST.getlist('matewant')):
            matewant = True
        else:
            matewant = False
        
        profile = Profile.objects.create(
            user = request.user,
            nickname = request.POST['nickname'],
            gender = request.POST['gender'],
            major = request.POST['major'],
            major_open = major_open,
            studentid = request.POST['studentId'],
            studentid_open = studentid_open,
            introduce = request.POST['description'],
            matewant = matewant,
            photo = request.POST['photo'],
        )
        return redirect('home')

    return render(request, '0_registration/profile.html')



@login_required(login_url='login')
def profile_edit(request, profile_pk):
    profile = Profile.objects.get(pk=profile_pk)
    if(request.method == 'POST'):
        if(request.POST.getlist('major-hide')):
            major_open = True
        else:
            major_open = False
        
        if(request.POST.getlist('studentId-hide')):
            studentid_open = True
        else:
            studentid_open = False

        if(request.POST.getlist('matewant')):
            matewant = True
        else:
            matewant = False
        
        Profile.objects.filter(pk=profile.pk).update(
            user = request.user,
            nickname = request.POST['nickname'],
            gender = request.POST['gender'],
            major = request.POST['major'],
            major_open = major_open,
            studentid = request.POST['studentId'],
            studentid_open = studentid_open,
            introduce = request.POST['description'],
            matewant = matewant,
            photo = request.POST['photo']
        )
        return redirect('home')

    return render(request, "1_mypage/profile_edit.html", {'profile': profile})

