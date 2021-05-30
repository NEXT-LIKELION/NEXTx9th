from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Event,Fotd,Ootd,Tag,Totd,Motd,Profile,Like_Fotd,Like_Ootd
from django.contrib.auth.models import User
from django.contrib import auth
import datetime
from django.contrib.auth.decorators import login_required
import calendar
from .calendar import Calendar_F,Calendar_M,Calendar_O,Calendar_T,Calendar_nonlogin
from django.utils.safestring import mark_safe
from .forms import EventForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


# Create your views here.

def home(request):
    today = get_date(request.GET.get('month'))

    prev_month_var = prev_month(today)
    next_month_var = next_month(today)
    cal = Calendar_nonlogin(today.year, today.month)
    html_cal = cal.formatmonth(withyear=True)
    result_cal = mark_safe(html_cal)

    context = {'calendar' : result_cal, 'prev_month' : prev_month_var, 'next_month' : next_month_var}

    return render(request, 'home.html', context)

def home_ootd(request):
    today = get_date(request.GET.get('month'))

    prev_month_var = prev_month(today)
    next_month_var = next_month(today)
    cal = Calendar_O(today.year, today.month, request.user)
    html_cal = cal.formatmonth(withyear=True)
    result_cal = mark_safe(html_cal)

    context = {'calendar' : result_cal, 'prev_month' : prev_month_var, 'next_month' : next_month_var}

    return render(request, 'ootd_home.html', context)

def home_fotd(request):
    today = get_date(request.GET.get('month'))

    prev_month_var = prev_month(today)
    next_month_var = next_month(today)

    cal = Calendar_F(today.year, today.month, request.user)
    html_cal = cal.formatmonth(withyear=True)
    result_cal = mark_safe(html_cal)

    context = {'calendar' : result_cal, 'prev_month' : prev_month_var, 'next_month' : next_month_var}

    return render(request, 'fotd_home.html', context)

@login_required(login_url="/registration/login")
def home_totd(request):
    today = get_date(request.GET.get('month'))

    prev_month_var = prev_month(today)
    next_month_var = next_month(today)
    cal = Calendar_T(today.year, today.month, request.user)

    html_cal = cal.formatmonth(withyear=True)
    result_cal = mark_safe(html_cal)

    context = {'calendar' : result_cal, 'prev_month' : prev_month_var, 'next_month' : next_month_var}

    return render(request, 'totd_home.html', context)


def home_motd(request):
    today = get_date(request.GET.get('month'))

    prev_month_var = prev_month(today)
    next_month_var = next_month(today)

    cal = Calendar_M(today.year, today.month, request.user)
    html_cal = cal.formatmonth(withyear=True)
    result_cal = mark_safe(html_cal)

    context = {'calendar' : result_cal, 'prev_month' : prev_month_var, 'next_month' : next_month_var}

    return render(request, 'motd_home.html', context)

#현재 달력을 보고 있는 시점의 시간을 반환
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.datetime.today()

#현재 달력의 이전 달 URL 반환
def prev_month(day):
    first = day.replace(day=1)
    prev_month = first - datetime.timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

#현재 달력의 다음 달 URL 반환
def next_month(day):
    days_in_month = calendar.monthrange(day.year, day.month)[1]
    last = day.replace(day=days_in_month)
    next_month = last + datetime.timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

@login_required(login_url="/registration/login")
def main_detail(request,year,month,day):
    fotds = Fotd.objects.filter(day__year=year, day__month = month, day__day=day, author = request.user)
    ootds = Ootd.objects.filter(day__year=year, day__month = month, day__day=day, author = request.user)
    motds = Motd.objects.filter(day__year=year, day__month = month, day__day=day, author = request.user)
    totds = Totd.objects.filter(day__year=year, day__month = month, day__day=day, author = request.user)
    return render(request, 'main_detail.html' , {'fotds':fotds,'ootds':ootds,'motds':motds,'totds':totds,'year':year,'month':month,'day':day})


@login_required(login_url="/registration/login")
def new_totd(request):
    if request.method == "POST":
        new_totd = Totd.objects.create(
            title=request.POST["title"],
            content=request.POST["content"],
            day = request.POST['day'],
            author=request.user,
        )
        return redirect("detail_totd", totd_pk=new_totd.pk)
    return render(request, "totd_base.html")

def edit_totd(request, totd_pk):
    totd = Totd.objects.get(pk=totd_pk)

    if request.method == 'POST':
        Totd.objects.filter(pk=totd_pk).update(
            title=request.POST['title'],
            content=request.POST['content'],
            day = request.POST['day'],
            author=request.user,
        )
        return redirect('detail_totd', totd_pk)

    return render(request, 'totd_edit.html', {'totd': totd})

def delete_totd(request, totd_pk):
    totd = Totd.objects.get(pk=totd_pk)
    totd.delete()
    return redirect('home')

def detail_totd(request, totd_pk):
    totd = Totd.objects.get(pk=totd_pk)

    if request.method == 'POST':
        return redirect('detail_totd', totd_pk)

    return render(request, 'totd_detail.html', {'totd': totd})

#MOTD
@login_required(login_url="/registration/login")
def new_motd(request):
    if request.method == "POST":
        new_motd = Motd.objects.create(
            title=request.POST["title"],
            content=request.POST["content"],
            day=request.POST["day"],
            author=request.user,
        )
        return redirect("detail_motd", new_motd.pk)
    return render(request, "motd_new.html")

def edit_motd(request, motd_pk):
    motd = Motd.objects.get(pk=motd_pk)

    if request.method == 'POST':
        Motd.objects.filter(pk=motd_pk).update(
            title=request.POST["title"],
            content=request.POST["content"],
            day=request.POST["day"],
            author=request.user,
        )
        return redirect('detail_motd', motd_pk)

    return render(request, 'motd_edit.html', {'motd': motd})


def delete_motd(request, motd_pk):
    motd = Motd.objects.get(pk=motd_pk)
    motd.delete()
    return redirect('home')

def detail_motd(request, motd_pk):
    motd = Motd.objects.get(pk=motd_pk)

    if request.method == 'POST':
        return redirect('motd_detail', motd_pk)

    return render(request, 'motd_detail.html', {'motd': motd})

def regist_page(request):
    return render(request, "regist_page.html")

#FOTD
@login_required(login_url="/registration/login")
def new_fotd(request):
    if request.method == "POST":
        new_fotd = Fotd.objects.create(
            title=request.POST["title"],
            content=request.POST["content"],
            day = request.POST['day'],
            author=request.user,
    
        )
        return redirect("detail_fotd", new_fotd.pk)
    return render(request, "fotd_new.html")

def edit_fotd(request, fotd_pk):
    fotd = Fotd.objects.get(pk=fotd_pk)

    if request.method == 'POST':
        Fotd.objects.filter(pk=fotd_pk).update(
            title=request.POST["title"],
            content=request.POST["content"],
            day=request.POST["day"],
            author=request.user,
        )
        return redirect('detail_fotd', fotd_pk)

    return render(request, 'fotd_edit.html', {'fotd': fotd})


def delete_fotd(request, fotd_pk):
    fotd = Fotd.objects.get(pk=fotd_pk)
    fotd.delete()
    return redirect('home')

def detail_fotd(request, fotd_pk):
    fotd = Fotd.objects.get(pk=fotd_pk)

    if request.method == 'POST':
        return redirect('detail_fotd', fotd_pk)

    return render(request, 'fotd_detail.html', {'fotd': fotd})

#OOTD
@login_required(login_url="/registration/login")
def new_ootd(request):
    if request.method == "POST":
        new_ootd = Ootd.objects.create(
            title=request.POST["title"],
            content=request.POST["content"],
            author=request.user,
            day = request.POST['day'],
        )
        return redirect("detail_ootd", new_ootd.pk)
    return render(request, "ootd_new.html")

def edit_ootd(request, ootd_pk):
    ootd = Ootd.objects.get(pk=ootd_pk)

    if request.method == 'POST':
        Ootd.objects.filter(pk=ootd_pk).update(
            title=request.POST["title"],
            content=request.POST["content"],
            day=request.POST["day"],
            author=request.user,
        )
        return redirect('detail_ootd', ootd_pk)

    return render(request, 'ootd_edit.html', {'ootd': ootd})


def delete_ootd(request, ootd_pk):
    ootd = Ootd.objects.get(pk=ootd_pk)
    ootd.delete()
    return redirect('home')

def detail_ootd(request, ootd_pk):
    ootd = Ootd.objects.get(pk=ootd_pk)

    if request.method == 'POST':
        return redirect('detail_ootd', ootd_pk)

    return render(request, 'ootd_detail.html', {'ootd': ootd})

def signup(request):
    if (request.method == 'POST'):
        found_user = User.objects.filter(username=request.POST['username'])
        if (len(found_user) > 0):
            error = 'username이 이미 존재합니다'
            return render(request, 'registration/signup.html', {'error': error})

        new_user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
        #auth.login(request, new_user)  # 회원가입 정상적으로 진행한 뒤에, 자동으로 로그인

        return redirect('profile_new')

    return render(request, 'registration/signup.html')


def login(request):
    if (request.method == "POST"):
        found_user = auth.authenticate(
            username=request.POST["username"],
            password=request.POST["password"]
        )

        if (found_user is None):
            error = "아이디 또는 비밀번호가 틀렸습니다"
            return render(request, "registration/login.html", {
                'error': error
            })

        auth.login(request, found_user)
        return redirect("home_totd")

    return render(request, "registration/login.html")


def logout(request):
    auth.logout(request)

    return redirect('home_totd')


def profile_edit(request, user_pk):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        Profile.objects.filter(user=request.user).update(
            user=request.user,
            nickname=request.POST["nickname"],
            introduction=request.POST["introduction"],
            birthday=request.POST["birthday"],
        )
        return redirect("regist_page")
    return render(request, "my_profile_edit.html", {"profile": profile})

def profile_new(request):
    if request.method == "POST":
        Profile.objects.create(
            user=request.user,
            nickname=request.POST["nickname"],
            introduction=request.POST["introduction"],
            birthday=request.POST["birthday"],
        )
        return redirect("home_totd")
    return render(request, "my_profile_new.html")

#authorProfile

def author_profile(request, fotd_pk, ootd_pk): #if else 로 
    fotd_post = Fotd.objects.get(pk=fotd_pk)
    fotd_profile = Profile.objects.get(user=fotd_post.author)
    ootd_post = Ootd.objects.get(pk=ootd_pk)
    ootd_profile = Profile.objects.get(user=ootd_post.author)
    return render(request, "author_profile.html", {
        "fotd_profile": fotd_profile,
        "ootd_profile": ootd_profile
        })


#likes - ootd fotd
@csrf_exempt
def like_fotd(request):
    if request.method == 'POST':
        request_body = json.loads(request.body)
        fotd_pk = request_body['fotd_pk']

        existing_like = Like_Fotd.objects.filter(
            fotd = Fotd.objects.get(pk=fotd_pk),
            user = request.user
        )
        
        #좋아요 취소
        if existing_like.count() > 0:
            existing_like.delete()

        #좋아요 생성
        else:
            Like_Fotd.objects.create(
                fotd = Fotd.objects.get(pk=fotd_pk),
                user = request.user
            )
        
        fotd_likes = Like_Fotd.objects.filter(
            fotd = Fotd.objects.get(pk=fotd_pk)
        )

        response = {
            'like_count_fotd': fotd_likes.count()
        }

        return HttpResponse(json.dumps(response))

@csrf_exempt
def like_ootd(request):
    if request.method == 'POST':
        request_body = json.loads(request.body)
        ootd_pk = request_body['ootd_pk']

        existing_like = Like_Ootd.objects.filter(
            ootd = Ootd.objects.get(pk=ootd_pk),
            user = request.user
        )
        
        #좋아요 취소
        if existing_like.count() > 0:
            existing_like.delete()

        #좋아요 생성
        else:
            Like_Ootd.objects.create(
                ootd = Ootd.objects.get(pk=ootd_pk),
                user = request.user
            )
        
        ootd_likes = Like_Ootd.objects.filter(
            ootd = Ootd.objects.get(pk=ootd_pk)
        )

        response = {
            'like_count_ootd': ootd_likes.count()
        }

        return HttpResponse(json.dumps(response))