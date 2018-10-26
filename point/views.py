from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView,
    GenericAPIView,
)

from .serializers import (
    PointListSerializer,
    PointCreateSerializer,
    PointDetailSerializer,
)
from .models import Point


# Create your views here.

class PointCreateAPIView(CreateAPIView):
    """
    创建Point表
    """
    serializer_class = PointCreateSerializer
    queryset = Point.objects.all()


class PointDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Post的查看、更新、删除
    """
    serializer_class = PointDetailSerializer
    queryset = Point.objects.all()

    # 允许PUT方法的部分字段修改
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class PointListAPIView(ListAPIView):
    """
    Point列表
    """
    serializer_class = PointListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Point.objects.all()
        return queryset_list
