from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.db.models import (
    Count,
    Q,
)

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
