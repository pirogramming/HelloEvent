from django.contrib.auth.models import User
from django.db import models


class Member(User):
    nickname = models.CharField(max_length=100, verbose_name='닉네임')
    AREA_CHOICES=(
        ('Seoul', '서울'),
        ('Incheon', '인천'),
        ('Gyeonggi', '경기'),
        ('Gangwon', '강원'),
        ('Daejeon', '대전'),
        ('Daegu', '대구'),
        ('Ulsan', '울산'),
        ('Busan', '부산'),
        ('Gwangju', '광주'),
        ('Chungcheong', '충청'),
        ('Jeolla', '전라'),
        ('Gyeongsang', '경상'),
        ('Jeju', '제주'),
    )
    SEOUL_CITY_CHOICES = (
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
    THEME_CHOICES = (
        ('BUSKING', '버스킹'),
        ('FLEE', '플리마켓'),
        ('EXHIBITION', '전시회'),
    )
    area = models.CharField(max_length=100, choices=AREA_CHOICES, verbose_name='지역')  # 지역 고르기
    seoul_city = models.CharField(max_length=100, choices=SEOUL_CITY_CHOICES, verbose_name='구')  # 서울 내 25개 구 中 선택
    theme = models.CharField(max_length=100, choices=THEME_CHOICES, verbose_name='테마')


# prefer_loc = models.OneToOneField(Prefer_Location, on_delete=models.CASCADE)


class Creator(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    creator_name = models.CharField(max_length=100, verbose_name='크리에이터명')
    creator_photo = models.ImageField(upload_to="creator_photo/%Y/%m/%d/") # 4주년 축하해 잘 보냈니? upload_to가 확실하지 않다. \
    # 내가 하고 싶은건 업로드 날마다 날짜명이 기록된 다른 폴더에 들어가게 하는거야 찾아봐
    desc = models.TextField(blank=True)
    AREA_CHOICES = (
        ('Seoul', '서울'),
        ('Incheon', '인천'),
        ('Gyeonggi', '경기'),
        ('Gangwon', '강원'),
        ('Daejeon', '대전'),
        ('Daegu', '대구'),
        ('Ulsan', '울산'),
        ('Busan', '부산'),
        ('Gwangju', '광주'),
        ('Chungcheong', '충청'),
        ('Jeolla', '전라'),
        ('Gyeongsang', '경상'),
        ('Jeju', '제주'),
    )
    SEOUL_CITY_CHOICES = (
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
    THEME_CHOICES = (
        ('BUSKING', '버스킹'),
        ('FLEE', '플리마켓'),
        ('EXHIBITION', '전시회'),
    )
    cr_area = models.CharField(max_length=100, choices=AREA_CHOICES, verbose_name='지역')
    cr_seoul_city = models.CharField(max_length=100, choices=SEOUL_CITY_CHOICES)
    cr_theme = models.CharField(max_length=100, choices=THEME_CHOICES, verbose_name='테마')
    # created_date = models.DateTimeField(auto_now_add=True)
    # updated_date = models.DateTimeField(add_now=True)


    # like_users = models.ManyToManyField(Member, on_delete=models.CASCADE)


class Like(models.Model):
    from_user = models.ForeignKey(Member, on_delete=models.CASCADE)  # 이용자가 좋아요 누를 때
    to_user = models.ForeignKey(Creator, on_delete=models.CASCADE)  # host가 좋아요 받을 때




