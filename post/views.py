from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView,
    GenericAPIView,
)

from .serializers import (
    PostListSerializer,
    PostDetailSerializer,
)

from .models import Post


# Create your views here.

class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()


class PostListAPIView(ListAPIView):
    """
    Post表的查看
    """
    serializer_class = PostListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        return queryset_list
