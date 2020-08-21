from django.contrib.auth.decorators import login_required
from django.core.checks import messages
import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth import login as auth_login
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from django.forms import modelformset_factory

from event.models import Event, Tag
from helloevent import settings
from django.urls import reverse

from login.forms import MemberForm, CreatorForm
from login.models import Creator, Member

from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from event.forms import EventForm, ImageForm, EventImage


def login(request):
    return render(request, 'login/login.html')


def main(request):
    user = request.user
    events = Event.objects.none()
    today = datetime.today()
    if user.is_authenticated:
        user_is = True
        creators = user.like_creators.all()
        for creator in creators:
            q = creator.events.filter(end_date_time__gt=today)
            events = events | q
    else:
        user_is = False
        creators = Creator.objects.none()
    print(creators)

    ctx = {
        'creators':creators,
        'user_is':user_is,
        'events':events,
    }
    return render(request, 'login/main.html', ctx)


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

    like_creators = Member.objects.get(id=request.user.pk).like_creators.all()
    today = datetime.today()
    events = Event.objects.none()
    print(like_creators)
    for creator in like_creators:
        q = creator.events.filter(end_date_time__gt=today)
        events = events | q
    print(events)
    try:
        creators = Member.objects.get(id=request.user.pk).creator
    except:
        creators = None
        # creator 가 없을 때 발생하는 RelatedObjectDoesNotExist 예외 처리
    return render(request, 'login/mypage.html', {
        'user': user,
        'creators': creators,
        'like_creators':like_creators,
        'events':events,
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
    events = creator.events.all()

    return render(request, 'login/creator_mypage.html', {
        'creator': creator,
        'events': events,
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
    if request.method == 'POST':
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


# 크리에이터 계정 삭제
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


# 로그인 중복확인
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


# 닉네임 중복확인
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


# 이메일 중복확인
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


# 일반, 소셜로그인 계정 삭제 (해당 user의 pk값으로 찾아 데이터에서 삭제)
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
    print(pk)
    creator = get_object_or_404(Event, pk=pk).creator
    print(creator)
    if request.user in creator.like_users.all():
        creator.like_users.remove(request.user)
        message = "좋아요 취소"
    else:
        creator.like_users.add(request.user)
        message = "좋아요"
    ctx = {
        'like_count':creator.like_count,
        'message':message,
        'creator_name':creator.creator_name,
    }
    return HttpResponse(json.dumps(ctx), content_type="application/json")



def event_update(request, pk):
    ImageFormSet = modelformset_factory(EventImage, form=ImageForm, extra=0)
    event = get_object_or_404(Event, pk=pk)  # object
    event_image = event.eventimage_set.all()  # queryset
    event_tags = event.tags.all()
    # print(event_image)
    id = event.creator.pk

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=event_image)

        if form.is_valid() and image_formset.is_valid():
            for image in event_image:
                image.delete()

            event = form.save(commit=False)
            event.save()

            for form in image_formset.cleaned_data:
                print(image_formset.cleaned_data)
                if form:
                    image = form['image']
                    photo = EventImage(event=event, image=image)
                    photo.save()

            for tag in event_tags:
                tag.delete()

            tags = request.POST['tags'].split(',')
            for tag in tags:
                tag = tag.strip()
                if tag == "":
                    continue
                _tag, _ = Tag.objects.get_or_create(name=tag)
                event.tags.add(_tag)

            # location = request.POST['location']
            start_date_time = request.POST['start_date_time']
            end_date_time = request.POST['end_date_time']
            # event.location = location
            event.start_date_time = start_date_time
            event.end_date_time = end_date_time
            event.save()

            url = reverse('login:creator_mypage', kwargs={'pk': id})
            return redirect(to=url)
    else:
        form = EventForm(instance=event)
        image_formset = ImageFormSet(queryset=event_image)
        starttime = event.start_date_time
        endtime = event.end_date_time
        starttime_value = transfer_time(starttime)
        endtime_value = transfer_time(endtime)

        return render(request, 'login/event_update.html', {
            'form': form,
            'image_formset': image_formset,
            'event': event,
            'tags': event_tags,
            'starttime_value': starttime_value,
            'endtime_value': endtime_value,
        })


def transfer_time(time):
    if len(str(time.month)) == 1:
        time_month = "0" + str(time.month)
    else:
        time_month = str(time.month)
    if len(str(time.day)) == 1:
        time_day = "0" + str(time.day)
    else:
        time_day = str(time.day)
    if len(str(time.hour)) == 1:
        time_hour = "0" + str(time.hour)
    else:
        time_hour = str(time.hour)
    if len(str(time.minute)) == 1:
        time_minute = "0" + str(time.minute)
    else:
        time_minute = str(time.minute)
    transfered_time = str(time.year) + "-" + time_month + "-" + time_day + "T" + time_hour + ":" + time_minute
    return transfered_time


