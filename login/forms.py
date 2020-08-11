from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member  # ModelForm을 이용하면, Model 내역에 맞게 손쉽게 정의 가능
        fields = ['nickname', 'city', 'gu']  # 모든 필드가 자동 지정이 됨.

# https://github.com/pennersr/django-allauth/issues/2039
# Allauth SignupForm 가져옴.

# from allauth.account.forms import SignupForm
# from django.utils.translation import ugettext_lazy as _
# from django import forms
# from .models import Profile


# class SignupForm(SignupForm):
#     class Meta:
#         model = Member
#         fields = ['nickname', 'city', 'gu']
#
#     def signup(self, request, user):
#         user.nickname = self.cleaned_data['nickname']
#         user.city = self.cleaned_data['city']
#         user.gu = self.cleaned_data['gu']
#         user.save()
#         return user
# class SignupForm(forms.Form):
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#
#         class Meta:
#             model = Profile
#             fields = ('nickname', 'city', 'gu')
#
#         def signup(self, request, user):
#             # Save your user
#             user.first_name = self.cleaned_data['first_name']
#             user.last_name = self.cleaned_data['last_name']
#             user.saver()
#
#             user.profile.nickname = self.cleaned_data['nickname']
#             user.profile.city = self.cleaned_data['city']
#             user.profile.gu = self.cleaned_data['gu']
#             user.profile.save()



    #
    # def signup(self, request, user):
    #     user.nickname = self.cleaned_data['nickname']
    #     user.city = self.cleaned_data['city']
    #     user.gu = self.cleaned_data['gu']
    #     user.save()
    #
    #     profile = Member()
    #     profile.user = user
    #     profile.nickname = self.cleaned_data['nickname']
    #     profile.city = self.cleaned_data['city']
    #     profile.gu = self.cleaned_data['gu']
    #     profile.save()




# class CreatorForm(forms.ModelForm):
#     class Meta:
#         model = Creator
#         fields = '__all__'


