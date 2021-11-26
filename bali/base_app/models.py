"""
Модуль моделей базового приложения.

Хранит в себе все модели, относящиеся к этому приложению.

Особые приметы:
    1. С помощью django.utils.translation.gettext_lazy
    сгенерированы файлы переводов. В них указываются переводы
    для каждого языка, указанного в settings.py.
"""


from django.db import models
from django.core import validators
from django.utils.translation import gettext_lazy as _


class FAQ(models.Model):
    """Модель часто задаваемых вопросов"""

    question = models.TextField(verbose_name=_('Вопрос'))
    answer = models.TextField(verbose_name=_('Ответ на вопрос'))

    class Meta:
        """Класс настроек поведения модели"""
        verbose_name = _('Часто задаваемый вопрос')
        verbose_name_plural = _('Часто задаваемые вопросы')

    def __str__(self) -> str:
        """Метод для строкового представления объекта"""
        return str(self.question)


class DataConsultation(models.Model):
    """Модель для заявок на консультацию"""

    phone = models.CharField(
        max_length=32,
        verbose_name=_('Номер телефона телефона'),
    )
    date_submission = models.DateTimeField(
        verbose_name=_('Дата подачи заявки'),
        auto_now_add=True,
    )

    class Meta:
        """Класс настроек поведения модели"""
        verbose_name = _('Данные для консультации')
        verbose_name_plural = _('Данные для консультации')

    def __str__(self) -> str:
        """Метод для строкового представления объекта"""
        return _('Заявка на консультацию') + '#' + str(self.pk)


class Quiz(models.Model):
    """Модель для результатов прохождения квиза"""

    class OrderType(models.TextChoices):
        """Перечисление для выбора типа заказа"""
        RENT = 'R', _('Аренда вилл')
        CONSTRUCTION = 'C', _('Строительство')

    class DistanceToSea(models.TextChoices):
        """Перечисление для выбора времени до моря"""
        FIVE_MINUTES = 'M5', _('5 минут')
        TEN_MINUTES = 'M10', _('10 минут')
        MORE_THEN_FIFTEEN_MINUTES = 'M15', _('от 15 минут')

    class Budget(models.TextChoices):
        """Перечисление для выбора бюджета"""
        BUDGET_ONE = 'B1', _('от $300.000')
        BUDGET_TWO = 'B2', _('$200.000 - $500.000')
        BUDGET_THREE = 'B3', _('$500.000 - $1.000.000')
        BUDGET_FOUR = 'B4', _('$1.000.000 - $3.000.000')
        BUDGET_FIVE = 'B5', _('Более $3.000.000')

    class CountBedrooms(models.TextChoices):
        """Перечисление для выбора кол-ва комнат"""
        ONE_BEDROOM = 'R1', _('1 спальня')
        TWO_BEDROOM = 'R2', _('2 спальни')
        THREE_BEDROOMS = 'R3', _('3 спальни')
        MORE_THEN_FOUR_BEDROOMS = 'R4', _('4 спальни и больше')

    client_name = models.CharField(
        max_length=64,
        verbose_name=_('Имя клиента'),
    )
    client_phone = models.CharField(
        max_length=32,
        verbose_name=_('Номер телефона клиента'),
    )
    order_type = models.CharField(
        max_length=8,
        verbose_name=_('Тип заказа'),
        choices=OrderType.choices,
    )
    distance_to_sea = models.CharField(
        max_length=8,
        verbose_name=_('Расстояние до моря'),
        choices=DistanceToSea.choices,
        null=True,
        blank=True,
    )
    profit_assessment = models.SmallIntegerField(
        verbose_name=_('Важность доходности'),
        validators=[validators.MinValueValidator(1),
                    validators.MaxValueValidator(5)],
        error_messages={'min_value': _('Минимальный оценка: 1'),
                        'max_value': _('Максимальный оценка: 5')},
        null=True,
        blank=True,
    )
    assessment_district = models.SmallIntegerField(
        verbose_name=_('Важность района'),
        validators=[validators.MinValueValidator(1),
                    validators.MaxValueValidator(5)],
        null=True,
        blank=True,
    )
    assessment_distance_to_sea = models.SmallIntegerField(
        verbose_name=_('Важность расстояния до моря'),
        validators=[validators.MinValueValidator(1),
                    validators.MaxValueValidator(5)],
        null=True,
        blank=True,
    )
    rental_period = models.SmallIntegerField(
        verbose_name=_('Срок аренды'),
        validators=[validators.MinValueValidator(5),
                    validators.MaxValueValidator(30)],
        null=True,
        blank=True,
    )
    budget = models.CharField(
        max_length=8,
        verbose_name=_('Планируемый бюджет'),
        choices=Budget.choices,
        null=True,
        blank=True,
    )
    villa_area = models.CharField(
        max_length=8,
        verbose_name=_('Площадь виллы'),
        choices=CountBedrooms.choices,
        null=True,
        blank=True,
    )

    class Meta:
        """Класс настроек поведения модели"""
        verbose_name = _('Квиз')
        verbose_name_plural = _('Квизы')

    def __str__(self) -> str:
        """Метод для строкового представления объекта"""
        return _('Квиз') + '#' + str(self.pk)
