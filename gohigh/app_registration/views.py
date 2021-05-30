from django.shortcuts import render, redirect
from .models import Post, Profile
from django.contrib.auth.models import User
from django.contrib import auth

# SMTP 관련 인증
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from django.contrib.auth.decorators import login_required

# Create your views here.
def start(request):
        return render(request, 'start.html')

@login_required(login_url='/registration/login')
def presetting(request):
    if request.method == 'POST':
        profiles = Profile.objects.create(
            nickname = request.POST['nickname'],
            location = request.POST['location'],
            # point = request.POST['point'],
            university = request.POST['university'],
            department = request.POST['department'],
            # likeStudy = request.POST['likeStudy'],
            # likeGift = request.POST['likeGift'],
            # myGift = request.POST['myGift'],
        )
        return redirect('studyhome', profiles.pk)
    return render(request, 'presetting.html')

def temp_home(request):
    profiles = Profile.objects.all()
    return render(request, 'temp_home.html', {'profiles': profiles})

def login2(request, Profile_pk):
    if request.method == 'POST':
        Profile.objects.filter(pk=Profile_pk).update(
            likeStudy = request.POST['likeStudy'],
        )
        return redirect('login')

    return render(request, 'login2.html')

# Create your views here.
def signup(request):
    # 포스트 방식으로 들어오면
    if request.method == 'POST':

        found_user = User.objects.filter(username = request.POST['username'])
        
        if len(found_user)>0:
            error = '해당 아이디는 이미 존재 다른거 쓰셈'
            return render(request, 'registrations/signup.html', {'error':error})
        
        elif request.POST['password1'] ==request.POST['password2']:
            send_email(request)
            return render(request,'registrations/rendering.html')
        
    return render(request, 'registrations/signup.html')

    # 포스트 방식 아니면 페이지 띄우기
    # return render(request, 'registrations/signup.html')

def send_email(request):
    user = User.objects.create_user(
        username=request.POST['username'], 
        password=request.POST['password1'])
    
    user.is_active = False # 유저 비활성화
    user.save()
    current_site = get_current_site(request) 
    message = render_to_string('account/activation_email.html', 
            {
            'user': user,
            # 'domain': current_site.domain,
            
            'domain': 'https://bde30d1d9341.ngrok.io',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
            } 
        )
    mail_title = "계정 활성화 확인 이메일"
    mail_to = request.POST["id"] + "@korea.ac.kr"
    email = EmailMessage(mail_title, message, to=[mail_to])
    email.content_subtype = 'html'
    email.send()

def login(request):
    # 포스트 방식으로 들어오면
    if request.method == 'POST':
        # 정보 가져와서 
        username = request.POST['username']
        password = request.POST['password']
        # 로그인
        user = auth.authenticate(request, username=username, password=password)
        # 성공
        if user is not None:
            auth.login(request, user)
            return redirect('studyhome')
        # 실패
        else:
            return render(request, 'registrations/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'registrations/login.html')

def logout(request):
    # 포스트 방식으로 들어오면
    if request.method == 'POST':
        # 유저 로그아웃
        auth.logout(request)
        return redirect('studyhome')
    return render(request, 'registrations/signup.html')

# 계정 활성화 함수(토큰을 통해 인증)
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExsit):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect("presetting")
    else:
        return render(request, 'presetting.html', {'error' : '계정 활성화 오류'})
    return 