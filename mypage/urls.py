from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^diary/', views.diary),
    url(r'^profile/', views.profile),
    url(r'^diary_detail/(?P<pk>\d+)/$', views.diary_detail, name='diary_detail'),
    url(r'^board/', views.board),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
