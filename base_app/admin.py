"""
Модуль для регистрации моделей базового приложения в админке.

Особые приметы:
    1. Модуль modeltranslation, запущенный раньше модуля
    django.contrib.admin (хотя, строго говоря, этот модуль использует
    django.contrib.admin, наследуя его функционал), регистрирует в
    себе модифицированные модели с доп. полями для перевода. Т.е. наши
    модели будут модифицированы без непосредственного изменения их в коде.

    2. Для удобного отображения дополнительных полей для ввода перевода на
    другие языки, модели, подлежащие регистрации в админке, унаследованы от
    TabbedTranslationAdmin, что позволяет отображать доп. поля в кладках по языкам.
"""

from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from base_app.models import (
    DataConsultation,
    FAQ,
    Quiz,
)


@admin.register(DataConsultation)
class DataConsultationAdmin(admin.ModelAdmin):
    """Класс для регистрации DataConsultation"""
    list_display = ('phone', 'date_submission')
    list_display_links = ('phone', )
    ordering = ('-date_submission', )


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    """Класс для регистрации Quiz"""
    list_display = ('client_name', 'client_phone',
                    'order_type', 'budget')
    list_display_links = ('client_name', 'client_phone',
                          'order_type', 'budget')


@admin.register(FAQ)
class FAQAdmin(TabbedTranslationAdmin):
    """Класс для регистрации FAQ"""
    list_display = ('question', 'answer', )
    list_display_links = ('question', )
