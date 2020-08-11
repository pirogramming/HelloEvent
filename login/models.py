from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django import forms

User
def min_length_2_validator(value):
    if len(value) < 2:
        raise forms.ValidationError('2글자 이상 입력해주세요')



class Member(AbstractUser):
    nickname = models.CharField(max_length=100, verbose_name='닉네임', validators=[min_length_2_validator])
    created_on = models.DateTimeField("등록일자", auto_now_add=True)
    updated_on = models.DateTimeField("수정일자", auto_now=True)

    class Meta(AbstractUser.Meta):
        db_table = 'member'
        verbose_name = 'member'

class Creator(models.Model):
    creator_name = models.CharField(max_length=100, verbose_name='크리에이터명')
    creator_photo = models.ImageField(upload_to="creator_photo/%Y/%m/%d/")
    desc = models.TextField(blank=True)
    member = models.OneToOneField(Member, on_delete=models.CASCADE)

class Like(models.Model):
    from_user = models.ForeignKey(Member, on_delete=models.CASCADE)
    to_user = models.ForeignKey(Creator, on_delete=models.CASCADE)

