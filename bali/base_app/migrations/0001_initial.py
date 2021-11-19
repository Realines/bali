# Generated by Django 3.2.9 on 2021-11-17 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название категории')),
                ('priority', models.SmallIntegerField(help_text='Чем больше значение, тем важнее будеткатегория при отборе проектов в рекомендации', verbose_name='Вес категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='DataConsultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=32, verbose_name='Номер телефона телефона')),
                ('date_submission', models.DateTimeField(auto_now_add=True, verbose_name='Дата подачи заявки')),
            ],
            options={
                'verbose_name': 'Данные для консультации',
                'verbose_name_plural': 'Данные для консультации',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Ответ на вопрос')),
                ('tes', models.CharField(choices=[('s', 'sdf'), ('q', 'qwe')], max_length=6, verbose_name='test')),
            ],
            options={
                'verbose_name': 'Часто задаваемый вопрос',
                'verbose_name_plural': 'Часто задаваемые вопросы',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название локации')),
            ],
            options={
                'verbose_name': 'Локация',
                'verbose_name_plural': 'Локации',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название проекта')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('price', models.BigIntegerField(verbose_name='Стоимость проекта')),
                ('description', models.TextField(verbose_name='Описание проекта')),
                ('area', models.SmallIntegerField(verbose_name='Площадь')),
                ('count_bedrooms', models.SmallIntegerField(verbose_name='Количество спален')),
                ('view', models.TextField(help_text='Открывающийся из виллы вид', verbose_name='Вид')),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='Дата добавления')),
                ('priority', models.SmallIntegerField(help_text='От этого значения будет зависит выборка рекомендаций', verbose_name='Приоритет проекта')),
                ('categories', models.ManyToManyField(related_name='projects', related_query_name='project', to='base_app.Category', verbose_name='Категории')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', related_query_name='project', to='base_app.location', verbose_name='Локация')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='LocationFact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Заголовок факта')),
                ('description', models.TextField(verbose_name='Описание факта')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='facts', related_query_name='fact', to='base_app.location', verbose_name='Локация')),
            ],
            options={
                'verbose_name': 'Факт о локации',
                'verbose_name_plural': 'Факты о локациях',
            },
        ),
        migrations.CreateModel(
            name='AdvantagesProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название преимущества')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advantages', related_query_name='advantage', to='base_app.project', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Преимущество проекта',
                'verbose_name_plural': 'Преимущества проектов',
            },
        ),
    ]
