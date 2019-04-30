__author__ = "jainfeng777"


from django.conf.urls import url
from . import views


urlpatterns = [
    # 查看照片详情
    url(r'^(?P<photo_id>\d+)/photo_detail/$', views.photo_detail, name='photo_detail'),

    # 上传照片
    url(r'^(?P<album_id>\d+)/photo_upload/$', views.photo_upload, name='photo_upload'),

    # 查看相册中所有照片
    url(r'^(?P<album_id>\d+)/$', views.photo_list, name='photo_list'),
]