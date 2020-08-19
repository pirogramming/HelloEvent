from django.contrib.auth.decorators import login_required
from django.core.checks import messages
import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth import login as auth_login
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers

from event.models import Event
from helloevent import settings
from django.urls import reverse

from login.forms import MemberForm, CreatorForm
from login.models import Creator, Member

from django.views.decorators.csrf import csrf_exempt






def login(request):
    return render(request, 'login/login.html')

def main(request):
    return render(request, 'login/main.html')

def signup_general(request):
    return render(request, 'login/signup.html')


# def login_signup(request):
#     if request.method == 'POST':
#         form = MemberForm(request.POST, request.FILES)
#         if form.is_valid():
#             member = form.save(commit=False)
#             member.save()   # ModelForm에선 2번 저장되어서 member.save()를 빼줘야 Integrity Error가 안뜨는듯..?
#             pk = member.id
#             url = reverse('login:main')
#             return redirect(to=url)
#     else:
#         form = MemberForm
#     return render(request, 'login/login_signup.html', {
#         'form': form,
#     })


def signup(request, pk):
    url = reverse('login:main')

    user = Member.objects.get(id=pk)

    if user.nickname != '':
        return redirect(to=url)
    else:
        if request.method == 'GET':
            context = {
                'user': user
            }
            return render(request, 'login/login_signup.html', context=context)

        nickname = request.POST['nickname']
        city = request.POST['city']
        gu = request.POST['gu']

        user.nickname = nickname
        user.city = city
        user.gu = gu
        user.save()

        return redirect(to=url)


def mypage(request, pk):
    user = get_object_or_404(Member, pk=pk)
    try:
        creator = Member.objects.get(id=request.user.pk).creator
    except:
        creator = None
        # creator 가 없을 때 발생하는 RelatedObjectDoesNotExist 예외 처리
    return render(request, 'login/mypage.html', {
        'user': user,
        'creator': creator,
    })


def login_update(request, pk):
    user = Member.objects.get(id=pk)
    if request.method == 'GET':
        context = {
            'user': user
        }
        return render(request, 'login/login_update.html', context=context)

    nickname = request.POST['nickname']
    city = request.POST['city']
    gu = request.POST['gu']

    user.nickname = nickname
    user.city = city
    user.gu = gu
    user.save()

    return redirect('login:mypage', pk)

    # if request.method == 'POST':
    #     form = MemberForm(request.POST, instance=member)
    #     if form.is_valid():
    #         member = form.save(commit=False)
    #         member.save()
    #         pk = member.id
    #         url = reverse('login:mypage', kwargs={'pk': pk})
    #         return redirect(to=url)
    # else:
    #     form = MemberForm(instance=member)
    # context = {'form': form}
    # return render(request, 'login/login_signup.html', context)


# def signup(request):
#     return render(request, 'login/login_signup.html')

def create_creator(request):
    if request.method == 'POST':
        form = CreatorForm(request.POST, request.FILES)
        if form.is_valid():
            # print(1)
            creator = form.save(commit=False)
            creator.member = Member.objects.get(id=request.user.pk)
            creator.save()
            print(2)
            return redirect("event:event_register")
    else:
        form = CreatorForm()
        cxt = {
            'form': form,
        }
        return render(request, 'login/enroll_creator.html', cxt)


def creator_mypage(request, pk):
    # creator = get_object_or_404(Creator, pk=pk)
    creator = Member.objects.get(id=request.user.pk).creator
    return render(request, 'login/creator_mypage.html', {
        'creator': creator,
    })


def creator_update(request, pk):

    temp = get_object_or_404(Creator, pk=pk)

    if request.method == 'POST':
        form = CreatorForm(request.POST, request.FILES, instance=temp)
        if form.is_valid():
            creator = form.save(commit=False)
            creator.save()
            url = reverse('login:creator_mypage', kwargs={'pk': pk})
            return redirect(to=url)
    else:
        form = CreatorForm(instance=temp)
    return render(request, 'login/creator_update.html', {
        'form': form
    })

def signup_form(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = Member.objects.create_user(
                request.POST['username'],
                nickname=request.POST['nickname'],
                password=request.POST['password1'],
                email=request.POST['email'],
                city=request.POST['city'],
                gu=request.POST['gu'],
            )
            # username_check = auth.authenticate(request, username=request.POST['username'])
            # nickname_check = auth.authenticate(request, nickname=request.POST['nickname'])
            #
            # if username_check is not None:
            #     auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("login:login")
    return render(request, 'login/signup_form.html')

def login_form(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("login:login")
        else:
            # messages.error(request, 'username or password is incorrect')
            # return redirect("login:login")
            return render(request, 'login/login_form.html', {
                'error': 'username or password is incorrect'
            })
    else:
        return render(request, 'login/login_form.html')


#크리에이터 계정 삭제
# def creator_delete(request, pk):
#     if request.method == 'POST':
#         creator = Member.objects.get(id=request.user.pk).creator
#         creator.delete()
#         return redirect("login:mypage", request.id)
def creator_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    creator = member.creator
    # creator = Member.objects.get(id=request.user.pk).creator
    if creator:
        creator.delete()
        return redirect('login:mypage', pk)
    return redirect("login:creator_mypage", pk)  

#로그인 중복확인
def id_overlap_check(request):
    username = request.GET.get('username')
    try:
        # 중복 검사 실패
        user = Member.objects.get(username=username)
    except:
        # 중복 검사 성공
        user = None
    if user is None:
        overlap = 'pass'
    else:
        overlap = 'fail'
    context = {'overlap': overlap}
    return JsonResponse(context)

#닉네임 중복확인
def nickname_lap_check(request):
    nickname = request.GET.get('nickname')
    try:
        # 중복 검사 실패
        user = Member.objects.get(nickname=nickname)
    except:
        # 중복 검사 성공
        user = None
    if user is None:
        lap = 'pass'
    else:
        lap = 'fail'
    context = {'lap': lap}
    return JsonResponse(context)

#이메일 중복확인
def email_lap_check(request):
    email = request.GET.get('email')
    try:
        # 중복 검사 실패
        user = Member.objects.get(email=email)
    except:
        # 중복 검사 성공
        user = None
    if user is None:
        lap = 'pass'
    else:
        lap = 'fail'
    context = {'lap': lap}
    return JsonResponse(context)

#일반, 소셜로그인 계정 삭제 (해당 user의 pk값으로 찾아 데이터에서 삭제)
def user_delete(request, pk):
    user = get_object_or_404(Member, pk=pk)
    if user:
        user.delete()
        return render(request, "login/main.html")  
    return redirect('login:mypage', pk)

@login_required
@csrf_exempt
def like(request):
    pk = request.POST.get('pk', None)
    print(0)
    creator = get_object_or_404(Event, id=pk).creator
    print(creator)
    if request.user in creator.like_users.all():
        print(1)
        creator.like_users.remove(request.user)
        message = "좋아요 취소"
    else:
        print(2)
        creator.like_users.add(request.user)
        message = "좋아요"

    ctx = {
        'like-count':creator.like_count,
        'message':message,
        'creator_name':creator.creator_name,
    }

    return HttpResponse(json.dumps(ctx), content_type="application/json")



