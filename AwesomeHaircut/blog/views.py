from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import BlogPost

# Create your views here.


def index(request):
    template = loader.get_template('mysite/blog.html')
    context = {
        'last_post' : BlogPost.objects.all()[0].title
    }
    return HttpResponse(template.render(context, request))


def blog_post(request, title):
        template = loader.get_template('mysite/post.html')
        context = {
            'title':title,
            'content': BlogPost.objects.all()[0].content
        }
        return HttpResponse(template.render(context, request))
