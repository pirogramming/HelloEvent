from django.urls import path
from event import views

app_name = 'event'

urlpatterns = [
    path('register/', views.event, name="event_register")
]