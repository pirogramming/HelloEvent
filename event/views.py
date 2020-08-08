from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.shortcuts import render

# Create your views here.
from django.template import RequestContext

from event.forms import ImageForm, EventForm
from event.models import EventImage


@login_required
def register_event(request, pk):
    ImageFormSet = modelformset_factory(EventImage, form=ImageForm, extra=4)
    if request.method == "POST":
        form = EventForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=EventImage.objects.none())
        if form.is_valid() and formset.is_valid():
            event = form.save(commit=False)
            for form in formset.cleaned_data:
                image = form['image']
                photo = EventImage(event = event, image = image);
                photo.save()
            messages.success(request, 'Event 사진 업로드 성공')
        else:
            print(form.error, formset.error)
    else:
        form = EventForm()  # TODO : fix me!
        formset = ImageForm(queryset=EventImage.objects.none())
    return render(request, 'event/event_register.html',
                  context={
                      'eventform': form,
                      'formset': formset,
                  }
                  )
