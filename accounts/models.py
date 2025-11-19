from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
 
    pass

class NewsPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)