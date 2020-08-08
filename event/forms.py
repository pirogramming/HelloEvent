from django import forms

from event.models import Event, Event_Image


class EventForm(forms.ModelForm):
    event_name = forms.CharField(max_length=200, required=False)
    desc = forms.CharField(required=False)
    #genre = ch

    class Meta:
        model = Event
        fields = ('event_name', 'desc', )

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label = "Image")

    class Meta:
        model = Event_Image
        fields = ('image',)