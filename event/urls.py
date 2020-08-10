from django.urls import path
from event import views

app_name = 'event'

urlpatterns = [
    path('register/<id:pk>/', views.register_event, name="event_register")
]