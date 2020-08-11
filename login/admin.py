from django.contrib import admin
from .models import Creator,Member
# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display=['pk','nickname']

@admin.register(Creator)
class CreatorAdmin(admin.ModelAdmin):
    list_display=['pk','member','creator_name']