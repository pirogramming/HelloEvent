# from django.db import models
# from login import User, Creator
#
# # Create your models here.
# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
#     creator = models.ForeignKey(Creator, on_delete=models.CASCADE, related_name='comments')
#     comment_text = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
#     updated_at = models.DateTimeField(auto_now=True)
#     approved_comment = models.BooleanField(default=True)
#
#     def approve(self):
#         self.approved_comment = True
#         self.save()
#
#     def __str__(self):
#         return self.comment_text
#
    