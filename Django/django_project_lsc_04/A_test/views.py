# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.http.response import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
# Create your views here.
from django.views import View

class TestDjangoTemplates(View):
    def get(self,request):
        context_data = {
            'today_date': datetime.now(),
            'safe_data': "<a href='#'>欢迎来到炉石传说</a>",

            'data_list': ['Add', 'Bqq', 'Ctt', 'Dyy'],
            'data_dict': {
                "age": 5,
                "name": "德鲁伊",
                "gender": True
            },
            # "score": 99,
            "score":10,

        }

        return render(request, 'ssss.html', context=context_data)




