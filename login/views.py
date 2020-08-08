from django.shortcuts import render, redirect

def login(request):
    return render(request, 'login/login.html')

def main(request):
    return render(request, 'login/main.html')
