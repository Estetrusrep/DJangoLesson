from django.http import HttpResponse


def index (request):
    return HttpResponse('Job')

def indatacollection (request):
    return HttpResponse('Входные наборы данных')

def jobdata (request):
    return HttpResponse('параметры анализа')

def jobresult (request):
    return HttpResponse('Результаты анализа')


# Create your views here.
