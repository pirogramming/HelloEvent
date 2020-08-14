from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    # path('<int:pk>/',views.comment_detail, name='comment_detail'),
    path('update/<int:comment_id>/', views.comment_update, name='comment_update'),
    path('delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]

