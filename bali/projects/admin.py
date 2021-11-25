"""
Модуль для регистрации моделей приложения проектов в админке.

Особые приметы:
    1. Модуль modeltranslation, запущенный раньше модуля
    django.contrib.admin (хотя, строго говоря, этот модуль использует
    django.contrib.admin, наследуя его функционал), регистрирует в
    себе модифицированные модели с доп. полями для перевода. Т.е. наши
    модели будут модифицированы без непосредственного изменения их в коде.

    2. Для удобного отображения дополнительных полей для ввода перевода на
    другие языки, модели, подлежащие регистрации в админке, унаследованы от
    TabbedTranslationAdmin, что позволяет отображать доп. поля в кладках по языкам.

    3. Некоторые класс не зарегистрированны напрямую в админке.
    Вместо этого они встроены в другие класс-регистраторы с помощью
    TabbedTranslationAdmin. Это сделано во имя удобства создания каких-либо
    записей в БД.
"""

from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from projects.models import (
    Project,
    Category,
    AdvantagesProject,
    Location,
    LocationFact,
    ProjectGallery,
)


@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    list_display = ('name', )
    list_display_links = ('name', )


class LocationFactInline(admin.TabularInline):
    model = LocationFact


@admin.register(Location)
class LocationAdmin(TabbedTranslationAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    inlines = [
        LocationFactInline,
    ]


class AdvantagesProjectInline(admin.TabularInline):
    model = AdvantagesProject


class GalleryInline(admin.TabularInline):
    fk_name = 'project'
    model = ProjectGallery


@admin.register(Project)
class ProjectAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'price', 'description')
    list_display_links = ('name', 'price')
    ordering = ('-date_added', )
    inlines = [
        GalleryInline,
        AdvantagesProjectInline,
    ]
