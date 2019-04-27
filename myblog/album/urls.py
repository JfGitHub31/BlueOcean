__author__ = "jianfeng777"


from django.conf.urls import url
from . import views


app_name = 'album'


urlpatterns = [
    # 查看个人相册路由
    #url(r'^(?P<author_id>\d+)/$', views.album_list, name='album_list'),

    # 查看相册详情路由
    url(r'^(?P<album_id>\d+)/$', views.album_detail, name='album_detail'),

    # 创建相册路由
    url('^album_create/$', views.album_create, name='album_create'),
]
