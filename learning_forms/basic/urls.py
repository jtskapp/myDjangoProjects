from django.urls import path, include, re_path
from basic import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^orderform/$', views.orderform, name='orderform'),
]
