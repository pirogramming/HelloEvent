from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import modelformset_factory, inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.template import RequestContext

from event.forms import ImageForm, EventForm
from event.models import EventImage, Event
from django.conf import settings



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

@login_required
def register_event(request):
    ImageFormSet = modelformset_factory(EventImage, form=ImageForm, extra=2)

    if request.method == 'POST':
        event_form = EventForm(request.POST)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=EventImage.objects.none())
        if event_form.is_valid() and image_formset.is_valid():
            event = event_form.save(commit=False)
            event.save()
            for form in image_formset.cleaned_data:
                image = form['image']
                photo = EventImage(event=event, image=image)
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
