from django.db import models
from django.utils import timezone


# Create your models here.
class Admins(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    info = models.TextField()
    right = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.login

# class Roles(models.Model):
#     NameRole = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.NameRole
