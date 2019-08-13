from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BookInfo,HeroInfo
# admin.site.register(BookInfo)
# admin.site.register(HeroInfo)


# 表格形式
class HeroTabularInline(admin.TabularInline):
    #     关联对象
    model = HeroInfo#继承关系

    #    设置显示个数
    extra = 1


# 块形势
class HeroStackedInline(admin.StackedInline):
    #     关联对象
    model = HeroInfo

    #    设置显示个数
    extra = 1
#自定义站点 admin

class BookInfoAdmin(admin.ModelAdmin):
    # 1. 显示哪些字段 list_dispaly
    list_display = ['id', 'btitle', 'bread', 'my_date']
    # 2. 每页显示的个数 list_per_page=
    list_per_page = 4
    # 3. 操作选项的位置 actions_on_top
    actions_on_top = True
    # actions_on_bottom = True
    # 4. 右侧过滤器 list_filter
    # list_filter = []
    # 5. 搜索框 search_fields
    search_fields = ['btitle']

    # # 6. 自定义列的名字  方法列 model.py—admin.py display = [‘read’]
    # # 7. 关联对象
    #
    # # 编辑页面
    # # 1.显示字段
    # fields = ['btitle','bpub_date']
    # # 2. 分组显示
    fieldsets = (
        ("必传", {'fields': ['btitle', 'bpub_date','image']}),
        ('选填', {
            'fields': ['bread', 'bcomment'],
            'classes': ('collapse',)
        }),
    )

    # # 3. 关联对象 块 和表
    # inlines = [HeroTabularInline]#书里面嵌英雄 表样式
    inlines = [HeroStackedInline] #快样式


# 注册模型类
admin.site.register(BookInfo, BookInfoAdmin)
#继承

# 装饰器
@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    list_filter = ['hgender']
    list_display = ['hname', 'hbook', 'read']


#设置标题
admin.site.site_header = '传智书城'
admin.site.site_title = '传智书城MIS'
admin.site.index_title = '欢迎使用传智书城MIS'