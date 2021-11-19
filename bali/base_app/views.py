"""
Модуль контроллеров для обработки клиентских запросов.
"""
from django.shortcuts import render
from django.http import (
    HttpRequest,
    HttpResponse,
)


def index(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер для главноый страницы.
    :param request: Объект запроса.
    :return: Возвращает шаблон главной страницы.
    """
    context = {}
    return render(request=request,
                  template_name='base_app/index.html',
                  context=context)


def projects(request: HttpRequest, project_id: int) -> HttpResponse:
    """
    Функция-контроллер для шаблона с проектом.
    :param request: Объект запроса.
    :param project_id: id проекта.
    :return: Возвращает шаблон страницы проекта по id.
    """
    context = {'project_id': project_id}
    return render(request=request,
                  template_name='base_app/projects.html',
                  context=context)
