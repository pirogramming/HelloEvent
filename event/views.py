from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import modelformset_factory, inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.template import RequestContext

from event.forms import ImageForm, EventForm
from event.models import EventImage, Event, Tag
from location.forms import LocationForm
from django.conf import settings

from login.models import Creator, Member
from comment.models import Comment

from django.db.models import Q
from datetime import datetime

class RelatedObjectDoesNotExist(Exception):
    def __init__(self):
        self.msg = '크리에이터 존재 오류'

    def __str__(self):
        return self.msg

# @login_required
# def register_event(request):
#     try:
#         if request.user.creator is None:
#             raise RelatedObjectDoesNotExist("오류!")
#         else:
#             ImageFormSet = modelformset_factory(EventImage, form=ImageForm, extra=3)
#
#             if request.method == 'POST':
#                 event_form = EventForm(request.POST)
#                 tags = request.POST['tag'].split(',')
#                 image_formset = ImageFormSet(request.POST, request.FILES, queryset=EventImage.objects.none())
#                 if event_form.is_valid() and image_formset.is_valid():
#                     event = event_form.save(commit=False)
#                     event.creator = Member.objects.get(id=request.user.pk).creator
#                     event.save()
#                     for tag in tags:
#                         print(tag)
#                         tag = tag.strip()
#                         Tag.objects.create(name=tag, event=event)
#
#                     for form in image_formset.cleaned_data:
#                         print(image_formset.cleaned_data)
#                         if form :
#                             image = form['image']
#                             photo = EventImage(event=event, image=image)
#                             print(2)
#                             photo.save()
#                 return redirect('login:login')
#             else:
#                 creator = request.user.creator
#                 form = EventForm()
#                 formset = ImageFormSet(queryset=EventImage.objects.none())
#                 cxt = {
#                     'form':form,
#                     'formset':formset,
#                     'creator':creator,
#                 }
#                 return render(request, 'event/event_register.html', cxt)
#     except RelatedObjectDoesNotExist:
#         return redirect('login:create_creator')



def register_event(request):
    try:
        if not request.user.is_authenticated:
            return redirect("login:create_creator")
        print('출력은 되는거니')
        if Member.objects.get(id=request.user.pk).creator is None:
            raise RelatedObjectDoesNotExist

        ImageFormSet = modelformset_factory(EventImage, form=ImageForm, extra=3)

        if request.method == 'POST':
            print("post 시작")
            event_form = EventForm(request.POST)
            tags = request.POST['tag'].split(',')
            image_formset = ImageFormSet(request.POST, request.FILES, queryset=EventImage.objects.none())
            location_form = LocationForm(request.POST)
            if event_form.is_valid() and image_formset.is_valid() and location_form.is_valid() :
                event = event_form.save(commit=False)
                location = location_form.save(commit=False)
                location.save()
                event.start_date_time = request.POST['start_date_time']
                event.end_date_time = request.POST['end_date_time']
                event.creator = Member.objects.get(id=request.user.pk).creator
                event.location = location
                event.save()
                print("세이브가 되었을까?????")
                for tag in tags:
                    print(tag)
                    tag = tag.strip()
                    _tag, _ = Tag.objects.get_or_create(name=tag)
                    event.tags.add(_tag)
                for form in image_formset.cleaned_data:
                    print(image_formset.cleaned_data)
                    if form :
                        image = form['image']
                        photo = EventImage(event=event, image=image)
                        print(2)
                        photo.save()
                return redirect('login:login')
        else:
            creator = request.user.creator
            location = LocationForm()
            form = EventForm()
            formset = ImageFormSet(queryset=EventImage.objects.none())
            cxt = {
                'form':form,
                'formset':formset,
                'location':location,
                'creator':creator,
            }
            return render(request, 'event/event_register.html', cxt)
    except Exception as e:
        print('예외 발생 ', e)
        return redirect("login:create_creator")

def creator_detail(request, pk):
    event = Event.objects.get(pk=pk)
    creator = event.creator
    events = creator.events.all()
    comments = creator.comments.all()
    comment_num = comments.count()
    images = event.eventimage_set.all()
    image_num = event.eventimage_set.count()
    comment_3 = creator.comments.order_by('-created_at')[:3]
    ctx = {
        'event':event,
        'events':events,
        'creator':creator,
        'comments':comments,
        'comment_3':comment_3,
        'comment_num':comment_num,
        'images':images,
        'image_num':image_num,
    }
    return render(request, 'event/creator_event_detail.html', ctx)

def search_result(request):
    # startdate = datetime.today()
    # endtime = startdate + datetime.timedelta()
    if 'search_data' in request.GET:
        data = request.GET['search_data']
        eventsall = Tag.objects.all().filter(Q(name__contains=data))
        print(eventsall)
    # events = eventsall.filter('start_date_time')
    ctx = {
        'events':eventsall,
    }
    return render(request, "event/search_result.html", ctx)
