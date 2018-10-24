from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    HyperlinkedRelatedField,
    SerializerMethodField,
    DateTimeField,
)

from .models import Point


class PointCreateSerializer(ModelSerializer):
    """
    序列化新的Point表
    """

    class Meta:
        model = Point
        fields = [
            'post',
            'longitude',
            'latitude',
            'travel_date_time',
            'name',
            'expend',
            'content',
        ]

    # 创建新的模型
    def create(self, validated_data):
        point = Point.objects.create(**validated_data)
        return point


class PointDetailSerializer(ModelSerializer):
    """
    查看、更新、删除Point
    """
    class Meta:
        model = Point
        fields = [
            'id',
            'post',
            'longitude',
            'latitude',
            'travel_date_time',
            'name',
            'expend',
            'content',
        ]
        read_only_fields = [
            'post',
        ]


class PointListSerializer(ModelSerializer):
    """
    Point列表
    """

    url = HyperlinkedIdentityField(view_name="point:detail")

    class Meta:
        model = Point
        fields = [
            'url',
            'post',
            'longitude',
            'latitude',
            'travel_date_time',
            'name',
            'expend',
            'content',
        ]
