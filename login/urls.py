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
    path('login/<int:pk>/delete/', views.user_delete, name='delete'), # 로그인 계정 삭제

    path('login/create_creator/', views.create_creator, name="create_creator"), # 크리에이터 등록
    path('login/<int:pk>/creator/', views.creator_mypage, name='creator_mypage'), # 크리에이터 마이페이지
    path('login/<int:pk>/creator/update/', views.creator_update, name='creator_update'), # 크리에이터 정보 수정
    path('login/<int:pk>/creator_delete/', views.creator_delete, name='creator_delete'),  # 크리에이터 계정 삭제
    path('login/<int:pk>/event/update/', views.event_update, name='event_update'), # 크리에이터 이벤트 수정
    # path('login/<int:pk>/creator/delete/', views.creator_delete, name='creator_delete'), -> 이렇게 하면 삭제하고 나서 새로고침했을 때 delete url을 계속 유지해서 오류 뜸


    path('login/signup_form/', views.signup_form, name="signup_form"), # 일반 회원가입 폼
    path('login/login_form/', views.login_form, name="login_form"), # 일반 로그인 폼

    path('login/check_id/', views.id_overlap_check, name='id_overlap_check'),  # id 중복 체크
    path('login/check_nickname/', views.nickname_lap_check, name='nickname_lap_check'),  # nickname 중복 체크
    path('login/check_email/', views.email_lap_check, name='email_lap_check'),  # email 중복 체크

    path('creator/like/', views.like, name="like_creator"), #크리에이터 좋아요/구독
]
