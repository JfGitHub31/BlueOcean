from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from . import models
from author.models import Author


def album_create(request):
    """
    创建相册
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'album/album_create.html', {})

    elif request.method == "POST":
        # 获取数据
        name = request.POST.get('name')
        cover = request.FILES.get('cover')
        remark = request.POST.get('remark')
        if name is "" or cover is None:
            return render(request, 'album/album_create.html', {'msg': "相册名称或封面不能为空"})

        author = request.session['login_user']

        # 创建并保存相册
        album = models.Album(name=name, cover=cover, remark=remark, author=author)
        album.save()

        # 跳转相册详情页面
        return redirect(reverse('album:album_detail', kwargs={'album_id': album.id}))


def album_detail(request, album_id):
    """
    查看制定编号相册
    :param request:
    :param album_id:
    :return:
    """
    album = models.Album.objects.get(pk=album_id)
    return render(request, 'album/album_detail.html', {'album': album})


def album_list(requset, author_id):
    """
    查看指定用户相册信息
    :param requset:
    :param author_id:
    :return:
    """
    author = Author.objects.get(pk=author_id)
    album_list = models.Album.objects.filter(author=author).order_by('-create_time')
    return render(requset, 'album/album_list.html', {'author': author, 'album_list': album_list})


def album_delete(request, album_id):
    """
    删除相册
    :param request:
    :param album_id:
    :return:
    """
    album = models.Album.objects.get(pk=album_id)
    author = album.author
    print('author_id---->', author.id)
    album.delete()

    return redirect(reverse('album:album_list', kwargs={'author_id': author.id}))


