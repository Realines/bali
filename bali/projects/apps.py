from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProjectsConfig(AppConfig):
    """Класс конфигурации приложения"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projects'
    verbose_name = _('Проекты')
