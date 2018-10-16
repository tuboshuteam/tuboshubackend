from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
import os

# 生成放置 avartar 的文件夹
def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    # 这里的id是User表的id
    return os.path.join('userprofile', str(instance.user.id), "avatar", filename)


class Profile(models.Model):
    # User中已有字段：username/password/email/date_joined/last_login
    # 外键链接User
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # 电话号码
    phone = models.TextField(max_length=20, blank=True, verbose_name="电话号码")
    # 性别
    gender = models.CharField(max_length=100, blank=True, verbose_name="性别")
    # 生日
    birthday = models.DateTimeField(null=True, blank=True, verbose_name="生日")
    # 常住地
    address = models.CharField(max_length=200, blank=True, verbose_name="常住地")
    # avatar
    avatar = models.ImageField(blank=True, upload_to=user_directory_path, verbose_name="头像")
    # 个人简介
    bio = models.TextField(max_length=500, blank=True, verbose_name="个人简介")
    # 标签
    tags = models.CharField(max_length=50, blank=True, verbose_name="标签")
    # 等级
    level = models.PositiveIntegerField(default=1, verbose_name="等级")

    def __str__(self):
        return self.user.username


# 定义信号，当创建/更新User实例的时候，Profile模型将会自动的创建/更新。
# 挂接create_user_profile和save_user_profile方法到User模型，无论何时保存事件发生。这种信号被称作post_save。
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()