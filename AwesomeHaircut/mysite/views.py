from django.http import HttpResponse
from django.shortcuts import Http404
from django.template import loader


def index(request):
    template = loader.get_template('mysite/index.html')
    return HttpResponse(template.render())


def notfound(request, notfound):
    template = loader.get_template('blog/notfound.html')
    context = {
        'path': notfound
    }
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('mysite/about.html')
    return HttpResponse(template.render())