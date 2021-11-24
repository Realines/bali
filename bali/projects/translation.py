# -*- coding: utf-8 -*-

from modeltranslation.translator import (
    translator,
    TranslationOptions,
)
from projects.models import (
    Project,
    Category,
    AdvantagesProject,
    Location,
    LocationFact,
)


class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'address',
              'description', 'view', )


class CategoryTranslationsOptions(TranslationOptions):
    fields = ('name', )


class AdvantagesProjectTranslationOptions(TranslationOptions):
    fields = ('name', )


class LocationTranslationOptions(TranslationOptions):
    fields = ('name', )


class LocationFactTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


translator.register(Project, ProjectTranslationOptions)
translator.register(Category, CategoryTranslationsOptions)
translator.register(AdvantagesProject, AdvantagesProjectTranslationOptions)
translator.register(Location, LocationTranslationOptions)
translator.register(LocationFact, LocationFactTranslationOptions)
