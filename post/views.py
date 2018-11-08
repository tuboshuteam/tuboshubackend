from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView,
    GenericAPIView,
)

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from .serializers import (
    PostListSerializer,
    PostDetailSerializer,
    PostCreateSerializer,
)

from django.shortcuts import get_object_or_404
from .models import Post


# Create your views here.
class PostCreateAPIView(CreateAPIView):
    """
    新建User表
    对应的Profile会自动创建并关联
    """
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Post的查看、更新、删除
    """
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()

    # 允许PUT方法的部分字段修改
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    # 重写GET方法，阅读量+1
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        post.increase_views()
        return super(PostDetailAPIView, self).get(request, *args, **kwargs)


class PostListAPIView(ListAPIView):
    """
    Post列表
    """
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['location', 'title',]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        return queryset_list
