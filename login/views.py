from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout as auth_logout
from django.urls import reverse

from .forms import MemberForm
from .models import Member, Creator


def login(request):
    return render(request, 'login/login.html')


def main(request):
    return render(request, 'login/main.html')


def login_signup(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save(commit=False)
            member.save()
            pk = member.id
            url = reverse('login:mypage', kwargs={'pk': pk})
            return redirect(to=url)
    else:
        form = MemberForm
    return render(request, 'login/login_signup.html', {
        'form': form,
    })


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
