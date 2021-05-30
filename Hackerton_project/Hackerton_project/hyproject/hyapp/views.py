
from django.shortcuts import render, redirect
from .models import Subject, Recordings, Fake_password
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from . import crawling
from datetime import datetime
import random
from . import weathercr
from pyautogui import center
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import pyautogui as pg
from . import click

# Create your views here.


def main(request):
    return render(request, 'main.html')

def signup(request):
    if request.method == "POST":
        found_user = User.objects.filter(username=request.POST['username'])
        if len(found_user) > 0:
            error = '이미 존재하는 아이디입니다 😥'
            return render(request, 'registration/signup.html', {'error': error})

        new_user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
        )
        Fake_password.objects.create(
            password = request.POST['fake_password'],
            user = request.user
        )
        user_id= request.POST['username']
        user_password=request.POST['password']
        this_user = User.objects.get(username=request.POST['username'])
        try:
            crawling.crawling(this_user, user_id, user_password)
        except:
            new_user.delete()
            error = '네트워크 혹은 아이디 오류입니다. 정확한 정보인지 확인하고 다시 시도해주세요'
            return render(request, 'registration/signup.html', {'error': error})

        auth.login(request, new_user,
                   backend='django.contrib.auth.backends.ModelBackend')
        return redirect('mysubject', new_user.pk)

    return render(request, 'registration/signup.html')



def home_select(request):
    subjects = Subject.objects.all()
    num = subjects.count()
   
    if datetime.today().isoweekday()==1:
        subjects1 = subjects.filter(day1 ='월요일')
        subjects2 = subjects.filter(day2 ='월요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        num = subjects.count()
        for i in range(num):
            if request.method == "POST":
                sub= subjects[i]
                Subject.objects.filter(subject=sub.subject).update(
                    record = request.POST['record[]']
                )
                select = request.POST.getlist('record[]').save()
                rnum = len(select)
                if i > (rnum - 1) :
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = "False"
                    record_yesno.save()                    
                else:
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = select[i]
                    record_yesno.save()
                if i == num - 1:
                    return redirect("home")
        return render(request, 'home_select.html', {'subjects': subjects})
    if datetime.today().isoweekday()==2:
        subjects1 = subjects.filter(day1 ='화요일')
        subjects2 = subjects.filter(day2 ='화요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        num = subjects.count()
        for i in range(num):
            if request.method == "POST":
                sub= subjects[i]
                Subject.objects.filter(subject=sub.subject).update(
                    record = request.POST['record[]']
                )
                select = request.POST.getlist('record[]')
                rnum = len(select)
                if i > (rnum - 1) :
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = "False"
                    record_yesno.save()                    
                else:
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = select[i]
                    record_yesno.save()
                if i == num - 1:
                    return redirect("home")
        return render(request, 'home_select.html', {'subjects': subjects})
    if datetime.today().isoweekday()==3:
        subjects1 = subjects.filter(day1 ='수요일')
        subjects2 = subjects.filter(day2 ='수요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        num = subjects.count()
        for i in range(num):
            if request.method == "POST":
                sub= subjects[i]
                Subject.objects.filter(subject=sub.subject).update(
                    record = request.POST['record[]']
                )
                select = request.POST.getlist('record[]')
                rnum = len(select)
                if i > (rnum - 1) :
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = "False"
                    record_yesno.save()                    
                else:
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = select[i]
                    record_yesno.save()
                if i == num - 1:
                    return redirect("home")
        return render(request, 'home_select.html', {'subjects': subjects})
    if datetime.today().isoweekday()==4:
        subjects1 = subjects.filter(day1 ='목요일')
        subjects2 = subjects.filter(day2 ='목요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        num = subjects.count()
        for i in range(num):
            if request.method == "POST":
                sub= subjects[i]
                Subject.objects.filter(subject=sub.subject).update(
                    record = request.POST['record[]']
                )
                select = request.POST.getlist('record[]')
                rnum = len(select)
                if i > (rnum - 1) :
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = "False"
                    record_yesno.save()                    
                else:
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = select[i]
                    record_yesno.save()
                if i == num - 1:
                    return redirect("home")
        return render(request, 'home_select.html', {'subjects': subjects})
    if datetime.today().isoweekday()==5:
        subjects1 = subjects.filter(day1 ='금요일')
        subjects2 = subjects.filter(day2 ='금요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        num = subjects.count()
        for i in range(num):
            if request.method == "POST":
                sub= subjects[i]
                Subject.objects.filter(subject=sub.subject).update(
                    record = request.POST['record[]']
                )
                select = request.POST.getlist('record[]')
                rnum = len(select)
                if i > (rnum - 1) :
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = "False"
                    record_yesno.save()                    
                else:
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = select[i]
                    record_yesno.save()
                if i == num - 1:
                    return redirect("home")
       
        return render(request, 'home_select.html', {'subjects': subjects})
    if datetime.today().isoweekday()==6:
        subjects1 = subjects.filter(day1 ='토요일')
        subjects2 = subjects.filter(day2 ='토요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        num = subjects.count()
        for i in range(num):
            if request.method == "POST":
                sub= subjects[i]
                Subject.objects.filter(subject=sub.subject).update(
                    record = request.POST['record[]']
                )
                select = request.POST.getlist('record[]')
                rnum = len(select)
                if i > (rnum - 1) :
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = "False"
                    record_yesno.save()                    
                else:
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = select[i]
                    record_yesno.save()
                rnum = len(select)
                if i > (rnum - 1) :
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = "False"
                    record_yesno.save()                    
                else:
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = select[i]
                    record_yesno.save()
                if i == num - 1:
                    return redirect("home")
        return render(request, 'home_select.html', {'subjects': subjects})
        
    else:
        subjects1 = subjects.filter(day1 ='일요일')
        subjects2 = subjects.filter(day2 ='일요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        num = subjects.count()
        for i in range(num):
            if request.method == "POST":
                sub= subjects[i]
                Subject.objects.filter(subject=sub.subject).update(
                    record = request.POST['record[]']
                )
                select = request.POST.getlist('record[]')
                rnum = len(select)
                if i > (rnum - 1) :
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = "False"
                    record_yesno.save()                    
                else:
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = select[i]
                    record_yesno.save()
                rnum = len(select)
                if i > (rnum - 1) :
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = "False"
                    record_yesno.save()                    
                else:
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = select[i]
                    record_yesno.save()
                if i == num - 1:
                    return redirect("home")
        return render(request, 'home_select.html', {'subjects': subjects})

def home(request):
    # logged_in_user = request.user
    subjects = Subject.objects.filter(user=request.user)
    records = Recordings.objects.filter(date=datetime.today())
    recordings = records.order_by('subject__start_time')
    travel=['서울','부산','제주도']
    travel_select = random.choice(travel)
    result = weathercr.weathercrcr()


    tf = []
    
    for i in recordings:   
        if i.record == True:
            tf.append("녹화")
        else:
            tf.append("녹화 x")
   
    if datetime.today().isoweekday()==1:
        subjects1 = subjects.filter(day1 ='월요일')
        subjects2 = subjects.filter(day2 ='월요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        return render(request, 'home.html', {'subjects': subjects, 'tf': tf,  
        'recordings': recordings, 'travel_select': travel_select})
    if datetime.today().isoweekday()==2:
        subjects1 = subjects.filter(day1 ='화요일')
        subjects2 = subjects.filter(day2 ='화요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        return render(request, 'home.html', {'subjects': subjects, 'tf': tf,  
        'recordings': recordings, 'travel_select': travel_select})
    if datetime.today().isoweekday()==3:
        subjects1 = subjects.filter(day1 ='수요일')
        subjects2 = subjects.filter(day2 ='수요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        num = subjects.count()
        return render(request, 'home.html', {'subjects': subjects, 'tf': tf,  
        'recordings': recordings, 'travel_select': travel_select})
    if datetime.today().isoweekday()==4:
        subjects1 = subjects.filter(day1 ='목요일')
        subjects2 = subjects.filter(day2 ='목요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        return render(request, 'home.html', {'subjects': subjects, 'tf': tf,  
        'recordings': recordings, 'travel_select': travel_select})
    if datetime.today().isoweekday()==5:
        subjects1 = subjects.filter(day1 ='금요일')
        subjects2 = subjects.filter(day2 ='금요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        return render(request, 'home.html', {'subjects': subjects, 'tf': tf,  
        'recordings': recordings, 'travel_select': travel_select})
    if datetime.today().isoweekday()==6:
        subjects1 = subjects.filter(day1 ='토요일')
        subjects2 = subjects.filter(day2 ='토요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        return render(request, 'home.html', {'subjects': subjects, 'tf': tf,  
        'recordings': recordings, 'travel_select': travel_select})
    else:
        subjects1 = subjects.filter(day1 ='일요일')
        print(subjects1)
        subjects2 = subjects.filter(day2 ='일요일')
        print(subjects2)
        subjects = subjects1.union(subjects2).order_by('start_time')
        return render(request, 'home.html', {'subjects': subjects, 'tf': tf,  
        'recordings': recordings, 'travel_select': travel_select, 'weathers': result})

def login(request):
    if request.method == 'POST':
        found_user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if found_user == None:
            error = '입력하신 아이디와 비밀번호가 잘못되었어요 😥'
            return render(request, 'registration/login.html', {'error': error})
        else:
            auth.login(request, found_user)
            return redirect('home_select')

    return render(request, 'registration/login.html')


def mysubject(request, user_pk):
    # if request.method == 'POST':
    #     for i in range(subject_num):
            
    # user = User.objects.get(pk=user_pk)
    # subjects = user.subjects.all()
    user =User.objects.get(pk=user_pk)
    subjects = user.subjects.all()
    subject_num = subjects.count()
    for i in range(subject_num):
        if request.method == "POST":
            subject_title = subjects[i].subject
            subject = Subject.objects.get(subject=subject_title)
            day1 = request.POST.getlist('day1[]')
            day2= request.POST.getlist('day2[]')
            start_time = request.POST.getlist('start_time[]')
            finish_time = request.POST.getlist('finish_time[]')
            try:
                start_time_converted = datetime.strptime(start_time[i], "%H:%M").time()
            except:
                start_time_converted = datetime.strptime("00:00", "%H:%M").time()
            try:
                finish_time_converted = datetime.strptime(finish_time[i], "%H:%M").time()
            except:
                finish_time_converted = datetime.strptime("00:00", "%H:%M").time()
            print(start_time_converted, finish_time_converted)
            recording_choices = request.POST.getlist('recording_choices[]')
            subject.day1 = str(day1[i])
            subject.day2 = day2[i]
            subject.start_time = start_time_converted
            subject.finish_time = finish_time_converted
            subject.recording_choices = recording_choices
            subject.save()
            return redirect('home_select')
    return render(request, 'mysubject.html', {'subjects': subjects})

def detail(request, subject_pk):
    subject = Subject.objects.get(pk=subject_pk)
    if request.method == "POST":
        Subject.objects.filter(pk=subject_pk).update(
            day1= request.POST['day1'],
            day2 =request.POST['day2'],
            start_time = request.POST['start_time'],
            finish_time = request.POST['finish_time'],
            )
        return redirect('mysubject', user_pk=request.user.pk)
    return render(request, 'detail.html', { 'subject': subject })


def logout(request):
    auth.logout(request)
    return redirect('login')

# def recordlist(request):

#     recordings = Recordings.objects.filter(user=request.user).filter(record = True).order_by('subject_id')
#     # recordings_num = recordings.count()

#     tf = []
#     for i in recordings:   
#         if i.complete == True:
#             tf.append("수강완료")
#         else:
#             tf.append("미수강")

    
#     return render(request, 'recordlist.html', {'recordings': recordings, 'tf': tf})


# def checkcomplete(request, pk):
#     recording = Recordings.objects.get(pk= pk)
#     if request.method =='POST':
#         Recordings.objects.filter(pk=pk).update(
#             complete = request.POST['complete'],
#         )
#         return redirect('recordlist')
#     return render(request, 'checkcomplete.html', {'recording': recording})

def study(request):
    # logged_in_user = request.user
    total = Subject.objects.all().count()
    subjects = Subject.objects.filter(user=request.user).order_by('id')
    subject_num = subjects.count()
    my_subject_id =[]

    # my_subject_id[0] = subjects[4].id
    for i in range(total):
        if subject_num < i + 1 :
            break
        else:
            my_subject_id.append(subjects[i].id)
    
# total = 11 subject_num =10
 
    
    #강의 전체 개수 세기
    lectures = Recordings.objects.all()
    lectures_num = Recordings.objects.all().count()
    #녹화한 과목 전체 개수 세기
    recordings = Recordings.objects.filter(record = True)
    recordings_num =recordings.count()
    #수강한 강의 개수
    # completed_recordings = Recordings.objects.filter(record = True).filter(complete = True)
    # comp_num =completed_recordings.count()


    recording_rate = recordings_num / lectures_num * 100
    # complete_rate = comp_num / recordings_num * 100

    sub = []
    # in_num = []
    for i in range(subject_num):
        # for j in recordings:
        number = recordings.filter(subject_id = my_subject_id[i]).count() 
        sub.append(number)
   

    # incompleted_recordings = recordings.filter(record = True).filter(complete = False)
    # for i in range(subject_num):
    #     # for j in incompleted_recordings:
    #     number = incompleted_recordings.filter(subject_id = my_subject_id[i]).count() 
    #     in_num.append(number)

       
# subject_name = "크롤링한 과목"
# if Subject.objects.get(name=subject_name):
#     pass
# else:
#     Subject.objects.create(name=)

    return render(request, 'study.html', {'subjects': subjects, 'lectures_num': lectures_num, 
    'recordings_num': recordings_num, 'sub': sub,
     'subject_num': subject_num, 'my_subject_id': my_subject_id, 'recording_rate': recording_rate })   

def click_start(request):
    a=Subject.objects.filter(user=request.user)
    print(a)
    b= a.filter(record=True)
    print(b)
    c= b.count()
    user= request.user
    user_id = user.username
    user_pw = user.fake_password
    for i in range(c):
        if b[i].record_choices == 'zoom':
            start_time=b[i].start_time
            subject_title = b[i].subject
            while True:
                if ((datetime.now().hour == start_time.hour) and (datetime.now().minute == start_time.minute)):
                    click.zoom(user_id, user_pw, subject_title)
                    break
        else:
            start_time=b[i].start_time
            subject_title = b[i].subject
            while True:
                time.sleep(2)
                if ((datetime.now().hour == start_time.hour) and (datetime.now().minute == start_time.minute)):
                    click.collabo(subject_title)
                    break
                print("안녕하세요")
        
    return 0