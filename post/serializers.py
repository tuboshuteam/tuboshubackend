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


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'content',
        ]


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
            'content',
        ]

    def get_user_name(self, obj):
        return obj.user.username
