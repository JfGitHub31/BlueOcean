from django.db import models
from album.models import Album


class Photo(models.Model):
    """
    照片模型类
    """
    id = models.AutoField(primary_key=True, verbose_name='照片主键')
    name = models.CharField(max_length=50, verbose_name='照片名称')
    path = models.ImageField(upload_to='static/images/photo/', verbose_name='照片路径')
    upload_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')
    read_count = models.IntegerField(default=0, verbose_name='查看次数')
    remark = models.TextField(null=True, blank=True, verbose_name='照片描述')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='所属相册')

