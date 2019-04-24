__author__ = "jianfeng777"


from django.conf.urls import url
from . import views


urlpatterns = [
    # 用户注册路由
    url(r'^register/$', views.author_register, name='author_register'),

    # 用户登录路由
    url(r'^login/$', views.author_login, name='author_login'),

    # 系统退出路由
    url(r'^logout/$', views.author_logout, name='author_logout'),

    # 用户个人首页路由
    url(r'^(?P<author_id>\d+)/$', views.author_index, name='author_index'),

    # 用户修改密码
    url(r'^password', views.author_password, name='author_password'),

]