from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import json
# Create your views here.
from django.views import View

from C_databases.models import HeroInfo


class HerosView(View):
    #1.获取所有英雄
    def get(self,request):
        #取出英雄对象的查询集
        heros = HeroInfo.objects.all()
        #空列表保存英雄信息
        hero_list = []
        for hero in heros:
            # herobook = hero.hbook
            # herobook_dict = json.loads(herobook)
            print(hero.hbook)
            print(type(hero.hbook))
            hero_list.append({"id":hero.id,"name":hero.hname,
                              "gender":hero.hgender,"gongfu":hero.hcomment,
                              "book":hero.hbook_id})
        # 2、返回查询集数据
        return JsonResponse(hero_list, safe=False)

    #2.保存英雄
    def post(self,request):
        #request.body 是二进制流,需要通过 decode 转换成str
        data = request.body.decode()
        #将str转换成dict
        data_dict =json.loads(data)

        # 4、返回
        #拆包保存   {"name" = "python"} ===>   name = python
        hero = HeroInfo.objects.create(**data_dict)
        return JsonResponse(
            {'id': hero.id,
             'hname': hero.hname,
             'hgender': hero.hgender,
             'hcomment': hero.hcomment,
             'hbook_id': hero.hbook_id
             }
        )






class HeroView(View):
    #2.查询单个英雄 路由GET /heros/<pk>/
    def get(self,requset,pk):
        try:
            hero = HeroInfo.objects.get(pk=pk)
        except HeroInfo.DoesNotExist:
            return HttpResponse(status=404)

        return JsonResponse(
            {'id': hero.id,
             'hname': hero.hname,
             'hgender': hero.hgender,
             'hcomment': hero.hcomment,
             'hbook_id': hero.hbook_id
             }
            )

    #3.修改英雄数据 路由GET /heros/<pk>/
    def put(self,request,pk):
        try:
            hero = HeroInfo.objects.get(pk=pk)#创建英雄对象
        except HeroInfo.DoesNotExist:
            return HttpResponse(status=404)
        # 前段接受到的数据是二进制流
        json_bytes = request.body
        # 通过decode 转换成字符串
        json_str = json_bytes.decode()
        # 通过loads转换成json字典
        hero_dict = json.loads(json_str)
        hero.hname =  hero_dict.get("hname")
        hero.hcomment = hero_dict.get("hcomment")
        hero.save()

        return JsonResponse(
            {
             'id': hero.id,
             'hname': hero.hname,
             'hgender': hero.hgender,
             'hcomment': hero.hcomment,
             'hbook_id': hero.hbook_id
             }
        )


    #4.删除英雄
    def delete(self,request,pk):
        try:
            hero = HeroInfo.objects.get(pk=pk)
        except HeroInfo.DoesNotExist:
            return HttpResponse(status=404)
        hero.delete()
        #204 NO CONTENT - [DELETE]：用户删除数据成功。
        return HttpResponse(status=204)