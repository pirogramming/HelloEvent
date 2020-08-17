from django.db import models
from login.models import Member, Creator


class Comment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField(blank=True)
    comment_photo = models.ImageField(null=True, upload_to='comment/%Y/%m/%d', verbose_name="댓글 첨부 사진")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_text + ' '+ self.created_at.strftime("%Y-%m-%d %H:%M:%S")

class Recomment(models.Model):
    parent = models.ForeignKey(Comment, on_delete=models.CASCADE)
    writer = models.ForeignKey(Member, on_delete=models.CASCADE)
    recomment_text = models.CharField(max_length=100,blank=True)
    comment_photo = models.ImageField(null=True, upload_to='recomment/%Y/%m/%d', verbose_name="댓글 첨부 사진")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.recomment_text + ' '+ self.created_at.strftime("%Y-%m-%d %H:%M:%S")
