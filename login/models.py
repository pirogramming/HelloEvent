from django.contrib.auth.models import User
from django.db import models

class Member(User):
    nickname = models.CharField(max_length=100, verbose_name='닉네임')
    #prefer_loc = models.OneToOneField(Prefer_Location, on_delete=models.CASCADE)

class Creator(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    creator_name = models.CharField(max_length=100, verbose_name='크리에이터명')
    creator_photo = models.ImageField(upload_to="creator_photo/%Y/%m/%d/") #4주년 축하해 잘 보냈니? upload_to가 확실하지 않다. \
    # 내가 하고 싶은건 업로드 날마다 날짜명이 기록된 다른 폴더에 들어가게 하는거야 찾아봐
    desc = models.TextField(blank=True)

    # like_users = models.ManyToManyField(Member, on_delete = models.CASCADE)


class Like(models.Model):
    from_user = models.ForeignKey(Member, on_delete=models.CASCADE)
    to_user = models.ForeignKey(Creator, on_delete=models.CASCADE)


