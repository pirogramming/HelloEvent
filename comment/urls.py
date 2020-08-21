from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    # path('<int:pk>/',views.comment_detail, name='comment_detail'),
    path('update/<int:comment_id>/', views.comment_update, name='comment_update'),
    path('delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('<int:comment_id>/recomment/', views.recomment_detail, name='recomment_detail'),
    path('<int:comment_id>/recomment/create/', views.recomment_create_ajax, name='recomment_create_ajax'),
    path('<int:comment_id/recomment/delete/<int:recomment_id>/', views.recomment_delete, name='recomment_delete'),
    # path('create/', views.comment_create_ajax, name='comment_create_ajax'),
    # path('creator_event/<int:pk>/',views.creator_detail, name='creator_detail'),
    # path('creator_event/<int:pk>/detail', comment_detail, name='comment_detail'),
]

