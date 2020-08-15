from django.db import models
from login.models import Creator
from location.models import Event_Location

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)

class Event(models.Model):
    location = models.ForeignKey(Event_Location, on_delete=models.CASCADE,default=None)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE,default=None, related_name='events')
    event_name = models.CharField(max_length=200, blank=False, verbose_name="이벤트 이름")
    desc = models.TextField(blank=True, verbose_name="이벤트 소개")

    start_date_time = models.DateTimeField(auto_now=False, blank=False, verbose_name="이벤트 시작 날짜/시간")
    end_date_time = models.DateTimeField(auto_now=False, blank=False, verbose_name="이벤트 종료 날짜/시간")

    tags = models.ManyToManyField(Tag, verbose_name="태그")

    GENRE_LIST = (
        ('Busking', '버스킹'),
        ('Flee', '플리마켓'),
        ('Exihibit', '전시'),
    )
    genre = models.CharField(max_length=100, choices=GENRE_LIST, verbose_name="이벤트 장르")

    def __str__(self):
        return self.event_name


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='event_images/%Y/%m/%d', verbose_name="이벤트 이미지")






