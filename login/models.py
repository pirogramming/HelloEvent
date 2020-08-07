from django.contrib.auth.models import User
from django.db import models

class Member(User):
    nickname = models.CharField(max_length=100, verbose_name='닉네임')
    #prefer_loc = models.OneToOneField(Prefer_Location, on_delete=models.CASCADE)

class Creator(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    creator_name = models.CharField(max_length=100, verbose_name='크리에이터명')
    creator_photo = models.ImageField(upload_to="creator_photo/%Y/%m/%d/")
    desc = models.TextField(blank=True)


class Like(models.Model):
    from_user = models.ForeignKey(Member, on_delete=models.CASCADE)
    to_user = models.ForeignKey(Creator, on_delete=models.CASCADE)

