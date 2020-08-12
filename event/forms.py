from django import forms

from event.models import Event, EventImage, Tag


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_name', 'genre', 'desc')
        widgets = {
            'event_name': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width:80%', 'style': 'margin:0 auto',
                       'placeholder': '이벤트 이름을 입력하세요'}
            ),
            'genre':forms.Select(
                attrs={'class':'form-control'}
            ),
            'desc': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': '이벤트에 대한 소개를 적어주세요'}
            )

        }
        labels = {
            'event_name': '이벤트명',
            'genre': '이벤트 종류',
            'desc': '이벤트 소개',

        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = EventImage
        fields=('image', )
        labels={
            'image':'이벤트 사진',
        }

