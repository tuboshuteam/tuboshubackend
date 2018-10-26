from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    HyperlinkedRelatedField,
    SerializerMethodField,
    DateTimeField,
)

from django.core.exceptions import ValidationError

from .models import Post

from userprofile.fields import TimestampField
from point.serializers import PointDetailSerializer
from point.models import Point


class PostCreateSerializer(ModelSerializer):
    """
    序列化新的Post表
    可以包含Point表

    必须的字段：title content

    json格式如下:
    {
    "title": str,
    "content": str,
    ...
    point: [
            {
                "longitude": num,
                "latitude": num,
                "travel_date_time": num,
                ...
            },
            {
                "longitude": num,
                "latitude": num,
                "travel_date_time": num,
                ...
            },
        ]
    }
    """

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
        ]

    def get_user(self, obj):
        return obj.user.id

    # 创建新的模型
    def create(self, validated_data):
        title = validated_data['title']
        content = validated_data['content']

        # 获取request.user
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        # 赋值并保存
        post_obj = Post(
            user=user,
            title=title,
            content=content
        )
        post_obj.save()

        # 为每一个point创建model
        if request and hasattr(request, "point"):
            for p_dict in request.data.get("point"):
                p_dict['post'] = post_obj
                Point.objects.create(**p_dict)
        return validated_data


class PostDetailSerializer(ModelSerializer):
    """
    Post的查看、更新、删除

    json格式如下:
    {
    "title": str,
    "content": str,
    ...
    point: [
            # 创建新Point
            {
                "method": "create",
                "longitude": num,
                "latitude": num,
                "travel_date_time": num,
                ...
            },
            # 删除id为"id"的Point
            {
                "method": "delete",
                "id": num,
            },
            # 更新id为"id"的Point
            {
                "method": "update",
                "id": num,
                "longitude": num,
                "latitude": num,
                "travel_date_time": num,
                ...
            },
        ]
    }
    """
    user = HyperlinkedRelatedField(
        view_name="userprofile:detail",
        read_only=True
    )
    created = TimestampField(read_only=True)
    updated = TimestampField(read_only=True)
    user_name = SerializerMethodField()
    point = PointDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'user_name',
            'title',
            'views',
            'created',
            'updated',
            'content',
            'point',
        ]
        read_only_fields = [
            'id',
            'user',
            'user_name',
            'views',
            'created',
            'updated',
        ]

    def get_user_name(self, obj):
        return obj.user.username

    # 重写update方法
    # 可以从这里更新相关的Point表了
    def update(self, instance, validated_data):
        request = self.context.get("request")
        if request.data.get("point"):
            # print(request.data.get("point"))
            # 遍历point数组，对Point表进行更新、创建、删除
            for p_dict in request.data.get("point"):
                method = p_dict['method']
                del p_dict['method']

                # 如果method元素为create，则创建一个新的Point
                if method == "create":
                    p_dict['post'] = instance
                    Point.objects.create(**p_dict)

                # method为update，则更新现有的Point
                elif method == 'update':
                    point_obj = Point.objects.get(id=p_dict['id'])
                    del p_dict['id']
                    for key, value in p_dict.items():
                        setattr(point_obj, key, value)
                    point_obj.save()

                # method为delete，则删除Point
                elif method == 'delete':
                    point_obj = Point.objects.get(id=p_dict['id'])
                    point_obj.delete()

                else:
                    raise ValidationError("method必须为create/update/delete")
        # 更新Post内容
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance


class PostListSerializer(ModelSerializer):
    """
    Post列表
    """
    url = HyperlinkedIdentityField(view_name="post:detail")
    user = HyperlinkedRelatedField(
        view_name="userprofile:detail",
        read_only=True
    )

    created = TimestampField(read_only=True)
    updated = TimestampField(read_only=True)
    user_name = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'user',
            'user_name',
            'title',
            'views',
            'created',
            'updated',
        ]

    def get_user_name(self, obj):
        return obj.user.username


class PostSimpleDetailSerializer(ModelSerializer):
    """
    提供给UserDetailSerializer连接的简易Detail
    """
    url = HyperlinkedIdentityField(view_name="post:detail")

    class Meta:
        model = Post
        fields = [
            'url',
            'title',
        ]
