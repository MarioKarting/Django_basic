from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import BookInfo,HeroInfo
from datetime import date
# Create your views here.
class DataView(View):
    def get(self,request):
        #1.图书对象
        # book = BookInfo()
        # book.btitle = "古董啦啦啦啦啦"
        # book.bpub_date = date(2007,1,1)
        # book.save()
        return HttpResponse("增加数据库操作哟")
#
# #1.增
#     #     save
# # book = BookInfo()
# # book.btitle = "古董啦啦啦啦啦"
# # book.bpub_date = date(2007,1,1)
# # book.save()
#
#     #     create
# BookInfo.objects.create(
#     btitle = "九层妖塔",
#     bpub_date = date(2018,8,8)
# )
# #2.删 delete
# # 取出来
# book = BookInfo.objects.get(id=5)
# book.delete()
# # 直接删除
# BookInfo.objects.filter(id=6).delete()
#
# #3.改
# # 取出来改 跟 取出来增加一样
# book =BookInfo.objects.get(id=6)
# book.btitle = "盗墓鼻孔鸡"
# book.save()
# # 直接改
# BookInfo.objects.filter(id=6).update(btitle ="精绝古城")
# #4.查
# BookInfo.objects.get(id = 3) #查询对象
#
# BookInfo.objects.filter(id=4)
# #类型不是列表,是QuerySet 查询集
#
# # all()  count()
# BookInfo.objects.all()
# BookInfo.objects.count()
#
#
#
#
# # 2.过滤出查询 filter()  exclude(取反不包含
# # 属性__符号 = 值
# # 等
# BookInfo.objects.filter(id = 2)
# BookInfo.objects.filter(id__exact = 3)
# BookInfo.objects.exclude(id__exact = 1)
#
# # 空
# BookInfo.objects.filter(bread__isnull= False)#0是默认值,不为空
# # 包含 contains startswith  endswith
# BookInfo.objects.filter(btitle__contains = "龙")
# BookInfo.objects.filter(btitle__endswith="塔")
# BookInfo.objects.filter(bpub_date__startswith = "198" )
#
# # 范围 in
# BookInfo.objects.filter(id__in=[1,3])
#
# # 条件 大于小于 B>= <=   gt gte lt lte
# BookInfo.objects.filter(bread__gte=50)
# BookInfo.objects.filter(bread__gt=20)
# BookInfo.objects.filter(bread__lt=30)
# BookInfo.objects.filter(id__lt=5,id__gt=1)
#
# # 日期 year month day week_day hour minute seconds
# BookInfo.objects.filter(bpub_date__day="08")
# # 月份大于八月份的
# BookInfo.objects.filter(bpub_date__month__gt="08")
#
#
# # F 和 Q 对象查询
# from django.db.models import F
# from django.db.models import Q
#
#
# # F查询阅读量大于等于评论量的图书。
# BookInfo.objects.filter(bread__lt = F('bcomment'))
#
# # Q查询阅读量大于20，或者编号小于3的图书。
#
# BookInfo.objects.filter(Q(bread__gt=20) | Q(id__lt = 3))
#
# # 聚合函数 Avg max min conunt sum
# from django.db.models import Sum,Avg,Count,Max,Min
#
# # 使用aggregate()过滤器调用聚合函数
# # 注意aggregate的返回值是一个字典类型，格式如下：
#   # {'属性名__聚合类小写':值}
#   # 如:{'bread__sum':3}
# BookInfo.objects.aggregate(Sum('bread'))
# BookInfo.objects.aggregate(Max('bread'))
#
# # 排序 对结果集进行 排序
# BookInfo.objects.order_by("bread")
# BookInfo.objects.order_by("-bread")
# BookInfo.objects.order_by("bcomment")
#
# # ※ 关联查询
# # 由一到多的访问语法：1:n 没有外键    对象.关联对象纯小写_set
# # 一对应的模型类对象.多对应的模型类名小写_set 例：
# b = BookInfo.objects.get(id=1)
# b.heroinfo_set.all()
# # 如果 在  hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书', related_name="heros")
# # 可以替换成 b.heros.all()
# # 书的ID为 2 的性别为男的英雄
# b = BookInfo.objects.get(id=2)
# b.heroinfo_set.filter(hgender="1")
# # 书的ID为 1 的性别为女的英雄
# c =BookInfo.objects.get(id=2)
# c.heroinfo_set.filter(hgender="0")
#
# # 由多到一的访问语法:
# #n:1有外键键 直接取外键属性
# # 如果表字段 设置了 related_name ="superman"
# # book.superman.all() 写了这个就不能写 _set
# # 多对应的模型类对象.多对应的模型类中的关系类属性名
# #
# h = HeroInfo.objects.get(id=3)
# #id为3的英雄所属的书
# h.hbook
# # id 为3的英雄所属的书的ID
# h.hbook_id
# # id 为3的英雄所属的技能
# h.hcomment
#
# # 关联过滤查询
# # 1:n
# # 一模型类关联属性名__一模型类属性名__条件运算符=值
# # 查询书名为“天龙八部”的所有英雄。
#
# HeroInfo.objects.filter(hbook__btitle="射雕英雄传")
#
# #查询图书阅读量大于30的所有英雄
# HeroInfo.objects.filter(hbook__bcomment__gte="30")
#
# # n:1
# # filter(关联模型类名小写__属性名__条件运算符=值)
# # 查询图书，要求图书英雄为"欧阳锋"
# BookInfo.objects.filter(heroinfo__hname="欧阳锋")
# # 查询图书，要求图书中英雄的描述包含"黄"
# BookInfo.objects.filter(heroinfo__hname__contains="王")
#
#
#
# #QuerySet 特点 : 查询集合
# # 懒惰执行 懒加载 数据用的时候才去交互数据库
#
#
# # 缓存
# # 先去缓存数据,缓存失效了,才交互数据库
# b =BookInfo.objects.filter(heroinfo__hname__contains="王")
# b.hbook
#
#
# #
