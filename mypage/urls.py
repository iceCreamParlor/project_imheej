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
    url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^diary_detail/(?P<pk>[0-9]+)/diarycomment/$', views.add_comment_to_diary, name='add_comment_to_diary'),
    url(r'^diary_detail/(?P<pk>[0-9]+)/diarycomment/mypage.views.diary_detail$', views.diary_detail),
    url(r'^post/(?P<pk>[0-9]+)/comment/mypage.views.post_detail$', views.post_detail),
]
