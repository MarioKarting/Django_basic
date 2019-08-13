from baseserializer import BaseSerializer



# 自定义序列化器
class BookSerialzier(BaseSerializer):

    #多个字段验证的方法
    #重写父类的验证方法
    def validate(self, value):

        print('自己封装的验证方法validate')
        return value#返回到父类序列化器中,因为被该序列化器调用的

    # 重写父类的保存方法
    def create(self, validated_data):
        return 'create'

    # 重写父类的更新方法
    def update(self, instance, validated_data):


        return 'update'