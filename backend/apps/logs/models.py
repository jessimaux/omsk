from django.db import models
from django.contrib.auth.models import User


class Log(models.Model):
    object_type = models.CharField(max_length=255)
    object_id = models.IntegerField()
    action = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    