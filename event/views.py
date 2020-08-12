from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import modelformset_factory, inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.template import RequestContext

from event.forms import ImageForm, EventForm
from event.models import EventImage, Event
from django.conf import settings

from comment.models import Comment



# @login_required
# def register_event(request):
#     ImageFormSet = inlineformset_factory(Event, EventImage, form=ImageForm, extra=2)
#     if request.method == "POST":
#         form = EventForm(request.POST)
#         formset = ImageFormSet(request.POST, request.FILES)
#         if form.is_valid() and formset.is_valid():
#             event = form.save(commit=False)
#             #event.creator = request.user
#
#             with transaction.atomic():
#                 event.save()
#                 formset.instance = event
#                 formset.save()
#                 messages.success(request, 'Event 사진 업로드 성공')
#                 return redirect('login:login')
#
#     else:
#         form = EventForm()
#         formset = ImageFormSet()
#     return render(request, 'event/event_register.html',
#                   context={
#                       'eventform': form,
#                       'formset': formset,
#                   })
from login.models import Creator, Member


@login_required
def register_event(request):
    ImageFormSet = modelformset_factory(EventImage, form=ImageForm, extra=3)

    if request.method == 'POST':
        event_form = EventForm(request.POST)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=EventImage.objects.none())
        if event_form.is_valid() and image_formset.is_valid():
            event = event_form.save(commit=False)
            event.creator = Member.objects.get(id=request.user.pk).creator
            print(1)
            event.save()
            for form in image_formset.cleaned_data:
                print(image_formset.cleaned_data)
                if form :
                    image = form['image']
                    photo = EventImage(event=event, image=image)
                    print(2)
                    photo.save()
        return redirect('login:login')
    else:
        form = EventForm()
        formset = ImageFormSet(queryset=EventImage.objects.none())
        cxt = {
            'form':form,
            'formset':formset,
        }
        return render(request, 'event/event_register.html', cxt)

def creator_detail(request, pk):
    event = Event.objects.get(pk=pk)
    creator = event.creator
    comments = creator.comments.all()
    ctx = {
        'event':event,
        'creator':creator,
        'comments':comments,
    }
    return render(request, 'event/creator_event_detail.html', ctx)