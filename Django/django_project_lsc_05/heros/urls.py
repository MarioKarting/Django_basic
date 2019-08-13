from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns=[
    url(r'^heros/$',views.HerosView.as_view()),

    url(r'^heros/(?P<pk>\d+)/$', views.HeroView.as_view()),


]