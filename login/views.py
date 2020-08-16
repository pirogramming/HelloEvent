from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth import login as auth_login
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from helloevent import settings
from django.urls import reverse

from login.forms import MemberForm, CreatorForm
from login.models import Creator, Member


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
        console.log(user.pk)
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
    url = reverse('login:main')
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

    return redirect(to=url)

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
    creator = get_object_or_404(Creator, pk=pk)
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
def delete_creator(request):
    if request.method == 'POST':
        creator = Member.objects.get(id=request.user.pk).creator
        creator.delete()
        return redirect("login:mypage", request.id)

