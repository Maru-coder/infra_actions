from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получи_лось_!')


def second_page(request):
    return HttpResponse('А это вторая страница')
