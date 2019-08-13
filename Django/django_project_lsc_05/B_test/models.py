# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from django.db import models
#
# # Create your models here.
# from django.db import models
# #
#
# #属性=models.字段类型(选项)
# #子应用必须注册,不然会翻译不成功
# #2.连接翻译  同步到数据库中 python manage.py migrate
# #1.数据迁移 python manage.py makemigrations
# #  建表建字段 -orm ---类和属性
# class Stu(models.Model):
#     #字段  就是 类的属性    自动生成主键 自动增长
#     # id =models.IntegerField(primary_key=True)
#     name =models.CharField(max_length=20)
#     age = models.IntegerField()
#     gender = models.BooleanField(default=False)
#     school = models.CharField(max_length=64)
#     hight = models.DecimalField(max_digits=5,decimal_places=2)
#
#     class Meta:
#         db_table = "tb_stu"
#
# #没有修改表名字 默认 自应用名字小写_类小写
# #以后命名数据尽量加Z,这样自己的数据库存就会在最下面
# class Score(models.Model) :
#     score = models.DecimalField(max_digits=3,decimal_places=1)
