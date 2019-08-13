from serialzier import BookSerialzier


class BookView(object):
    #定义一个保存方法
    def post(self, data):
        # 1、获取数据 前端传递的数据
        data = data

        #调用类,而不是直接继承 调用序列化器
        #这个序列化器本身继承的是BaseSerializer ,BaseSerializer有个初始化方法,需要传参数,关键字参数
        #在一个类中调用另一个类,调用的是该类中的初始化方法__init__,子类没有,去父类
        ser = BookSerialzier(data=data)
        # 2、验证数据
        ser.is_valid()#父类BaseSerializer定义的方法
        # 3、保存数据
        ser.save()#父类BaseSerializer定义的方法
        # 4、返会结果
        return ser.data


data = {'name': 'python'}
BookView().post(data)
