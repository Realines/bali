from django.db import models


class Project(models.Model):
    name = models.TextField(verbose_name='Название проекта')
    address = models.TextField(verbose_name='Адрес')
    price = models.BigIntegerField(verbose_name='Стоимость проекта')
    description = models.TextField(verbose_name='Описание проекта')
    area = models.SmallIntegerField(verbose_name='Площадь')
    count_bedrooms = models.SmallIntegerField(verbose_name='Количество спален')
    view = models.TextField(
        verbose_name='Вид',
        help_text='Открывающийся из виллы вид',
    )
    location = models.ForeignKey(
        'Location',
        verbose_name='Локация',
        on_delete=models.SET_NULL,
        related_name='projects',
        related_query_name='project',
        null=True,
    )
    date_added = models.DateField(
        verbose_name='Дата добавления',
        auto_now_add=True,
    )
    priority = models.SmallIntegerField(
        verbose_name='Приоритет проекта',
        help_text='От этого значения будет зависит выборка рекомендаций',
    )
    categories = models.ManyToManyField(
        'Category',
        verbose_name='Категории',
        related_name='projects',
        related_query_name='project',
        symmetrical=True,
    )
    invested = models.BooleanField(
        verbose_name='Проект подлежит инвестированию',
        default=False,
    )
    main_image = models.ImageField(
        verbose_name='Главное изображение',
        upload_to='sys/projects/',
        null=True,
    )

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self) -> str:
        return str(self.name)


class ProjectGallery(models.Model):
    image = models.ImageField(
        verbose_name='Изображение для проекта',
        upload_to='sys/projects/'
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='images',
    )

    class Meta:
        verbose_name = 'Галерея проекта'
        verbose_name_plural = 'Галереи проектов'

    def __str__(self) -> str:
        return str(self.project)


class Category(models.Model):
    name = models.TextField(verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return str(self.name)


class AdvantagesProject(models.Model):
    name = models.TextField(verbose_name='Название преимущества')
    project = models.ForeignKey(
        Project,
        verbose_name='Проект',
        on_delete=models.CASCADE,
        related_name='advantages',
        related_query_name='advantage',
        null=True,
    )

    class Meta:
        verbose_name = 'Преимущество проекта'
        verbose_name_plural = 'Преимущества проектов'

    def __str__(self) -> str:
        return str(self.name)


class Location(models.Model):
    name = models.TextField(verbose_name='Название локации')

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self) -> str:
        return str(self.name)


class LocationFact(models.Model):
    title = models.TextField(verbose_name='Заголовок факта')
    description = models.TextField(verbose_name='Описание факта')
    location = models.ForeignKey(
        Location,
        verbose_name='Локация',
        on_delete=models.CASCADE,
        related_name='facts',
        related_query_name='fact',
    )

    class Meta:
        verbose_name = 'Факт о локации'
        verbose_name_plural = 'Факты о локациях'

    def __str__(self) -> str:
        return f'{self.location}#{self.pk}'
