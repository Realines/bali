# Generated by Django 3.2.9 on 2021-11-22 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_projectgallery_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectgallery',
            name='image',
            field=models.ImageField(upload_to='sys/projects/', verbose_name='Изображение для проекта'),
        ),
    ]
