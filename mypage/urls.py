from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^consumer/', views.consumer),
    url(r'^merchants_area/', views.merchants_area),
    url(r'^vendors_area/', views.vendors_area),
    url(r'^board/', views.board),
]
