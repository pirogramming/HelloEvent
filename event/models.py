# from django.db import models
#
# # Create your models here.
#
# class Event(models.Model):
#     location = models.ForeignKey(Event_Location, on_delete=models.CASCADE)
#     creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
#     event_name = models.CharField(max_length=200, blank=True)
#     desc = models.TextField(blank=True)
#
#
# class EventImage(models.Model):
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to="event/%Y/%m/%d")

