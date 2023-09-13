from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=timezone.now)


class Comments(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    post = models.ForeignKey(Posts,on_delete=models.CASCADE,default=None)
    content = models.TextField()