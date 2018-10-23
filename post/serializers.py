from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    HyperlinkedRelatedField,
    SerializerMethodField,
    DateTimeField,
)

from django.contrib.auth.models import User

from .models import Post

from userprofile.fields import TimestampField


class PostCreateSerializer(ModelSerializer):
    """
    序列化新的Post表
    必须的字段：title content
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
        return validated_data


class PostDetailSerializer(ModelSerializer):
    """
    Post的查看、更新、删除
    """
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
            'id',
            'user',
            'user_name',
            'title',
            'views',
            'created',
            'updated',
            'content',
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
