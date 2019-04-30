from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from album.models import Album
from . import models


def photo_list(request, album_id):
    """
    查看指定相册中的所有照片
    :param request:
    :param album_id:
    :return:
    """
    album = Album.objects.get(pk=album_id)
    photo_list = models.Photo.objects.filter(album=album).order_by('-upload_time')
    return render(request, 'photo/photo_list.html', {'album': album, 'photo_list': photo_list})


def photo_upload(request, album_id):
    """
    上传照片
    :param request:
    :param album_id:
    :return:
    """
    album = Album.objects.get(pk=album_id)
    if request.method == "GET":
        return render(request, 'photo/photo_upload.html', {'album': album})
    elif request.method == "POST":
        # 获取数据
        path = request.FILES['path']
        name = request.POST['name']

        # 创建并保存照片
        photo = models.Photo(name=name, path=path, album=album)
        photo.save()

        # 更新相册照片数量
        album.photo_count = len(album.photo_set.all())
        album.save()

        # 返回相册信息页面
        return redirect(reverse('photo_list', kwargs={'album_id': album.id}))


def photo_detail(request, photo_id):
    """
    查看照片详情
    :param request:
    :param photo_id:
    :return:
    """
    photo = models.Photo.objects.get(pk=photo_id)
    return render(request, 'photo/photo_detail.html', {'photo': photo})