from django.shortcuts import render
from django.http import (
    HttpRequest,
    HttpResponseRedirect,
)

from bali import settings


def set_language(request: HttpRequest) -> HttpResponseRedirect:
    """
    Функция-контроллер для переключения языка.
    Устанавливает клиенту куки с языком и язык в сессии.
    :param request: Объект запроса.
    :return: Редирект на страницу, откуда пришел запрос, но с новым языком.
    """

    # Принимаем язык из GET-параметра.
    lang = request.GET.get('l', 'en')

    # Меняем язык в сессии и в куки.
    request.session[settings.LANGUAGE_SESSION_KEY] = lang
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)

    # Делаем редирект на страницу, откуда пришел запрос.
    return response
