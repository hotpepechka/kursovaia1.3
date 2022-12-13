from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Song(models.Model):
    title = models.TextField()
    artist = models.TextField()
    image = models.ImageField()
    audio_file = models.FileField(blank=True, null=True)
    audio_link = models.CharField(max_length=200, blank=True, null=True)
    duration = models.CharField(max_length=20)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    paginate_by = 2

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('PersonalArea', args=[str(self.id)])


class Loved(models.Model):
    title = models.TextField()
    artist = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('PersonalArea', args=[str(self.id)])


class Genre(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

