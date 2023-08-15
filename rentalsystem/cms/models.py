from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser


class Item(models.Model):
    item_name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    mount = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.item_name

class Action(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.action_type} {self.item.item_name} at {self.timestamp}"
