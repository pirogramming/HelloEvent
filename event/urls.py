from django.urls import path
from event import views

app_name = 'event'

urlpatterns = [
    path('register/', views.register_event, name="event_register"),
    path('creator_event/<int:pk>/',views.creator_detail, name='creator_detail'),
]