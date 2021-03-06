from django.db import models
from django.contrib.auth.models import User

from post.models import Post

# Create your models here.

class Comment(models.Model):
    """
    评论model
    """
    post = models.ForeignKey(Post, models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, models.CASCADE, related_name='comment')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
