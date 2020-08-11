from django.db import models


# 이벤트가 일어나는 장소 모델
class Event_Location(models.Model):
    city = models.CharField(max_length=30, verbose_name='이벤트도시')
    gu = models.CharField(max_length=30, verbose_name='이벤트구')
    rest_address = models.CharField(max_length=100, verbose_name='나머지주소')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city
