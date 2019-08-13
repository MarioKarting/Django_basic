from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
# Create your views here.
from C_databases.models import BookInfo
from book_serializer.serializers import BookInfoSerializer
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

class BooksView(GenericAPIView,ListModelMixin,CreateModelMixin):
    """
          获取所有图书
          保存图书
      """
    # 指定视图使用的查询集
    queryset = BookInfo.objects.all()
    # 指定视图使用的序列化器
    serializer_class = BookInfoSerializer

    def get(self, request):
      return self.list(request)

    def post(self, request):
       return self.create(request)


class BookView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    """
        获取单一图书
        更新
        删除
    """
    # 指定视图使用的查询集
    queryset = BookInfo.objects.all()
    # 指定视图使用的序列化器
    serializer_class = BookInfoSerializer

    def get(self, request, pk):
        return self.retrieve(request,pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)