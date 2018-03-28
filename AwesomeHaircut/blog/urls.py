from django.urls import path

from . import views
from mysite.views import notfound

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:notfound>', notfound, name='notfound')
]