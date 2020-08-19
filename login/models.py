from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser, UserManager
from django.db import models
from django import forms


def min_length_2_validator(value):
    if len(value) < 2:
        raise forms.ValidationError('2글자 이상 입력해주세요')


class Member(AbstractUser):
    nickname = models.CharField(max_length=100, verbose_name='닉네임', validators=[min_length_2_validator], unique=True)
    created_on = models.DateTimeField("등록일자", auto_now_add=True)
    updated_on = models.DateTimeField("수정일자", auto_now=True)
    CITY_CHOICES = (
        ('서울특별시', '서울특별시'),
    )
    GU_CHOICES = (
        ('강남구', '강남구'),
        ('송파구', '송파구'),
        ('서초구', '서초구'),
        ('강동구', '강동구'),
        ('관악구', '관악구'),
        ('영등포구', '영등포구'),
        ('강서구', '강서구'),
        ('양천구', '양천구'),
        ('구로구', '구로구'),
        ('금천구', '금천구'),
        ('종로구', '종로구'),
        ('중구', '중구'),
        ('동대문구', '동대문구'),
        ('중랑구', '중랑구'),
        ('마포구', '마포구'),
        ('용산구', '용산구'),
        ('성동구', '성동구'),
        ('광진구', '광진구'),
        ('은평구', '은평구'),
        ('서대문구', '서대문구'),
        ('성북구', '성북구'),
        ('강북구', '강북구'),
        ('도봉구', '도봉구'),
        ('노원구', '노원구'),
    )
    city = models.CharField(max_length=30, choices=CITY_CHOICES, verbose_name='선호도시')
    gu = models.CharField(max_length=30, choices=GU_CHOICES, verbose_name='선호구')


    class Meta:
        db_table = 'member'
        verbose_name = 'member'


class Creator(models.Model):
    creator_name = models.CharField(max_length=100, verbose_name='크리에이터명')
    creator_photo = models.ImageField(upload_to="creator_photo/%Y/%m/%d/")
    desc = models.TextField(blank=True)

    member = models.OneToOneField(Member, on_delete=models.CASCADE, default=None, null=True, blank=True, related_name="creator")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_creators")

    @property
    def like_count(self):
        return self.like_users.count()