from django.shortcuts import render,redirect
from login.models import Member 
from event.models import Event,EventImage

def show_map(request):
    prefer_city = Member.objects.get(id=request.user.pk).city
    prefer_gu = Member.objects.get(id=request.user.pk).gu
    ctx = {
        'prefer_city' : prefer_city,
        'prefer_gu' : prefer_gu,
    }
    return render(request,'location/map_list.html',ctx)

def search_map(request):
    if request.method == "POST":
        selected_city = request.POST.get('selected_city') 
        selected_gu = request.POST.get('selected_gu') 
        if selected_city == '시' or selected_gu == '구':
            return redirect('login:main')
        events = Event.objects.all()
        event_images = EventImage.objects.all()

        ctx = {
            'selected_city' : selected_city,
            'selected_gu' : selected_gu,
            'events' : events,
            'event_images' : event_images,
        }
    
    return render(request,'location/search_map.html',ctx)

