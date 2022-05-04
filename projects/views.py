import json
from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.http import (
    HttpRequest,
    HttpResponse,
    JsonResponse,
)
from django.db.models import (
    Count,
    Q,
)
from django.core.paginator import Paginator

from projects.models import Project
from base_app.forms import ConsultationForm


def projects(request: HttpRequest, project_id: int) -> HttpResponse:
    """
    Функция-контроллер для шаблона с проектом.
    :param request: Объект запроса.
    :param project_id: id проекта.
    :return: Возвращает шаблон страницы проекта по id.
    """

    # Текущий проект либо ошибка 404.
    current_project = get_object_or_404(Project, pk=project_id)
    consult_form = ConsultationForm()

    # Проекты в ленту рекомендаций.
    # Проекты отсортированы по количествую совпавших категорий
    # с категориями исходного проекта (current_project).
    recommended_projects = Project.objects\
        .exclude(pk=project_id)\
        .filter(public=True)\
        .annotate(matching_cat=Count('categories',
                                     filter=Q(categories__in=current_project.categories.all()),
                                     distinct=True))\
        .order_by('-matching_cat')

    context = {'current_project': current_project,
               'recommended_projects': recommended_projects,
               'consult_form': consult_form}

    return render(request=request,
                  template_name='projects/projects.html',
                  context=context)


# def projects_paginator(request: HttpRequest) -> JsonResponse:
#     """
#     Контроллер для пагинации по списку проектов на главной.
#
#     :param request: Объект запроса.
#     :return: Список данных о проекта в JSON.
#     """
#
#     current_page_num = request.GET.get('page_num', 1)
#
#     count_projects_in_part = 3
#     queryset = Project.objects.all()
#     paginator = Paginator(queryset, count_projects_in_part,
#                           allow_empty_first_page=False)
#
#     page = paginator.get_page(current_page_num)
#     projects_set = page.object_list
#     json_projects = [{
#         'img_src': project.main_image.url,
#         'name': project.name,
#         'url': project.get_absolute_url(),
#     } for project in projects_set]
#
#     return JsonResponse(data=json_projects, safe=False)
