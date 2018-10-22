from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')

    title = models.CharField(max_length=100)
    views = models.PositiveIntegerField(default=0)
    # collection
    # forward
    # like
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # continent/country/state/city/attractions..
    content = models.TextField()
