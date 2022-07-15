from django.contrib import admin
from django.urls import path
from user import views
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.UserView.as_view()),
    path('login/', views.TokenObtainPairView.as_view(), name='patrasche_token'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('authonly/', views.OnlyAuthenticatedUserView.as_view()),
    path('authonly/<int:pk>/', views.OnlyAuthenticatedUserView.as_view()),
    path('follow/', views.UserFollowingView.as_view()),
    path('mypet/', views.PetView.as_view()),
    path('mypet/<int:pk>/', views.PetView.as_view()),

]
