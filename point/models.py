from django.db import models

from post.models import Post

# Create your models here.
class Point(models.Model):
    # Post外键
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='point')
    # 经度
    longitude = models.FloatField()
    # 纬度
    latitude = models.FloatField()
    # Point起始时间
    travel_date_time = models.DateTimeField()
    # Point名称
    name = models.TextField(blank=True)
    # 花销
    expend = models.FloatField(null=True)
    # 正文
    content = models.TextField(blank=True)
    # img
    # video
    # comment

    def __str__(self):
        return self.name
