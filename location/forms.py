from django import forms
from .models import Event_Location

class LocationForm(forms.ModelForm):
    class Meta:
        model = Event_Location
        fields = ('city', 'gu', 'rest_address')