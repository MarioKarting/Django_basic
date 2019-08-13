from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from C_databases.models import BookInfo,HeroInfo
from book_serializer.serializers import BookInfoSerializer, HeroInfoSerializer
from rest_framework.filters import OrderingFilter
from django.db import DatabaseError


class PageNUm(PageNumberPagination):
    """
        自定义分页器
    """

    page_query_param = 'page'#表示你要请求第几页的数据
    page_size_query_param = 'page_size'  #指定控制每页数量的参数
    max_page_size = 8 # 指定每页最大返回数据


class BookModleViewSet(ModelViewSet):
    # 指定视图使用的查询集
    queryset = BookInfo.objects.all()
    # 指定视图使用的序列化器 重写get_serializer_class后,就不用了
    # serializer_class = BookInfoSerializer

    #局部控制只针对当前类视图有效
    # 认证
    authentication_classes = [BasicAuthentication, SessionAuthentication]

    # 权限
    permission_classes = [IsAuthenticated]

    # 限流
    # throttle_classes = [UserRateThrottle] #认证用户限流
    #类视图命名
    throttle_scope = 'a'
    filter_fields = ('btitle', 'bread')
    filter_backends = [OrderingFilter]
    ordering_fields = ('id', 'bread', 'bpub_date')
    # 指定分页器
    pagination_class = PageNUm




    #当调用get_serializer()会调用到get_serailizer_class()
    def get_serializer_class(self):
        #原生方法默认返回self.serializer_class
        # return self.serializer_class#返回指定的序列化器
        if self.action =="hero":
            return HeroInfoSerializer
        else:
            return BookInfoSerializer

    #获取最后一个图书返回
    @action(methods=['get'],detail=False)
    def last(self,request):
        # raise DatabaseError
        book = BookInfo.objects.latest("id")
        ser=self.get_serializer(book)
        return Response(ser.data)

    #获取所有英雄信息
    @action(methods=['get'],detail=False)
    def hero(self,request):
        hero =HeroInfo.objects.all()
        ser = self.get_serializer(hero,many=True)
        return Response(ser.data)