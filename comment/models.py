from django.db import models
from login import Member, Creator

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='comments')
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_text
    