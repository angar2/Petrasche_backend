from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('', views.UserView.as_view()),
    path('login/', views.TokenObtainPairView.as_view(), name='patrasche_token'),
    path('follow/', views.UserFollowingView.as_view()),
    # path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('my_page/', views.OnlyAuthenticatedUserView.as_view()),
]
