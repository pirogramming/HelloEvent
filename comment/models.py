from django.db import models
from login.models import Member, Creator


class Comment(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_text + ' '+ self.created_at.strftime("%Y-%m-%d %H:%M:%S")