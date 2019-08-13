# 框架源代码序列化器
class BaseSerializer(object):
    #初始化调用__init__方法
    def __init__(self, instance=None, data=None):
        """

        :param instance: 接受对象
        :param data: 接受验证数据
        """
        self.instance = instance#实例属性 or 对像属性
        self.valid_data = data#验证之前的数据

    def is_valid(self):
        """
            父类验证方法
        :return:
        """
        #在本身类中定义了验证方法
        #在父类中调用最下面定义的验方法,并将结果返回
        self.validated_data = self.validate(self.valid_data)#调用验证方法

        return self.validated_data#验证后的数据

    @property#这个方法使用过程中是一个属性
    def data(self):
        """
            构造序列化结果
        :return:
        """
        return self.instance#对对象进行返回

    def save(self):
        """
            保存或更新
        :return:
        """
        #不为空,说明在初始化的时候接收到了一个对象
        if self.instance is not None:
            #调用子类重写的更新方法
            self.instance = self.update(self.instance, self.validated_data)
        else:#如果是空值,就是保存,调用子类重写的create方法
            self.instance = self.create(self.validated_data)

    def validate(self, attrs):
        # pass 目的是为了子类重写
        pass

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
