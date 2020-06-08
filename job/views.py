from django.http import HttpResponse


def index (request):
    return HttpResponse('Job')

def indatacollection (request):
    return HttpResponse('Входные наборы данных')


# Create your views here.
