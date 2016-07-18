from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='list'),
    url(r'^create/$', login_required(views.post_create), name='create'),
    # url(r'^(?P<id>\d+)/$', views.post_detail, name='detail'),
    # url(r'^(?P<id>\d+)/edit/$', views.post_update, name='update'),
    # url(r'^(?P<id>\d+)/delete/$', views.post_delete, name='delete'),

    url(r'^(?P<slug>[\w-]+)/$', views.post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', login_required(views.post_update), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', login_required(views.post_delete), name='delete'),
]