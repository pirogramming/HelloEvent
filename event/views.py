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
from django.conf import settings

from login.models import Creator, Member


@login_required
def register_event(request):
    ImageFormSet = modelformset_factory(EventImage, form=ImageForm, extra=3)

    if request.method == 'POST':
        event_form = EventForm(request.POST)
        tags = request.POST['tag'].split(',')
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=EventImage.objects.none())
        if event_form.is_valid() and image_formset.is_valid():
            event = event_form.save(commit=False)
            event.creator = Member.objects.get(id=request.user.pk).creator
            event.save()
            for tag in tags:
                print(tag)
                tag = tag.strip()
                Tag.objects.create(name=tag, event=event)

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
        form = EventForm()
        formset = ImageFormSet(queryset=EventImage.objects.none())
        cxt = {
            'form':form,
            'formset':formset,
            'creator':creator,
        }
        return render(request, 'event/event_register.html', cxt)

def creator_detail(request, pk):
    event = Event.objects.get(pk=pk)
    creator = event.creator
    # Creator.objects.get(id=1).event_set.get(pk=1)
    ctx = {
        # 'event':event,
        # 'creator':event.creator,
        # 'event_name' : event.event_name,
        # 'genre' : event.genre,
        # 'creator_photo' : creatordetail.creator_photo,
        # 'creator':creator,
        'event':event,
        'creator':creator
    }
    return render(request, 'event/creator_event_detail.html', ctx)
