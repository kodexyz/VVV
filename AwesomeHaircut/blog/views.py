from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import BlogPost

# Create your views here.


def index(request):
    template = loader.get_template('mysite/blog.html')
    context = {
        'last_post': BlogPost.objects.all()[0].title,
        'all_posts': [i.title for i in BlogPost.objects.all()]
    }
    return HttpResponse(template.render(context, request))


def blog_post(request, post_title):
        template = loader.get_template('mysite/post.html')
        context = {
            'title':  post_title,
            'content': BlogPost.objects.get(title=str(post_title)).content
        }
        return HttpResponse(template.render(context, request))
