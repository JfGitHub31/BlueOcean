__author__ = "jianfeng777"


from django.conf.urls import url
from . import views


urlpatterns = [
    # 查看留言板
    url(r'^(?P<author_id>\d+)/$', views.message, name='message'),

    # 删除留言
    url(r'^(?P<msg_id>\d+)/delete/$', views.message_delete, name='message_delete')
]