from datetime import datetime
from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
import json
from book_serializer.serializers import BookInfoSerializer

# Create your views here.
from C_databases.models import BookInfo


class BooksView(View):
    """
        获取所有图书
        保存图书
    """
    #1、获取所有图书数据
    def get(self, request):
        # 1、查询所有图书
        books = BookInfo.objects.all()
        # 构建json数据
        ser = BookInfoSerializer(books,many=True)
        # 2、返回查询集数据
        return JsonResponse(ser.data, safe=False)

    #3、保存图书
    def post(self, request):
        # 1、获取前端数据
        data = request.body.decode()
        data_dict = json.loads(data)
        # 2、验证数据
        # btitle = data_dict.get('btitle')
        # if len(btitle) < 3:
        #     return JsonResponse({"error": "书名长度不符合需求"}, status=400)
        # 序列化器初始化传入验证数据
        ser = BookInfoSerializer(data=data_dict)
        # 序列化器提供的验证方法is_valid
        ser.is_valid(raise_exception=True)  # raise_exception参数作用：验证失败抛出异常
        # ser.errors获取验证后的信息
        # print(ser.errors)
        # if ser.errors is not None:
        #     return JsonResponse({'error':ser.errors})


        # 获取验证后的数据
        book_data = ser.validated_data

        # 3、保存
        # {'name':'python'}  name=python
        # book = BookInfo.objects.create(**book_data)
        ser.save()
        # 4、返回
        # 在类视图中调用序列化器类，初始化是传入需要序列化返回的数据对象

        # 构建序列化的json数据
        return JsonResponse(ser.data)


class BookView(View):
    """
        获取单一图书
        更新
        删除
    """
    #获取单一图书 路由GET /books/<pk>/
    def get(self, request, pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)
        #2.返回结果
        #生成序列化对象 在类视图中调用序列化器类,初始化是传入需要序列化返回的数据对象
        ser = BookInfoSerializer(book)
        ser.is_valid(raise_exception=True)
        #通过data 方法 构建序列化的json数据
        # ser.data
        return  JsonResponse(ser.data)

    # 修改图书信息 路由： PUT  /books/<pk>
    def put(self, request, pk):

        data = request.body.decode()
        data_dict = json.loads(data)
        try:
            book =BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)
        # 序列化器初始化传入验证数据 多一个参数book
        ser = BookInfoSerializer(book,data=data_dict)
        # 序列化器提供的验证方法is_valid
        ser.is_valid(raise_exception=True)  # raise_exception参数作用：验证失败抛出异常
        # 获取验证后的数据
        # book_data = ser.validated_data
        # 3、保存
        # {'name':'python'}  name=python
        ser.save() #save不同的原因 是因为传递的参数不同
        # 4、返回
        # 在类视图中调用序列化器类，初始化是传入需要序列化返回的数据对象

        # 构建序列化的json数据
        return JsonResponse(ser.data)


    # 删除图书 路由： DELETE /books/<pk>/

    def delete(self, request, pk):
        #根据图书id查询当前图书对象
        try:
            book =BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        #逻辑删除
        book.is_delete=True
        book.save()
        # 物理删除
        # book.delete()
        return HttpResponse(status=204)
