from django.db import models


# 自定义管理器 ORM models.Manager -自定义之后系统的objests失效了
# class BookInfoManage(models.Manager):
# # 1.改 系统功能
#     def all(self):
#         return  super().filter(is_deldete=False)
# #     2.新增自己的功能
'''
      def create_book(self,title,pub_data):
          book = self.model()
          book.btitle = title
          book.bpub_data = pub_data
          book.bread =0
          book.bcomment = 10
          book.save()

          return book
'''



# Create your models here.
# 定义图书模型类BookInfo
class BookInfo(models.Model):
    # books = BookInfoManage()  自定义的得重启
    btitle = models.CharField(max_length=20, verbose_name='名称')#没有默认值,不能为空,必须写
    bpub_date = models.DateField(verbose_name='发布日期')#没有默认值,不能为空,必须写
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    # 新增  图片字段 upload_to 上传的位置 可写可不写
    # null = True 必须写
    image = models.ImageField(upload_to='adata', null=True, verbose_name="图片")

    class Meta:
        db_table = 'tb_books'  # 指明数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称 图书s

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.btitle

    # def custom_data(self):
    #     return "自定义"

    def my_date(self):
        return self.bpub_date.strftime("%Y-%m-%d")

    my_date.short_description = "我的日期"
    my_date.admin_order_field = "bpub_date" #排序只能根据原始数据排序 my_data是自己定义的
#定义英雄模型类HeroInfo

class HeroInfo(models.Model):
    # 枚举类型
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )
    hname = models.CharField(max_length=20, verbose_name='名称')
    # 短整型
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    # 关联外键              英雄关联书的类            级联操作,一删全删
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_heros'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname

    def read(self):#书没有阅读量,自己自定义一个
        return self.hbook.bread
    read.short_description = "书阅读量"#显示中文