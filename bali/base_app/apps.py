from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BaseAppConfig(AppConfig):
    """Класс конфигурации приложения"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_app'
    verbose_name = _('Базовое приложение')
