# Generated by Django 3.2.9 on 2021-12-06 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20211207_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectgallery',
            name='videoYouTube',
            field=models.URLField(null=True, verbose_name='Видео для проекта'),
        ),
    ]
