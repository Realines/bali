from django import forms
from django.utils.translation import gettext_lazy as _

from base_app.models import (
    Quiz,
    DataConsultation,
)


class ConsultationForm(forms.ModelForm):
    """Форма консультации"""

    # TODO: Придумать валидацию телфона. Уточнить у Витали.
    phone = forms.CharField(max_length=32, label=_('Ваш номер телефона'),
                            error_messages={'max_length': _('Ограничение по символам: 32')},
                            widget=forms.TextInput(attrs={'placeholder': _('Ваш номер телефона')}))

    class Meta:
        """Класс настроек поведения модели"""
        model = DataConsultation
        fields = ('phone', )


class QuizForm(forms.ModelForm):
    """Форма квиза"""

    client_name = forms.CharField(
        max_length=64,
        label=_('Ваше имя'),
        error_messages={'max_length': _('Слишком длинное имя')},
        widget=forms.TextInput(attrs={'placeholder': _('Ваше имя')}),
        required=False,
    )
    client_phone = forms.CharField(
        max_length=32,
        label=_('Ваш номер телефона'),
        error_messages={'max_length': _('Ограничение по символам: 32')},
        widget=forms.TextInput(attrs={'placeholder': _('Ваш номер телефона')}),
        required=False,
    )
    order_type = forms.ChoiceField(
        label=_('Что вам больше подходит?'),
        label_suffix='',
        choices=Quiz.OrderType.choices,
        error_messages={'invalid_choice': _('Такого варианта нет')},
        widget=forms.RadioSelect(),
        required=False,
    )
    distance_to_sea = forms.ChoiceField(
        label=_('Расстояние виллы до моря?'),
        label_suffix='',
        choices=Quiz.DistanceToSea.choices,
        error_messages={'invalid_choice': _('Такого варианта нет')},
        widget=forms.RadioSelect(),
        required=False,
    )
    profit_assessment = forms.IntegerField(
        label=_('Доходность'),
        label_suffix='',
        error_messages={'min_value': _('Минимальный срок: 5 лет'),
                        'max_value': _('Максимальный срок: 30 лет')},
        required=False,
    )
    assessment_district = forms.IntegerField(
        label=_('Район'),
        label_suffix='',
        error_messages={'min_value': _('Минимальный срок: 5 лет'),
                        'max_value': _('Максимальный срок: 30 лет')},
        required=False,
    )
    assessment_distance_to_sea = forms.IntegerField(
        label=_('Расстояние до моря'),
        label_suffix='',
        error_messages={'min_value': _('Минимальный срок: 5 лет'),
                        'max_value': _('Максимальный срок: 30 лет')},
        required=False,
    )
    rental_period = forms.IntegerField(
        label=_('Срок аренды виллы?'),
        label_suffix='',
        error_messages={'min_value': _('Минимальный срок: 5 лет'),
                        'max_value': _('Максимальный срок: 30 лет')},
        widget=forms.NumberInput(attrs={'type': 'range'}),
        required=False,
    )
    budget = forms.ChoiceField(
        label=_('Укажите Ваш планируемый бюджет инвестирования'),
        label_suffix='',
        choices=Quiz.Budget.choices,
        error_messages={'invalid_choice': _('Такого варианта нет')},
        widget=forms.RadioSelect(),
        required=False,
    )


    class Meta:
        """Класс настроек поведения модели"""
        model = Quiz
        fields = '__all__'
