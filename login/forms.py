from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member  # ModelForm을 이용하면, Model 내역에 맞게 손쉽게 정의 가능
        fields = '__all__' # 모든 필드가 자동 지정이 됨.


# class CreatorForm(forms.ModelForm):
#     class Meta:
#         model = Creator
#         fields = '__all__'