from django.db import models
from author.models import Author


class Message(models.Model):
    """
    留言板数据类型
    """
    id = models.AutoField(primary_key=True, verbose_name="主键编号")
    content = models.TextField(verbose_name='留言内容')
    msg_time = models.DateTimeField(auto_now_add=True, verbose_name="留言时间")
    send_author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='sender', verbose_name='发表人')
    receive_author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='receive', verbose_name='接收人')
