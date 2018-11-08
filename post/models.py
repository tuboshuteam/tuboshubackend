from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    title = models.CharField(max_length=100)
    views = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=100)

    # collection
    # forward
    # like
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # continent/country/state/city/attractions..
    content = models.TextField()

    # 用户查看detail后调用，阅读量+1
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title