from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
# Create your views here.
from C_databases.models import BookInfo
from book_serializer.serializers import BookInfoSerializer
from rest_framework.response import Response


class BooksView(GenericViewSet):
    """
          获取所有图书
          保存图书
      """
    # 指定视图使用的查询集
    queryset = BookInfo.objects.all()
    # 指定视图使用的序列化器
    serializer_class = BookInfoSerializer

    def list(self, request):
        # 1、查询所有图书
        # self.get_queryset() 获取查询集的所有数据
        books = self.get_queryset()
        # 构建json数据 # 在类视图中调用序列化器类，初始化是传入需要序列化返回的数据对象
        # ser = BookSerializer(books, many=True)
        # self.get_serializer  获取指定的序列化器进行初始化操作
        ser = self.get_serializer(books, many=True)
        # 2、返回查询集数据
        return Response(ser.data)

    def create(self, request):
        # 1、获取前端数据
        # data = request.body.decode()
        # data_dict = json.loads(data)
        data = request.data
        # 2、验证数据
        # 序列化器初始化传入验证数据
        # ser = BookSerializer(data=data)
        ser = self.get_serializer(data=data)
        # 序列化器提供的验证方法is_valid
        ser.is_valid(raise_exception=True)  # raise_exception参数作用：验证失败抛出异常
        # 3、保存
        ser.save()
        # 4、返回
        # 在类视图中调用序列化器类，初始化是传入需要序列化返回的数据对象
        # 构建序列化的json数据
        return Response(ser.data)


class BookView(GenericViewSet):
    """
        获取单一图书
        更新
        删除
    """
    # 指定视图使用的查询集
    queryset = BookInfo.objects.all()
    # 指定视图使用的序列化器
    serializer_class = BookInfoSerializer

    def retrieve(self, request, pk):
        # 1、根据图书id查询当前图书对象
        # try:
        #     book = BookInfo.objects.get(id=pk)
        # except:
        #     return JsonResponse({'error': '查询的图书不存在'})
        # get_object()从查询集中获取符合pk所对应的id的数据对象
        book = self.get_object()
        # 2、返回结果
        # 在类视图中调用序列化器类，初始化是传入需要序列化返回的数据对象
        ser = self.get_serializer(book)
        # 构建序列化的json数据
        return Response(ser.data)

    def update(self, request, pk):
        # 1、获取前端数据
        data = request.data
        # 2、验证数据
        book = self.get_object()
        ser = self.get_serializer(book,data=data)
        ser.is_valid(raise_exception=True)
        # 3、更新数据
        ser.save()
        # 4、返回更新后的数据构建序列化的json数据
        return Response(ser.data)

    def destroy(self, request, pk):
        # 1、根据图书id查询当前图书对象
        book = self.get_object()
        # 2、逻辑删除
        book.is_delete = True
        book.save()
        # 物理删除
        # book.delete()

        # 3、返回结果
        return Response({})
