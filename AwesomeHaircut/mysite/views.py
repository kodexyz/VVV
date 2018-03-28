from django.http import HttpResponse
from django.shortcuts import Http404
from django.template import loader


def index(request):
    template = loader.get_template('mysite/index.html')
    return HttpResponse(template.render())


def notfound(request, notfound):
    template = loader.get_template('mysite/notfound.html')
    context = {
        'path' : notfound
    }
    return HttpResponse(template.render(context, request))


def about(request):
    return notfound(request, 'About')
