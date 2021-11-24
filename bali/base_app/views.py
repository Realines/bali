import json

from django.shortcuts import render
from django.http import (
    HttpRequest,
    HttpResponse,
    JsonResponse,
)
from django.utils.translation import gettext as _

from base_app.models import FAQ
from base_app.forms import (
    ConsultationForm,
    QuizForm,
)

from projects.models import Project


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
        return JsonResponse({'errors': quiz_form.errors}, status=201,
                            json_dumps_params={'ensure_ascii': False})

    return JsonResponse({'msg': _('OK')}, status=201,
                        json_dumps_params={'ensure_ascii': False})


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
        return JsonResponse({'errors': consult_form.errors}, status=403,
                            json_dumps_params={'ensure_ascii': False})

    return JsonResponse({'msg': _('OK')}, status=201,
                        json_dumps_params={'ensure_ascii': False})
