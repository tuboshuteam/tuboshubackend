from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'post'
urlpatterns = [
    # 增
    path('create/', views.PostCreateAPIView.as_view(), name='create'),
    # 删改查
    path('edit/<int:pk>/', views.PostDetailAPIView.as_view(), name='detail'),
    # Post列表
    path('list/', views.PostListAPIView.as_view(), name='list'),
]