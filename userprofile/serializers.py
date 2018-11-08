from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    DateTimeField,
)

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Profile
from utils.fields import TimestampField

from post.serializers import (
    PostDetailSerializer,
    PostUserSerializer,
)


class UserCreateSerializer(ModelSerializer):
    """
    序列化新的User表
    必须的字段：username 用户名；password 密码
    并对数据进行验证、保存
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

    # 验证password是否大于6位
    def validate_password(self, value):
        data = self.get_initial()
        password = data.get('password')
        if len(password) < 6:
            raise ValidationError("密码至少6位。")
        return value

    # 创建新的模型
    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user_obj = User(
            username=username,
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class ProfileDetailSerializer(ModelSerializer):
    """
    Profile表的查看、更新
    Profile表必须通过User表才能删除
    并对数据验证
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
        read_only_fields = [
            'level',
        ]

    # 验证电话号码是否合法
    def validate_phone(self, value):
        if len(value) != 11 or not value.isdigit():
            raise ValidationError("请输入11位电话号码.")
        return value

    # 验证性别是否正确
    def validate_gender(self, value):
        gender_list = ['男', '女']
        if value not in gender_list:
            raise ValidationError("性别必须为'男'或'女'")
        return value


class UserDetailSerializer(ModelSerializer):
    """
    User表的查看、更新、删除
    """
    date_joined = TimestampField(read_only=True)
    last_login = TimestampField(read_only=True)
    profile = ProfileDetailSerializer()
    post = PostUserSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'email',
            'last_login',
            'date_joined',
            'profile',
            'post',
        ]
        read_only_fields = [
            'username',
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

    def update(self, instance, validated_data):
        """
        更新User表、Profile表的数据
        :param instance: 待更新的模型实例
        :param validated_data: 用户提交的数据
        :return: 模型实例
        """

        # 更新Profile数据
        if 'profile' in validated_data:
            profile_data = validated_data.pop('profile')
            profile = Profile.objects.get(id=instance.id)
            profile.user = instance
            # 循环检查数据更新
            for key, value in profile_data.items():
                setattr(profile, key, value)
            profile.save()

        # 更新User数据
        if 'email' in validated_data:
            instance.email = validated_data['email']
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance


class ProfileListSerializer(ModelSerializer):
    """
    序列化Profile列表，与User表一对一关联
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


class UserListSerializer(ModelSerializer):
    """
    User用户列表
    含有拓展的Profile用户数据列表
    """
    url = HyperlinkedIdentityField(view_name="userprofile:detail")

    profile = SerializerMethodField()
    date_joined = TimestampField()
    last_login = TimestampField()

    class Meta:
        model = User
        fields = [
            'url',
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
