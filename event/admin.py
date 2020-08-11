from django.contrib import admin

# Register your models here.
from event.models import Event, EventImage, Test

admin.site.register(Event)

admin.site.register(EventImage)

admin.site.register(Test)