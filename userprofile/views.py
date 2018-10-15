from django.db.models import Q

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
)

from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)

from rest_framework.mixins import (
    UpdateModelMixin,
)

from django.contrib.auth.models import User

from .serializers import (
    UserCreateSerializer,
    UserListSerializer,
    UserCreateUpdateSerializer,
)


# 增
class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


# 删改查
class UserUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer

    # 允许PUT方法的部分字段修改
    def put(self, request, *args, **kwargs):
        print("partile_update")
        return self.partial_update(request, *args, **kwargs)


# 列表
class UserListAPIView(ListAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = User.objects.all()
        return queryset_list
