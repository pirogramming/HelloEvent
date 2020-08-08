from django.contrib.auth.models import User
from django.db import models
from django import forms


def min_length_2_validator(value):
    if len(value) < 2:
        raise forms.ValidationError('2글자 이상 입력해주세요')


class Member(User):
    nickname = models.CharField(max_length=100, verbose_name='닉네임', validators=[min_length_2_validator])

class Creator(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    creator_name = models.CharField(max_length=100, verbose_name='크리에이터명')
    creator_photo = models.ImageField(upload_to="creator_photo/%Y/%m/%d/")
    desc = models.TextField(blank=True)

class Like(models.Model):
    from_user = models.ForeignKey(Member, on_delete=models.CASCADE)
    to_user = models.ForeignKey(Creator, on_delete=models.CASCADE)

