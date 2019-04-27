from django.db import models
from author.models import Author


class Album(models.Model):
    """
    相册数据模型类
    """
    id = models.AutoField(primary_key=True, verbose_name='相册编号')
    name = models.CharField(max_length=50, verbose_name='相册名称')
    cover = models.ImageField(upload_to='static/images/album/', default='static/images/album/default.jpg')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    remark = models.TextField(null=True, blank=True, verbose_name='相册描述')
    photo_count = models.IntegerField(default=0, verbose_name='照片数量')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='所属用户')

