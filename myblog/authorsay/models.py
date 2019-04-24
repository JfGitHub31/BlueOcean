from django.db import models
from author.models import Author


class AuthorSay(models.Model):
    """
    说说模型类
    """
    id = models.AutoField(primary_key=True, verbose_name='说说编号')
    content = models.TextField(verbose_name='说说内容')
    say_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')

    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='所属用户')
