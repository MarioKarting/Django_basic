from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^book/$', views.BookView.as_view()),
    url(r'^hero/$', views.HeroView.as_view()),
]
