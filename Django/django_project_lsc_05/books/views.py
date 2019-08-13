from datetime import datetime
from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
import json


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
        book_list = []
        for book in books:
            book_list.append({'id': book.id, 'btitle': book.btitle, 'bread': book.bread, 'bpub_date': book.bpub_date,
                              'bcomment': book.bcomment})
        # 2、返回查询集数据
        return JsonResponse(book_list, safe=False)

    #3、保存图书
    def post(self, request):
        # 1、获取前端数据
        data = request.body.decode()
        data_dict = json.loads(data)
        # 2、验证数据
        btitle = data_dict.get('btitle')
        if len(btitle) < 3:
            return JsonResponse({"error": "书名长度不符合需求"}, status=400)
        # 3、保存
        book = BookInfo.objects.create(**data_dict)
        # 4、返回
        return JsonResponse(
            {'id': book.id,
             'btitle': book.btitle,
             'bread': book.bread,
             'bpub_date': book.bpub_date,
             'bcomment': book.bcomment
             }
        )

0
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

        return JsonResponse({
            "id":book.id,
            "btitle":book.btitle,
            "bpub_date":book.bpub_date,
            "bread":book.bread,
            "bcomment":book.bcomment,
            "image":book.image.url if book.image else " "
        })

    # 修改图书信息 路由： PUT  /books/<pk>
    def put(self, request, pk):
        try:
            book =BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)
        #前段接受到的数据是二进制流
        json_bytes = request.body
        #通过decode 转换成字符串
        json_str = json_bytes.decode()
        #通过loads转换成json字典
        book_dict = json.loads(json_str)
        # 2、验证数据
        btitle = book_dict.get('btitle')
        if len(btitle) < 3:
            return JsonResponse({"error": "书名长度不符合需求"}, status=400)
        book.bpub_date = datetime.strptime(book_dict.get('bpub_date'), '%Y-%m-%d').date()
        book.save()
        #方法二
        # book = BookInfo.objects.filter(id=pk).update(**data_dict)
        #返回的结果不是对象,而是更新了几条数据
        #需要把更新的对象再查询出来返回
        return JsonResponse({
            'id': book.id,
            'btitle': btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.image else ''
        })


    #删除图书 路由： DELETE /books/<pk>/

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
