from django import forms

from event.models import Event, EventImage, Tag


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_name', 'desc', 'genre')

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = EventImage
        fields=('image', )

