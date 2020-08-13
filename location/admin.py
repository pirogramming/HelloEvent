from django.contrib import admin
from .models import Event_Location

@admin.register(Event_Location)
class LocationAdmin(admin.ModelAdmin):
    list_display=['pk','city','gu','rest_address']