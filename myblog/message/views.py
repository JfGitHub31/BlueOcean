from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from author.models import Author
from . import models


def message(request, author_id):
    """
    留言视图处理函数
    :param request:
    :param author_id:
    :return:
    """
    author = Author.objects.get(pk=author_id)
    if request.method == "GET":
        msg_list = models.Message.objects.filter(receive_author=author).order_by('-msg_time')
        return render(request, 'message/message.html', {'author': author, 'msg_list': msg_list})

    elif request.method == "POST":
        # 获取数据
        msg = request.POST.get('msg')
        # 获取当前登录用户
        send_author = request.session['login_user']

        # 创建留言板对象
        msg = models.Message(content=msg, send_author=send_author, receive_author=author)
        msg.save()

        # 跳转到查看留言板的路由
        return redirect(reverse('message', kwargs={'author_id': author.id}))


def message_delete(request, msg_id):
    """
    留言删除视图处理函数
    :param request:
    :param msg_id:
    :return:
    """
    pass






