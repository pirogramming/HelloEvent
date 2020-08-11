from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'login'

urlpatterns = [
    path('', views.main),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/sign_up/', views.login_signup, name='signup'),
    path('login/<int:pk>/update/', views.login_update, name='update'),
    path('login/<int:pk>/', views.mypage, name='mypage'),
    path('login/create_creator/', views.create_creator, name="create_creator"),
    # path('accounts/social/signup/', views.signup, name='signup')
]


