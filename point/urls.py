from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'point'
urlpatterns = [
    # 增
    path('create/', views.PointCreateAPIView.as_view(), name='create'),
    # 删改查
    path('edit/<int:pk>/', views.PointDetailAPIView.as_view(), name='detail'),
    # Post列表
    path('list/', views.PointListAPIView.as_view(), name='list'),
]