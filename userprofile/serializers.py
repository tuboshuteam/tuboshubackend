from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Profile


# Profile扩展表，挂在User上展示
class UserProfileListSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'phone',
            'gender',
            'birthday',
            'address',
            'avatar',
            'bio',
            'tags',
            'level',
        ]

# 增加User
class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
        extra_kwargs = {"password":
            {"write_only": True}
        }

    # 验证password大于6位
    def validate_password(self, value):
        data = self.get_initial()
        password = data.get('password')
        if len(password) < 6:
            raise ValidationError("密码至少6位。")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user_obj = User(
            username = username,
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


# 改User表
class UserCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'last_login',
            'date_joined',
        ]
        read_only_fields = [
            'username',
            'last_login',
            'date_joined',
        ]

    # email数据验证，不允许与已有的email相同
    def validate_email(self, value):
        data = self.get_initial()
        email = data.get('email')
        user_qs = User.objects.exclude(email__isnull=True).exclude(email__exact='').filter(email=email)
        if user_qs.exists():
            raise ValidationError("本邮箱已被注册。")
        return value

    # 更新数据
    def update(self, instance, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        if email:
            instance.email = email
        if password:
            instance.set_password(password)
        instance.save()
        return validated_data


# 用户列表
class UserListSerializer(ModelSerializer):
    profile = SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'last_login',
            'date_joined',
            'profile',
        ]

    def get_profile(self, obj):
        c_qs = Profile.objects.get(user=obj.id)
        profile = UserProfileListSerializer(c_qs).data
        return profile