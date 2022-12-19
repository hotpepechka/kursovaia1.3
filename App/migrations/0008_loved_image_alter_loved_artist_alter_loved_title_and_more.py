# Generated by Django 4.1.4 on 2022-12-16 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_song_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='loved',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='App.song'),
        ),
        migrations.AlterField(
            model_name='loved',
            name='artist',
            field=models.CharField(max_length=255, verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='loved',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.TextField(verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Аудио-файл'),
        ),
        migrations.AlterField(
            model_name='song',
            name='audio_link',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Аудио-ссылка'),
        ),
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.CharField(max_length=20, verbose_name='Длина трека'),
        ),
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.genre', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Обложка'),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.TextField(verbose_name='Название'),
        ),
    ]