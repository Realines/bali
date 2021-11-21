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
    OuterRef,
    Subquery,
    F,
    Q,
)

from base_app.models import (
    FAQ,
    Project,
    Category,
)
from base_app.forms import (
    ConsultationForm,
    QuizForm,
)


def index(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер для главноый страницы.
    :param request: Объект запроса.
    :return: Возвращает шаблон главной страницы.
    """

    # Данные для контекста шаблона.
    faq = FAQ.objects.all()
    all_project = Project.objects.all()
    invested_projects = all_project.filter(invested=True)
    not_invested_projects = all_project.difference(invested_projects)

    # Формы консультации и квиза.
    consult_form = ConsultationForm()
    quiz_form = QuizForm()

    context = {'faq': faq,
               'invested_projects': invested_projects,
               'not_invested_projects': not_invested_projects,
               'consult_form': consult_form,
               'quiz_form': quiz_form}

    return render(request=request,
                  template_name='base_app/index.html',
                  context=context)


def quiz_handler(request: HttpRequest) -> JsonResponse:
    """
    Функция-контроллер для обработки формы квиза.
    :param request: Объект запроса.
    :return: JSON-объект с кодом успеха либо словарем ошибок.
    """

    # Получение данных из формы.
    quiz_form = QuizForm(request.POST)

    # Валидация данных в форме.
    if quiz_form.is_valid():
        quiz_form.save()
    else:
        return JsonResponse({'errors': quiz_form.errors},
                            status=403)

    return JsonResponse({'msg': 'OK'}, status=201)


def consult_handler(request: HttpRequest) -> JsonResponse:
    """
    Функция-контроллер для обработки формы консультации.
    :param request: Объект запроса.
    :return: JSON-объект с кодом успеха либо словарем ошибок.
    """

    # Получение данных из формы.
    consult_form = ConsultationForm(request.POST)

    # Валидация данных в форме.
    if consult_form.is_valid():
        consult_form.save()
    else:
        return JsonResponse({'errors': consult_form.errors},
                            status=403)

    return JsonResponse({'msg': 'OK'}, status=201)


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
    recommended_projects = Project.objects.exclude(pk=project_id).annotate(matching_cat=Count(
        'categories', filter=Q(categories__in=current_project.categories.all()), distinct=True)
    ).order_by('-matching_cat')

    context = {'current_project': current_project,
               'recommended_projects': recommended_projects,
               'consult_form': consult_form}

    return render(request=request,
                  template_name='base_app/projects.html',
                  context=context)
