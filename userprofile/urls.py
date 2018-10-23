from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'userprofile'
urlpatterns = [
    # 增User
    path('create/', views.UserCreateAPIView.as_view(), name='create'),
    # 删改查User
    path('edit/<int:pk>/', views.UserUpdateAPIView.as_view(), name='detail'),
    # User列表
    path('list/', views.UserListAPIView.as_view(), name='list'),
]