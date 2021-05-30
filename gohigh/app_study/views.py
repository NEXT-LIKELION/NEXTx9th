from django.shortcuts import render, redirect
from .models import Study, Member
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

# Create your views here.

# home, edit- accept, deny, deny_apply, detail, new, apply,

def studyhome(request):
    studys = Study.objects.all()

    return render(request, 'studyhome.html', {'studys':studys})

def new(request):
    if request.method =='POST':
        new_study = Study.objects.create(
            name = request.POST['name'],
            num_member = request.POST['num_member'],
            max_member = request.POST['max_member'],
            location = request.POST['location'],
            period = request.POST['period'],
            content = request.POST['content'],
            category = request.POST['category']
        )
        return redirect('detail', new_study.pk)

    return render(request, 'new.html')

def detail(request, study_pk):
    study = Study.objects.get(pk=study_pk)

    return render(request, 'detail.html', {'study':study})

def category(request, category_name):
    studys = Study.objects.filter(category = category_name)
    return render(request, 'studyhome.html', {'studys':studys})

@csrf_exempt
def join(request):
    if request.method == "POST":
        request_body = json.loads(request.body)
        study_pk = request_body['study_pk']

        existing_member = Member.objects.filter(
            study = Study.objects.get(pk=study_pk),
            user = request.user
        )

        if existing_member.count() > 0 :
            pass
        #Member 생성
        else :
            Member.objects.create(
                study = Study.objects.get(pk=study_pk),
                user = request.user,
                is_accepted = False
            )
        
    join_count = Member.objects.filter(
        study = Study.objects.get(pk=study_pk)
    )

    response = {
        'join_count' : join_count.count()
    }

    return HttpResponse(json.dumps(response))

