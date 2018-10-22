from django.db.models import Q

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView,
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
    UserDetailSerializer,
    ProfileDetailSerializer,
)

from .models import Profile


class ProfileUpdateAPIView(RetrieveUpdateAPIView):
    """
    查看、更新Profile表
    """
    queryset = Profile
    serializer_class = ProfileDetailSerializer
    lookup_field = 'user'


class UserCreateAPIView(CreateAPIView):
    """
    新建User表
    对应的Profile会自动创建并关联
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateAPIView(RetrieveUpdateDestroyAPIView):
    """
    User表的删除、更新、查看
    对应http请求的delete/put/get方法
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    # 允许PUT方法的部分字段修改
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class UserListAPIView(ListAPIView):
    """
    User表的查看
    """
    serializer_class = UserListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = User.objects.all()
        return queryset_list
