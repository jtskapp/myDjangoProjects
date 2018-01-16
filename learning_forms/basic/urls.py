from django.urls import path, include, re_path
from basic import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^orderform/$', views.orderform, name='orderform'),
    re_path(r'^userlogin/$', views.user_login, name='user_login'),
    re_path(r'^userinfo/$', views.userinfo, name='userinfo'),
    re_path(r'^updateprofile/$', views.update_profile, name='updateprofile'),
]
