from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'login'

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='login'), # 로그인 전체화면
    path('signup/', views.signup_general, name='signup_general'), # 회원가입 전체화면
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('login/<int:pk>/sign_up/', views.signup, name='signup'), # 소셜 로그인 추가 정보 입력
    path('login/<int:pk>/update/', views.login_update, name='update'), # 사용자 정보 수정
    path('login/<int:pk>/', views.mypage, name='mypage'), # 사용자 마이페이지

    path('login/create_creator/', views.create_creator, name="create_creator"), # 크리에이터 등록
    # path('accounts/social/signup/', views.signup, name='signup')
    path('login/<int:pk>/creator/', views.creator_mypage, name='creator_mypage'), # 크리에이터 마이페이지
    path('login/<int:pk>/creator/update/', views.creator_update, name='creator_update'), # 크리에이터 정보 수정

    path('login/signup_form/', views.signup_form, name="signup_form"), # 일반 회원가입 폼
    path('login/login_form/', views.login_form, name="login_form"), # 일반 로그인 폼

    path('login/check/', views.id_overlap_check, name='id_overlap_check')  # id 중복 체크
]
