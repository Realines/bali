# -*- coding: utf-8 -*-

from modeltranslation.translator import (
    translator,
    TranslationOptions,
)
from base_app.models import FAQ


class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer', )


translator.register(FAQ, FAQTranslationOptions)
