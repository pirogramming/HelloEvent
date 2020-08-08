from django.contrib.auth.models import User
from django.db import models
from django import forms


def min_length_2_validator(value):
    if len(value) < 2:
        raise forms.ValidationError('2글자 이상 입력해주세요')


class Member(User):
    nickname = models.CharField(max_length=100, verbose_name='닉네임', validators=[min_length_2_validator])






