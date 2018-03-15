from django.http import HttpResponse
from django.shortcuts import Http404


def index(request):
    return HttpResponse("<h1>Hola index!</h1>")

