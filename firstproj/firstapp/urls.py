from django.conf.urls import url
from firstapp import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^sample/$', views.sample, name='sample'),
    url(r'^users/$', views.users, name='users'),
    url(r'^user2/$', views.user2, name='user2')
]
