from django.urls import path, include, re_path
from django.conf.urls import url
from basicapp import views

urlpatterns = [
    re_path(r'^$', views.index, name = 'index'),
    re_path(r'^index/$', views.index, name = 'index'),
    re_path(r'^form/$', views.form_view, name = 'form_view')
]
