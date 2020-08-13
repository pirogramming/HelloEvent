from django.contrib import admin

# Register your models here.
from event.models import Event, EventImage, Tag

admin.site.register(Event)

admin.site.register(EventImage)

admin.site.register(Tag)