from django.conf.urls import url
from django.contrib import admin
from . import views, views_genericapiview, views_modelmixin,  views_genericviewset,view_viewset,view_modelchildmixin,views_modelviewset


from rest_framework.routers import SimpleRouter,DefaultRouter

urlpatterns=[
 #    #APIView
 #    url(r'^books_view_api/$',views.BooksView.as_view()),
 #    url(r'^books_view__api/(?P<pk>\d+)/$', views.BookView.as_view()),
 #    #genericapiview
 #    url(r'^books_view_gapi/$', views_genericapiview.BooksView.as_view()),
 #    url(r'^books_view__gapi/(?P<pk>\d+)/$', views_genericapiview.BookView.as_view()),
 #    #五个扩展类
 #    url(r'^books_view_mixin/$', views_modelmixin.BookView.as_view()),
 #    url(r'^books_view_mixin/(?P<pk>\d+)/$', views_modelmixin.BookView.as_view()),
 #    #扩展子类
 #    url(r'^books_view_mixinchlid/$', view_modelchildmixin.BookView.as_view()),
 #    url(r'^books_view_mixinchlid/(?P<pk>\d+)/$', view_modelchildmixin.BookView.as_view()),
 #    #Viewset
 #    url(r'^books_viewset/$', view_viewset.BooksView.as_view({'get':'list','post':'create'})),
 #    url(r'^books_viewset/(?P<pk>\d+)/$', view_viewset.BookView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
 #    #generciviewset
 #    url(r'^books_genericviewset/$', views_genericviewset.BooksView.as_view({'get':'list','post':'create'})),
 #    url(r'^books_genericviewset/(?P<pk>\d+)/$', views_genericviewset.BookView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
 #    #modelViewset 调用同一个类视图 都是BookModleViewSet
 #    url(r'^books_modelViewset/$', views_modelviewset.BookModleViewSet.as_view({'get': 'list', 'post': 'create'})),
 #    url(r'^books_modelViewset/(?P<pk>\d+)/$',views_modelviewset.BookModleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
 # # # 视图集中额外定义的方法，在匹配规则中将方法名最为路径
 #    url(r'^books_modelViewset/last/$', views_modelviewset.BookModleViewSet.as_view({'get':'last'})),
 #    url(r'^books_modelViewset/hero/$', views_modelviewset.BookModleViewSet.as_view({'get':'hero'})),
]

# 初始化生成路由对象
router = DefaultRouter()
# register 路由注册
router.register('books_view', views_modelviewset.BookModleViewSet, base_name='books_view')
# urls 获取生成后的路由列表
print(router.urls)

urlpatterns += router.urls