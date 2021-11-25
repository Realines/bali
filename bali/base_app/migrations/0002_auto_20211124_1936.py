# Generated by Django 3.2.9 on 2021-11-24 12:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='assessment_distance_to_sea',
            field=models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Важность расстояния до моря'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='assessment_district',
            field=models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Важность района'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='profit_assessment',
            field=models.SmallIntegerField(blank=True, error_messages={'max_value': 'Максимальный оценка: 5', 'min_value': 'Минимальный оценка: 1'}, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Важность доходности'),
        ),
    ]