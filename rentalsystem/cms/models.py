from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    grade = models.IntegerField()  # 例: 1, 2, 3... などのグレード番号
    status = models.CharField(max_length=255)  # 例: 'active', 'inactive' など

    def __str__(self):
        return self.username

class Item(models.Model):
    item_name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)  # 例: 'available', 'rented' など
    category = models.CharField(max_length=255)  # 例: 'camera', 'lens' など
    mount = models.CharField(max_length=255)  # 例: 'EF', 'RF', 'E-mount' など

    def __str__(self):
        return self.item_name

class Action(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=255)  # 例: 'borrowed', 'returned' など
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.action_type} {self.item.item_name} at {self.timestamp}"


