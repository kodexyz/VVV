from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import Http404

#from .models import BlogPost

# Create your views here.

#all_posts = [i.title for i in BlogPost.objects.all()]


def index(request):
    template = loader.get_template('blog/blog.html')
    context = {
        'last_post': "all_posts[0]",
        'all_posts': "all_posts"
    }
    return HttpResponse(template.render(context, request))


def blog_post(request, post_title):
    if post_title not in all_posts:
        template = loader.get_template('blog/blog_not_found.html')
        context = {
            'last_post': "all_posts[0]",
            'all_posts': "all_posts",
            'title': post_title,
            'content': "How about a sonnet?\nNo\nshe exclaimed."
        }
        return HttpResponse(template.render(context, request))

    template = loader.get_template('blog/post.html')
    context = {
        'title':  post_title,
        'content': BlogPost.objects.get(title=str(post_title)).content
    }
    return HttpResponse(template.render(context, request))

