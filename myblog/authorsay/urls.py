__author__ = "jianfeng777"


from django.conf.urls import url
from . import views


urlpatterns = [
    # 查看用户发表说说
    url(r'^(?P<author_id>\d+)/$', views.say_list, name='say_list'),

    # 删除用户说说
    url(r'^(?P<say_id>\d+)/delete/$', views.say_delete, name='say_delete')
]