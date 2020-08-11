from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    path('<int:creator_id>', views.comment_read, name='comment_read'),
    # path('<int:pk>/',views.comment_create, name='comment_create'),
]

