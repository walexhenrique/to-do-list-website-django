from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField(verbose_name='Description', blank=True)
    is_published = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

