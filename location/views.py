from django.shortcuts import render

def show_map(request):
    return render(request,'location/index.html')
