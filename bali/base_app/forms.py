from django import forms
from django.core import validators

from base_app.models import (
    Quiz,
    DataConsultation,
)


class ConsultationForm(forms.ModelForm):
    # TODO: Придумать валидацию телфона. Уточнить у Витали.
    phone = forms.CharField(max_length=32, label='Ваш номер телефона',
                            error_messages={'max_length': 'Ограничение по символам: 32'},
                            widget=forms.TextInput(attrs={'placeholder': 'Ваш номер телефона'}))

    class Meta:
        model = DataConsultation
        fields = ('phone', )


class QuizForm(forms.ModelForm):
    client_name = forms.CharField(
        max_length=64,
        label='Ваше имя',
        error_messages={'max_length': 'Слишком длинное имя'},
        widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
        required=False,
    )
    client_phone = forms.CharField(
        max_length=32,
        label='Ваш номер телефона',
        error_messages={'max_length': 'Ограничение по символам: 32'},
        widget=forms.TextInput(attrs={'placeholder': 'Ваш номер телефона'}),
        required=False,
    )
    order_type = forms.ChoiceField(
        label='Что вам больше подходит?',
        label_suffix='',
        choices=Quiz.OrderType.choices,
        error_messages={'invalid_choice': 'Такого варианта нет'},
        widget=forms.RadioSelect(),
        required=False,
    )
    distance_to_sea = forms.ChoiceField(
        label='Расстояние виллы до моря?',
        label_suffix='',
        choices=Quiz.DistanceToSea.choices,
        error_messages={'invalid_choice': 'Такого варианта нет'},
        widget=forms.RadioSelect(),
        required=False,
    )
    profit_assessment = forms.IntegerField(
        label='Доходность',
        label_suffix='',
        error_messages={'min_value': 'Минимальный срок: 5 лет',
                        'max_value': 'Максимальный срок: 30 лет'},
        widget=forms.RadioSelect(),
        required=False,
    )
    assessment_district = forms.IntegerField(
        label='Район',
        label_suffix='',
        error_messages={'min_value': 'Минимальный срок: 5 лет',
                        'max_value': 'Максимальный срок: 30 лет'},
        required=False,
    )
    assessment_distance_to_sea = forms.IntegerField(
        label='Расстояние до моря',
        label_suffix='',
        error_messages={'min_value': 'Минимальный срок: 5 лет',
                        'max_value': 'Максимальный срок: 30 лет'},
        required=False,
    )
    rental_period = forms.IntegerField(
        label='Срок аренды виллы?',
        label_suffix='',
        error_messages={'min_value': 'Минимальный срок: 5 лет',
                        'max_value': 'Максимальный срок: 30 лет'},
        widget=forms.NumberInput(attrs={'type': 'range'}),
        required=False,
    )
    budget = forms.ChoiceField(
        label='Укажите Ваш планируемый бюджет инвестирования',
        label_suffix='',
        choices=Quiz.Budget.choices,
        error_messages={'invalid_choice': 'Такого варианта нет'},
        widget=forms.RadioSelect(),
        required=False,
    )

    class Meta:
        model = Quiz
        fields = '__all__'
