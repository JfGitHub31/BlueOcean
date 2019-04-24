from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from . import models
from author.models import Author


def article_publish(request):
    """
    发表文章视图处理函数
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'article/article_publish.html', {})

    elif request.method == "POST":
        # 获取用户发表文章的数据
        title = request.POST.get('title')
        content = request.POST.get('content')

        author = request.session['login_user']

        # 创建文章对象并发表文章, 保存文章到数据库
        article = models.Article(title=title, content=content, author=author)
        print('--__>',article.title)
        article.save()

        # 返回详情页面查看文章
        return redirect(reverse('article_detail', kwargs={'article_id': article.id}))


def article_detail(request, article_id):
    """
    文章详情信息
    :param request:
    :return:
    """
    # 查询文章
    article = models.Article.objects.get(pk=article_id)
    article.read_count += 1

    article.save()
    return render(request, 'article/article_detail.html', {'article': article})


def article_list(request, author_id):
    """
    查看指定编号的用户的所有文章
    :param request:
    :param author_id:
    :return:
    """
    # 查询到用户
    author = Author.objects.get(pk=author_id)
    article_list = models.Article.objects.filter(author=author).order_by('-publish_time')
    return render(request, 'article/article_list.html', {'author': author, 'article_list': article_list})


def article_update(request, article_id):
    """
    修改文章
    :param request:
    :param article_id:
    :return:
    """
    article = models.Article.objects.get(pk=article_id)
    if request.method == "GET":
        return render(request, 'article/article_update.html', {'article': article})
    elif request.method == "POST":
        # 获取数据,修改文章
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 修改文章数据
        article.title = title
        article.content = content

        article.save()

        # 跳转到文章详情页面 TODO
        return redirect(reverse('article_detail', kwargs={'article_id': article.id}))


def article_delete(request, article_id):
    """
    删除文章
    :param request:
    :param article_id:
    :return:
    """
    # 查询文章
    article = models.Article.objects.get(pk=article_id)
    author = article.author
    article.delete()

    # 跳转到文章列表页面
    return redirect(reverse('article_list', kwargs={'author_id': author.id}))


