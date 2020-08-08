from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.shortcuts import render

# Create your views here.
from django.template import RequestContext

from HelloEvent.event.forms import ImageForm, EventForm
from HelloEvent.event.models import Event_Image


@login_required
def event(request, pk):
    ImageFormSet = modelformset_factory(Event_Image, form = ImageForm, extra=4)
    if request.method == "POST":
        form = EventForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset = Event_Image.objects.none())
        if form.is_valid() and formset.is_valid():
            event = form.save(commit=False)
            for form in formset.cleaned_data:
                image = form['image']
                photo = Event_Image(event = event, image = image);
                photo.save()
            messages.success(request, 'Event 사진 업로드 성공')
        else:
            print form.error, formset.error
    else:
        form = EventForm
        formset = ImageForm(queryset = Event_Image.objects.none())
    return render(request, 'event/event_register.html',
                  context={
                      'eventform' : form,
                      'formset' : formset,
                  }, context_instance=RequestContext(request)
                  )
