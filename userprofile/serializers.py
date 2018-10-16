from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    DateTimeField,
)

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Profile
from .fields import TimestampField


class ProfileUpdateSerializer(ModelSerializer):
    """
    Profile表的查看、更新
    Profile表必须通过User表才能删除
    并对其验证
    """
    birthday = TimestampField(required=False)

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

    def validate_phone(self, value):
        data = self.get_initial()
        phone = data.get('phone')
        if len(phone) != 11 or not phone.isdigit():
            raise ValidationError("请输入11位电话号码.")
        return value

    def validate_gender(self, value):
        data = self.get_initial()
        gender = data.get('gender')
        gender_list = ['男', '女']
        if gender not in gender_list:
            raise ValidationError("性别必须为'男'或'女'")
        return value


class ProfileListSerializer(ModelSerializer):
    """
    序列化Profile列表，与User表一对一
    """
    birthday = TimestampField()

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


class UserCreateSerializer(ModelSerializer):
    """
    序列化新的User表
    必须的字段：username 用户名；password 密码
    并对其进行验证
    """

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
            username=username,
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


# 改User表
class UserUpdateSerializer(ModelSerializer):
    """
    User表的查看、更新、删除
    并对其验证
    """
    date_joined = TimestampField()
    last_login = TimestampField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'email',
            'last_login',
            'date_joined',
        ]
        read_only_fields = [
            'username',
            'last_login',
            'date_joined',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # 验证password是否合法
    def validate_password(self, value):
        data = self.get_initial()
        password = data.get('password')
        if len(password) < 6:
            raise ValidationError("密码至少6位。")
        return value

    # email数据验证，不允许与已有的email相同
    def validate_email(self, value):
        data = self.get_initial()
        email = data.get('email')
        user_qs = User.objects.exclude(email__isnull=True).exclude(email__exact='').filter(email=email)
        if user_qs.exists():
            raise ValidationError("本邮箱已被注册。")
        return value

    # 更新验证后的数据
    def update(self, instance, validated_data):
        # 获取email
        try:
            email = validated_data['email']
            instance.email = email
        except:
            pass
        # 获取password
        try:
            password = validated_data['password']
            instance.set_password(password)
        except:
            pass
        instance.save()
        return validated_data


# 用户列表
class UserListSerializer(ModelSerializer):
    profile = SerializerMethodField()
    date_joined = TimestampField()
    last_login = TimestampField()

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

    # 获取Profile表
    def get_profile(self, obj):
        c_qs = Profile.objects.get(user=obj.id)
        profile = ProfileListSerializer(c_qs).data
        return profile
