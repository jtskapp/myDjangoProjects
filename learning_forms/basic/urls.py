from django.urls import path, include, re_path
from basic import views

urlpatterns = [
    re_path(r'^$', views.orderform1, name='orderform1'),
    re_path(r'^orderform1/$', views.orderform1, name='orderform1'),
    re_path(r'^orderform2/$', views.orderform2, name='orderform2'),
    re_path(r'^userlogin/$', views.user_login, name='user_login'),
    re_path(r'^userinfo/$', views.userinfo, name='userinfo'),
    re_path(r'^updateprofile/$', views.update_profile, name='updateprofile'),
    re_path(r'^testajax/$', views.orderinfo, name='orderinfo'),
    re_path(r'^ajax/getorders/$', views.get_orders, name='get_orders'),
]
