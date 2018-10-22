from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'post'
urlpatterns = [
    # 增User
    # path('create/', views.UserCreateAPIView.as_view(), name='create'),
    # 删改查User
    path('edit/<int:pk>/', views.PostDetailAPIView.as_view(), name='detail'),
    # User列表
    path('list/', views.PostListAPIView.as_view(), name='list'),
    # 删改Profile
    # path('edit-profile/<int:user>/', views.ProfileUpdateAPIView.as_view(), name='p_detail'),
]