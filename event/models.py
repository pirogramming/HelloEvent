from django.db import models
from login.models import Creator
from location.models import Event_Location

# Create your models here.

class Event(models.Model):
    location = models.ForeignKey(Event_Location, on_delete=models.CASCADE)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=200, blank=False)
    desc = models.TextField(blank=True)
    genre = models.CharField(max_length=100)

    genre = ["Busking", "Flimarket", ""]

def get_image_filename(instance, filename):
    id = instance.post.id
    return f'event_images/{id}'

class Event_Image(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to= get_image_filename, verbose_name="이벤트 이미지")

class Tag(models.Model):
    name = models.CharField(max_length=100)


