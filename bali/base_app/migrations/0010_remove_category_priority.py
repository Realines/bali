# Generated by Django 3.2.9 on 2021-11-18 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0009_alter_category_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='priority',
        ),
    ]