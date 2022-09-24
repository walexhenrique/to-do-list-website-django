from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField(verbose_name='Description', blank=True)
    is_published = models.BooleanField(default=False, blank=True)
    is_finished = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title

