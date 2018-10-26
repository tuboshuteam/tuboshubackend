from django.urls import path, include
from . import views

app_name = 'comment'

urlpatterns = [
    # 增
    path('create/', views.CommentCreateAPIView.as_view(), name='create'),
    # 删改查
    path('edit/<int:pk>/', views.CommentDetailAPIView.as_view(), name='detail'),
    # Post列表
    path('list/', views.CommentListAPIView.as_view(), name='list'),
]