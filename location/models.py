from django.db import models

# 사용자의 선호 지역 모델
class Prefer_Location(models.Model):
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

    def __str__(self):
        return self.city

# 이벤트가 일어나는 장소 모델
class Event_Location(models.Model):
    city = models.CharField(max_length=30, verbose_name='이벤트도시')
    gu = models.CharField(max_length=30, verbose_name='이벤트구')
    rest_address = models.CharField(max_length=100, verbose_name='나머지주소')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city
