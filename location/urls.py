from django.urls import path
from . import views

app_name = 'location'

urlpatterns = [
    path('',views.show_map,name='show_map'),
    path('search/',views.search_map,name='search_map'),
    path('search/genre/',views.ajax_search_genre,name='ajax_search_genre'),
]