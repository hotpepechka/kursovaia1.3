from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class MEOW(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.user

