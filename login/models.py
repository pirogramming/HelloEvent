from django.contrib.auth.models import User
from django.db import models
from django import forms


def min_length_2_validator(value):
    if len(value) < 2:
        raise forms.ValidationError('2글자 이상 입력해주세요')


class Member(User):
    nickname = models.CharField(max_length=100, verbose_name='닉네임', validators=[min_length_2_validator], unique=True)
    CITY_CHOICES = (
        ('Seoul', '서울특별시'),
    )
    GU_CHOICES = (
        ('Gangnam', '강남구'),
        ('Songpa', '송파구'),
        ('Seocho', '서초구'),
        ('Gangdong', '강동구'),
        ('Gwanak', '관악구'),
        ('Yeongdeung', '영등포구'),
        ('Gangseo', '강서구'),
        ('Yangcheon', '양천구'),
        ('Guro', '구로구'),
        ('Geumcheon', '금천구'),
        ('Jongno', '종로구'),
        ('Jung', '중구'),
        ('Dongdaemun', '동대문구'),
        ('Jungrang', '중랑구'),
        ('Mapo', '마포구'),
        ('Yongsan', '용산구'),
        ('Seongdong', '성동구'),
        ('Gwangjin', '광진구'),
        ('Eunpyeong', '은평구'),
        ('Seodaemun', '서대문구'),
        ('Seongbuk', '성북구'),
        ('Gangbuk', '강북구'),
        ('Dobong', '도봉구'),
        ('Nowon', '노원구'),
    )
    city = models.CharField(max_length=30, choices=CITY_CHOICES, verbose_name='선호도시')
    gu = models.CharField(max_length=30, choices=GU_CHOICES, verbose_name='선호구')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Creator(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)  # 주최명
    desc = models.TextField(blank=True)  # 팀 설명
    creator_name = models.CharField(max_length=100, verbose_name='크리에이터명')  # 대표 이름
    creator_photo = models.ImageField(blank=True, upload_to="creator_photo/%Y/%m/%d/")  # 대표 사진


class Like(models.Model):
    from_user = models.ForeignKey(Member, on_delete=models.CASCADE)
    to_user = models.ForeignKey(Creator, on_delete=models.CASCADE)


