from django.shortcuts import render

def showmap_view(request):
    return render(request,'location/index.html')
