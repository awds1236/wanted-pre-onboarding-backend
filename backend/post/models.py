from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

class Post(models.Model):

    post_title = models.CharField(max_length=200)
    post_content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.post_title
