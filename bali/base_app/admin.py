from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from base_app.models import (
    DataConsultation,
    FAQ,
    Quiz,
)


@admin.register(DataConsultation)
class DataConsultationAdmin(admin.ModelAdmin):
    list_display = ('phone', 'date_submission')
    list_display_links = ('phone', )
    ordering = ('-date_submission', )


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_phone',
                    'order_type', 'budget')
    list_display_links = ('client_name', 'client_phone',
                          'order_type', 'budget')


@admin.register(FAQ)
class FAQAdmin(TabbedTranslationAdmin):
    list_display = ('question', 'answer', )
    list_display_links = ('question', )
