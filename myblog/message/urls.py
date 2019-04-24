__author__ = "jianfeng777"


from django.conf.urls import url
from . import views


urlpatterns = [
    # 查看留言板
    url(r'^(?P<author_id>\d+)/$', views.message, name='message'),
]