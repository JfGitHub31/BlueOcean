from django.db import models
from author.models import Author


class Article(models.Model):
    """
    博客文章数据模型类
    """
    id = models.AutoField(primary_key=True, verbose_name='文章编号')
    title = models.CharField(max_length=100, verbose_name='文章标题')
    content = models.TextField(verbose_name='文章内容')

    publish_time = models.DateTimeField(verbose_name='发表时间', auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    read_count = models.IntegerField(default=0, verbose_name='阅读次数')
    comment_count = models.IntegerField(default=0, verbose_name='评论次数')

    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='作者')
