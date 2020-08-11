from django import forms

from event.models import Event, EventImage, Test


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_name', 'desc', 'genre')

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='')
    class Meta:
        model = EventImage
        fields = ('image', )

class TestForm(forms.ModelForm):

    class Meta:
        model = Test
        fields = ('name',)