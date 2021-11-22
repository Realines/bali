from django.db import models
from django.core import validators


class DataConsultation(models.Model):
    phone = models.CharField(
        max_length=32,
        verbose_name='Номер телефона телефона',
    )
    date_submission = models.DateTimeField(
        verbose_name='Дата подачи заявки',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Данные для консультации'
        verbose_name_plural = 'Данные для консультации'

    def __str__(self) -> str:
        return f'Заявка на консультацию#{self.pk}'


class FAQ(models.Model):
    question = models.TextField(verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ на вопрос')

    class Meta:
        verbose_name = 'Часто задаваемый вопрос'
        verbose_name_plural = 'Часто задаваемые вопросы'

    def __str__(self) -> str:
        return str(self.question)


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
    image = models.ImageField(upload_to='sys/projects/')
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='images',
    )


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
        null=True,
    )

    class Meta:
        verbose_name = 'Факт о локации'
        verbose_name_plural = 'Факты о локациях'

    def __str__(self) -> str:
        return f'{self.location}#{self.pk}'


class Quiz(models.Model):
    class OrderType(models.TextChoices):
        RENT = 'R', 'Аренда вилл'
        CONSTRUCTION = 'C', 'Строительство'

    class DistanceToSea(models.TextChoices):
        FIVE_MINUTES = 'M5', '5 минут'
        TEN_MINUTES = 'M10', '10 минут'
        MORE_THEN_FIFTEEN_MINUTES = 'M15', 'от 15 минут'

    class Assessments(models.TextChoices):
        LEVEL_ONE = 'L1', 'Первый уровень'
        LEVEL_TWO = 'L2', 'Второй уровень'
        LEVEL_THREE = 'L3', 'Третий уровень'
        LEVEL_FOUR = 'L4', 'Четвертый уровень'
        LEVEL_FIVE = 'L5', 'Пятый уровень'

    class Budget(models.TextChoices):
        BUDGET_ONE = 'B1', 'от $300.000'
        BUDGET_TWO = 'B2', '$200.000 - $500.000'
        BUDGET_THREE = 'B3', '$500.000 - $1.000.000'
        BUDGET_FOUR = 'B4', '$1.000.000 - $3.000.000'
        BUDGET_FIVE = 'B5', 'Более $3.000.000'

    class CountBedrooms(models.TextChoices):
        ONE_BEDROOM = 'R1', '1 спальня'
        TWO_BEDROOM = 'R2', '2 спальни'
        THREE_BEDROOMS = 'R3', '3 спальни'
        MORE_THEN_FOUR_BEDROOMS = 'R4', '4 спальни и больше'

    client_name = models.CharField(
        max_length=64,
        verbose_name='Имя клиента',
    )
    client_phone = models.CharField(
        max_length=32,
        verbose_name='Номер телефона клиента',
    )
    order_type = models.CharField(
        max_length=8,
        verbose_name='Тип заказа',
        choices=OrderType.choices,
    )
    distance_to_sea = models.CharField(
        max_length=8,
        verbose_name='Расстояние до моря',
        choices=DistanceToSea.choices,
        null=True,
        blank=True,
    )
    profit_assessment = models.CharField(
        max_length=8,
        verbose_name='Важность доходности',
        choices=Assessments.choices,
        null=True,
        blank=True,
    )
    assessment_district = models.CharField(
        max_length=8,
        verbose_name='Важность района',
        choices=Assessments.choices,
        null=True,
        blank=True,
    )
    assessment_distance_to_sea = models.CharField(
        max_length=8,
        verbose_name='Важность расстояния до моря',
        choices=Assessments.choices,
        null=True,
        blank=True,
    )
    rental_period = models.SmallIntegerField( # TODO: Валидатор от 5 до 30.
        verbose_name='Срок аренды',
        validators=[validators.MinValueValidator(5),
                    validators.MaxValueValidator(30)],
        null=True,
        blank=True,
    )
    budget = models.CharField(
        max_length=8,
        verbose_name='Планируемый бюджет',
        choices=Budget.choices,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Квиз'
        verbose_name_plural = 'Квизы'

    def __str__(self) -> str:
        return f'Квиз#{self.pk}'
