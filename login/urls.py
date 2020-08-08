from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.main),
    path('login/sign_up/', views.login_signup, name='signup')
]

# , name='main'

