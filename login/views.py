from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from helloevent import settings
from django.urls import reverse

from login.forms import MemberForm
from login.models import Creator, Member


def login(request):
    # pk = request.GET['pk']
    # nickname = request.GET['nickname']
    # if nickname == '':
    return render(request, 'login/login.html')
    # else:
    #     return render(request, 'login/login_signup.html', pk)


def main(request):
    return render(request, 'login/main.html')


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


def login_signup(request, pk):
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
    member = get_object_or_404(Member, pk=pk)
    print(member)
    return render(request, 'login/mypage.html', {
        'member': member,
    })


def login_update(request, pk):
    member = Member.objects.get(id=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            member = form.save(commit=False)
            member.save()
            pk = member.id
            url = reverse('login:mypage', kwargs={'pk': pk})
            return redirect(to=url)
    else:
        form = MemberForm(instance=member)
    context = {'form': form}
    return render(request, 'login/login_signup.html', context)

# def signup(request):
#     return render(request, 'login/login_signup.html')

def create_creator(request):
    if request.method == 'POST':
        form = CreatorForm(request.POST, request.FILES)
        if form.is_valid():
            print(1)
            creator = form.save(commit=False)
            creator.member = Member.objects.get(id=request.user.pk)
            creator.save()
            return redirect("event:event_register")
    else:
        form = CreatorForm()
        cxt={
            'form':form,
        }
        return render(request, 'login/enroll_creator.html', cxt)








