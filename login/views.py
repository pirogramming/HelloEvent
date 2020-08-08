from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.urls import reverse

from .forms import MemberForm

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
            url = reverse('none', kwargs={'pk': pk})
            return redirect(to=url)
    else:
        form = MemberForm
    return render(request, 'login/login_signup.html', {
        'form': form,
    })

