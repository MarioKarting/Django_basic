from rest_framework import serializers

from C_databases.models import BookInfo


class Book1InfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    image = serializers.ImageField(label='图片', required=False)


class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)

    hbook = Book1InfoSerializer()

#单一字段验证的另一种方法
#def bitile_func()
# btitle = serializers.CharField(validators = 'bitile_func')

class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)#read_only 指定该字段参加序列化返回过程,不进行验证操作
    btitle = serializers.CharField(label='名称',min_length=3, max_length=20)#write_only 指定该字段只参加反序列化的验证保存更新过程,结果返回没有该字段
    bpub_date = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False,max_value=200,min_value=1)
    # image = serializers.ImageField(label='图片', required=False)

    #password=serializers.CharField(write_only = True)
    # heros = HeroInfoSerializer(many = True) 找不到该字段

    #嵌套序列化返回 用关联查询的字段作为序列化器的字段
    #根据所指定的序列化器字段返回内容
    # heroinfo_set = HeroInfoSerializer(many = True)

    #返回关联数据的id值
    # heroinfo_set = serializers.PrimaryKeyRelatedField(many = True,read_only=True)

    # 返回关联数据表中的 __str__方法所返回的值
    #def __str__
    # heroinfo_set = serializers.StringRelatedField(many = True,read_only=True)

    #定义单一字段验证方法 固定的方法名 接收参数命名不固定 is_valid 自动调用
    def validate_btitle(self, value):
        '''
        图书书名的验证
        :param value: 接收验证的图书书名
        :return:
        '''
        if value =='python':
            raise serializers.ValidationError('书名不能是python')
        #验证后必须将验证的结果返回 不返回 到下次验证的时候btitle 是空值
        return value


    # 定义多个字段验证方法 固定的方法名 接收参数命名不固定 is_valid 自动调用
    #序列化初始化验证传入的字典数据
    #应用于两个密码的验证
    def validate(self, attrs):
        '''
            完成多个字段验证
        :param attrs: 接收的是需要验证的字典数据
        :return:
        '''
        if attrs['bread']>attrs['bcomment']:
            raise serializers.ValidationError("阅读量大于评论量")
        # 验证后必须将验证的结果返回
        return attrs

    #定义保存方法,完成保存业务逻辑,固定方法名
    def create(self, validated_data):
        '''
            保存图书
        :param validated_data: 接收验证后的图书数据
        :return:
        '''
        book = BookInfo.objects.create(**validated_data)
        return book

    #定义更新方法,完成保存业务逻辑固定方法名
    def update(self, instance, validated_data):
        '''
            更新图书
        :param instance: 接收更新的数据对象
        :param validated_data: 接收验证后的图书数据
        :return:
        '''
        instance.btitle = validated_data.get("btitle")
        instance.save()
        return instance


class BookInfoModelSerializer(serializers.ModelSerializer):
    #ModelSerializer和Serializer区别
    #1.可以根据指定的模型类自动生成序列化器字段
    #2.帮助实现create方法和update方法
    #3.如果模型类的字段有唯一值限定,会自动生成唯一值判断方法

    #显示指明最高级的,直接就可以修改字段选项
    #显示指明字段  本身模型类没有该字段
    sms_code  = serializers.CharField(max_length=6,min_length=6,write_only=True)

    #1.自动生成的选项有误就按照自己定义的显示指明
    bread =serializers.IntegerField(max_value=20,min_value=1)

    class Meta:#固定用法
        model = BookInfo
        #指定模型类中那些字段生成序列化器字段  元祖的形式
        fields = ("id","btitle","bread","sms_code")

        #全部字段
        # fields = "__all__"

        #必须没有显示指明的字段 给字段增加read_only=True的选项
        read_only_field = ('bread',)

        # exclude 根据指定字段取反生成其他字段
        # exclude=("id",) #除它之外的 元祖只有一个数据需要加括号
        #fields和exclude 二者用其中一个

        #2.自动生成的选项有误 修改自动生成选项的形式
        extra_kwargs={
            'bcomment':{
                "max_value":30,
                "min_value": 1
            },
            #增加一个最小长度的限制
            'btitle':{
                'min_length':5
            }

        }


        #不用写保存和更新方法
        #需要自己写验证方法
        def validate(self, attrs):
            pass