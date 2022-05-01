from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    """Модель проекта"""

    name = models.TextField(verbose_name=_('Название проекта'))
    address = models.TextField(verbose_name=_('Адрес'))
    price = models.BigIntegerField(verbose_name=_('Стоимость проекта'))
    description = models.TextField(verbose_name=_('Описание проекта'))
    area = models.SmallIntegerField(verbose_name=_('Площадь'))
    count_bedrooms = models.SmallIntegerField(verbose_name=_('Количество спален'))
    view = models.TextField(
        verbose_name=_('Вид'),
        help_text=_('Открывающийся из виллы вид'),
    )
    location = models.ForeignKey(
        'Location',
        verbose_name=_('Локация'),
        on_delete=models.SET_NULL,
        related_name='projects',
        related_query_name='project',
        null=True,
    )
    date_added = models.DateField(
        verbose_name=_('Дата добавления'),
        auto_now_add=True,
    )
    categories = models.ManyToManyField(
        'Category',
        verbose_name=_('Категории'),
        related_name='projects',
        related_query_name='project',
    )
    invested = models.BooleanField(
        verbose_name=_('Проект подлежит инвестированию'),
        default=False,
    )
    public = models.BooleanField(
        verbose_name=_('Опубликовать'),
        default=False,
    )
    main_image = models.ImageField(
        verbose_name=_('Главное изображение'),
        upload_to='sys/projects/',
        null=True,
    )

    class Meta:
        """Класс настроек поведения модели"""

        verbose_name = _('Проект')
        verbose_name_plural = _('Проекты')

    def get_absolute_url(self) -> str:
        return reverse('projects:projects', args=(self.pk, ))

    def __str__(self) -> str:
        """Метод для строкового представления объекта"""

        return str(self.name)


class ProjectGallery(models.Model):
    """Модель галереи для проекта"""

    image = models.ImageField(
        verbose_name=_('Изображение для проекта'),
        upload_to='sys/projects/',
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='images',
    )

    class Meta:
        """Класс настроек поведения модели"""

        verbose_name = _('Галерея проекта')
        verbose_name_plural = _('Галереи проектов')

    def __str__(self) -> str:
        """Метод для строкового представления объекта"""

        return str(self.project)


class Category(models.Model):
    """Модель категории проекта"""

    name = models.TextField(verbose_name=_('Название категории'))

    class Meta:
        """Класс настроек поведения модели"""

        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    def __str__(self) -> str:
        """Метод для строкового представления объекта"""

        return str(self.name)


class AdvantagesProject(models.Model):
    """Модель преимущества проекта"""

    name = models.TextField(verbose_name=_('Название преимущества'))
    project = models.ForeignKey(
        Project,
        verbose_name=_('Проект'),
        on_delete=models.CASCADE,
        related_name='advantages',
        related_query_name='advantage',
        null=True,
    )

    class Meta:
        """Класс настроек поведения модели"""

        verbose_name = _('Преимущество проекта')
        verbose_name_plural = _('Преимущества проектов')

    def __str__(self) -> str:
        """Метод для строкового представления объекта"""

        return str(self.name)


class Location(models.Model):
    """Модель локации проекта"""

    name = models.TextField(verbose_name=_('Название локации'))

    class Meta:
        """Класс настроек поведения модели"""

        verbose_name = _('Локация')
        verbose_name_plural = _('Локации')

    def __str__(self) -> str:
        """Метод для строкового представления объекта"""

        return str(self.name)


class LocationFact(models.Model):
    """Модель факта о локации проекта"""

    title = models.TextField(verbose_name=_('Заголовок факта'))
    description = models.TextField(verbose_name=_('Описание факта'))
    location = models.ForeignKey(
        Location,
        verbose_name=_('Локация'),
        on_delete=models.CASCADE,
        related_name='facts',
        related_query_name='fact',
    )

    class Meta:
        """Класс настроек поведения модели"""

        verbose_name = _('Факт о локации')
        verbose_name_plural = _('Факты о локациях')

    def __str__(self) -> str:
        """Метод для строкового представления объекта"""

        return f'{self.location}#{self.pk}'
