from django.db import models


# Create your models here.
class Admins(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    info = models.TextField()
    right = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.login
