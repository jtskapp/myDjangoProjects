from django.urls import path, re_path, include
from django.conf.urls import url
from secondapp import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'index/$', views.index, name='index'),
    re_path(r'help/$', views.help, name='help')
]
