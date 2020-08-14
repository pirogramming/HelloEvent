from django.db import models
from login.models import Creator
from location.models import Event_Location

# Create your models here.


class Event(models.Model):
    location = models.ForeignKey(Event_Location, on_delete=models.CASCADE,default=None)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE,default=None, related_name='events')
    event_name = models.CharField(max_length=200, blank=False)
    desc = models.TextField(blank=True)

    start_date_time = models.DateTimeField(auto_now=False, blank=False)
    end_date_time = models.DateTimeField(auto_now=False, blank=False)


    GENRE_LIST = (
        ('Busking', '버스킹'),
        ('Flee', '플리마켓'),
        ('Exihibit', '전시'),
    )
    genre = models.CharField(max_length=100, choices=GENRE_LIST)


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None, related_name='images')
    image = models.ImageField(upload_to='event_images/%Y/%m/%d', verbose_name="이벤트 이미지")


class Tag(models.Model):
    name = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)






