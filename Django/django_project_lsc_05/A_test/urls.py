from django.conf.urls import url, include
from django.contrib import admin
from django.http.response import HttpResponse, HttpResponseForbidden
from . import views


urlpatterns = [

    url(r'^atest/$', views.TestDjangoTemplates.as_view()),

]
