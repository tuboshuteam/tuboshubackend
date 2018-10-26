from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    HyperlinkedRelatedField,
    SerializerMethodField,
    DateTimeField,
)

from .models import Comment

class CommentListSerializer(ModelSerializer):

    post = HyperlinkedRelatedField(
        view_name='post:detail',
        read_only=True,
    )
    user = HyperlinkedRelatedField(
        view_name='userprofile:detail',
        read_only=True,
    )
    post_name = SerializerMethodField()
    user_name = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'post',
            'post_name',
            'user',
            'user_name',
            'content',
            'created',
        ]

    def get_post_name(self, instance):
        return  instance.post.id

    def get_user_name(self, instance):
        return instance.user.username