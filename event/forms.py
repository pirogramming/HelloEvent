from django import forms

from event.models import Event, EventImage, Tag
from event.widgets import DatePickerWidget


class DateTimeInput(forms.DateTimeInput):
    input_type = 'DateTime'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_name', 'genre', 'desc',)
        exclude = ('start_date_time', 'end_date_time',)
        widgets = {
            'event_name': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width:100%; margin:0 auto',
                       'placeholder': '이벤트 이름을 입력하세요'}
            ),
            'genre':forms.Select(
                attrs={'class':'form-control', 'style': 'width:30%;',}
            ),
            'desc': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': '이벤트에 대한 소개를 적어주세요'}
            ),
            # 'start_date': forms.SelectDateWidget(
            #     attrs={'class':'form-control', 'style':'width:10%; display:inline-block;'}
            # ),
            # 'end_date': forms.SelectDateWidget(
            #     attrs={'class':'form-control', 'style':'width:10%; display:inline-block;'}
            # ),
            # 'start_time':forms.TimeInput(),
            # 'end_time':forms.TimeInput(),

        }
        labels = {
            'event_name': '이벤트명',
            'genre': '이벤트 종류',
            'desc': '이벤트 소개',
            'start_date' : '이벤트 시작 날짜',
            'end_date': '이벤트 종료 날짜',
            'start_time' : '시작 시간',
            'end_time' : '종료 시간',
        }
        required = {
            'event_name':True,
            'genre':True,
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = EventImage
        fields=('image', )
        labels={
            'image':'이벤트 사진',
        }

