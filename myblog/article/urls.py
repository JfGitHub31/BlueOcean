__author__ = "jianfeng777"


from django.conf.urls import url
from . import views


urlpatterns = [
    # 发表文章
    url(r'^publish/$', views.article_publish, name='article_publish'),

    # 文章详情
    url(r'^(?P<article_id>\d+)/detail/$', views.article_detail, name='article_detail'),

    # 查看用户所有文章
    url(r'^(?P<author_id>\d+)/article_list/$', views.article_list, name='article_list'),

    # 编辑文章
    url(r'^(?P<article_id>\d+)/update/$', views.article_update, name='article_update'),

    # 删除文章
    url(r'^(?P<article_id>\d+)/delete/$', views.article_delete, name='article_delete')
]