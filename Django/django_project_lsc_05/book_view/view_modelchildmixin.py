from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
# Create your views here.
from C_databases.models import BookInfo
from book_serializer.serializers import BookInfoSerializer
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class BooksView(ListCreateAPIView):
    """
          获取所有图书
          保存图书
      """
    # 指定视图使用的查询集
    queryset = BookInfo.objects.all()
    # 指定视图使用的序列化器
    serializer_class = BookInfoSerializer



class BookView(RetrieveUpdateDestroyAPIView):
    """
        获取单一图书
        更新
        删除
    """
    # 指定视图使用的查询集
    queryset = BookInfo.objects.all()
    # 指定视图使用的序列化器
    serializer_class = BookInfoSerializer
