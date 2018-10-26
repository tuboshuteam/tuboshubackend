from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    HyperlinkedRelatedField,
    SerializerMethodField,
    DateTimeField,
)

from .models import Comment
from utils.fields import TimestampField


class CommentCreateSerializer(ModelSerializer):
    """
    新建Comment

    json [POST]:
    {
        "post": [post_id],
        "content": str
    }
    """

    class Meta:
        model = Comment
        fields = [
            'post',
            'user',
            'content',
        ]
        read_only_fields = [
            'user',
        ]

    def create(self, validated_data):
        # 获取request.user
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        Comment.objects.create(**validated_data, user=user)
        return validated_data


class CommentDetailSerializer(ModelSerializer):
    """
    删除、更新、查看Comment

    json [PUT]:
    {
        "content": str
    }
    """

    created = TimestampField(read_only=True)
    post = HyperlinkedRelatedField(
        view_name='post:detail',
        read_only=True,
    )
    user = HyperlinkedRelatedField(
        view_name='userprofile:detail',
        read_only=True,
    )
    post_title = SerializerMethodField()
    user_name = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'user',
            'post_title',
            'user_name',
            'content',
            'created',

        ]
        read_only_fields = [
            'user',
            'post',
        ]

    def get_post_title(self, instance):
        return instance.post.title

    def get_user_name(self, instance):
        return instance.user.username


class CommentListSerializer(ModelSerializer):
    """
    评论列表
    """
    url = HyperlinkedIdentityField(
        view_name='comment:detail',
    )
    post = HyperlinkedRelatedField(
        view_name='post:detail',
        read_only=True,
    )
    user = HyperlinkedRelatedField(
        view_name='userprofile:detail',
        read_only=True,
    )
    post_title = SerializerMethodField()
    user_name = SerializerMethodField()

    created = TimestampField()

    class Meta:
        model = Comment
        fields = [
            'url',
            'post',
            'user',
            'post_title',
            'user_name',
            'content',
            'created',
        ]

    def get_post_title(self, instance):
        return instance.post.title

    def get_user_name(self, instance):
        return instance.user.username


class CommentPostSerializer(ModelSerializer):
    """
    在Post中展示的Comments
    """
    url = HyperlinkedIdentityField(view_name='comment:detail')
    created = TimestampField(read_only=True)
    user_name = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'url',
            'user_name',
            'content',
            'created',

        ]
    def get_user_name(self, instance):
        return instance.user.username