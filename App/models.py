from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
import copy
from django.forms import ModelForm, forms



# Create your models here.


class Song(models.Model):
    title = models.TextField(verbose_name='Название')
    artist = models.TextField(verbose_name='Исполнитель')
    image = models.ImageField(verbose_name='Обложка')
    audio_file = models.FileField(blank=True, null=True, verbose_name='Аудио-файл')
    audio_link = models.CharField(max_length=200, blank=True, null=True, verbose_name='Аудио-ссылка' )
    duration = models.CharField(max_length=20, verbose_name='Длина трека')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, verbose_name='Жанр')
    paginate_by = 2

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('PersonalArea', args=[str(self.id)])


class Loved(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    artist = models.CharField(max_length=255, verbose_name='Исполнитель')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('PersonalArea', args=[str(self.id)])





class Genre(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

