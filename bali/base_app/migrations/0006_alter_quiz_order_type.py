# Generated by Django 3.2.9 on 2021-11-17 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0005_alter_quiz_order_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='order_type',
            field=models.IntegerField(choices=[(None, 'Выберите тип заказа'), (1, 'Аренда вилл'), (2, 'Строительство')], verbose_name='Тип заказа'),
        ),
    ]
