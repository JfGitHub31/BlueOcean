from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from author.models import Author
from . import models


def say_list(request, author_id):
    """
    查看用户说说
    :param request:
    :param author_id:
    :return:
    """
    author = Author.objects.get(pk=author_id)
    if request.method == "GET":
        # 查看说说
        say_list = models.AuthorSay.objects.filter(author=author).order_by('-say_time')
        return render(request, 'authorsay/say_list.html', {'say_list': say_list, 'author': author})

    elif request.method == "POST":
        # 发表说说
        content = request.POST.get('say_content')
        # 创建说说对象并保存
        say = models.AuthorSay(content=content, author=author)
        say.save()

        # 跳转查看说说
        return redirect(reverse('say_list', kwargs={'author_id': author.id}))


def say_delete(request, say_id):
    """
    删除说说
    :param request:
    :param say_id:
    :return:
    """
    # 查询说说并删除
    say = models.AuthorSay.objects.get(pk=say_id)
    author = say.author
    say.delete()

    # 跳转到说说列表页面
    return redirect(reverse('say_list', kwargs={'author_id': author.id}))