from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView,
    GenericAPIView,
)

from .models import Comment
from .serializers import (
    CommentListSerializer,
    CommentCreateSerializer,
    CommentDetailSerializer
)


# Create your views here.

class CommentCreateAPIView(CreateAPIView):
    serializer_class = CommentCreateSerializer


class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
