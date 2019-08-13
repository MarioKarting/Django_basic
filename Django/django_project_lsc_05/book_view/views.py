from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from book_serializer.serializers import BookInfoSerializer


from rest_framework.response import Response

from C_databases.models import BookInfo


class BooksView(APIView):
    """
          获取所有图书
          保存图书
      """

    def get(self, request):
        # 1、查询所有图书
        books = BookInfo.objects.all()
        # 构建json数据 # 在类视图中调用序列化器类，初始化是传入需要序列化返回的数据对象
        ser = BookInfoSerializer(books, many=True)
        # 2、返回查询集数据
        return Response(ser.data)

    def post(self, request):#封装后的request
        # 1、获取前端数据
        # data = request.body.decode()
        # data_dict = json.loads(data)
        data=request.data
        # 2、验证数据
        # 序列化器初始化传入验证数据
        ser = BookInfoSerializer(data=data)
        # 序列化器提供的验证方法is_valid
        ser.is_valid(raise_exception=True)  # raise_exception参数作用：验证失败抛出异常
        # 3、保存
        ser.save()
        # 4、返回
        # 在类视图中调用序列化器类，初始化是传入需要序列化返回的数据对象
        # 构建序列化的json数据
        return Response(ser.data)

class BookView(APIView):

    def get(self,request,pk):
        # 1、查询一个图书
        book = BookInfo.objects.get(pk=pk)
        # 构建json数据 # 在类视图中调用序列化器类，初始化是传入需要序列化返回的数据对象
        ser = BookInfoSerializer(book)
        # 2、返回查询集数据
        return Response(ser.data)

    # 修改图书信息 路由： PUT  /books/<pk>
    def put(self, request, pk):
        data = request.data
        book = BookInfo.objects.get(pk=pk)
        ser = BookInfoSerializer(book,data=data)
        ser.is_valid(raise_exception=True)  # raise_exception参数作用：验证失败抛出异常
        ser.save()

        return Response(ser.data)

    def delete(self, request, pk):
        book = BookInfo.objects.get(pk=pk)
        # 逻辑删除
        book.is_delete = True
        book.save()
        # 物理删除
        # book.delete()
        # 3、返回结果
        return Response({})








