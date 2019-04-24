from django.db import models


class AuthorManager(models.Manager):

    def get_by_natural_key(self, id, username, realname, header_img):
        return self.get(id=id, username=username, realname=realname, header_img=header_img)


class Author(models.Model):
    objects = AuthorManager()

    """
    博客用户数据模型类
    """
    id = models.AutoField(primary_key=True, verbose_name="作者编号")
    username = models.CharField(max_length=50, verbose_name="登录账号")
    userpass = models.CharField(max_length=50, verbose_name="登录密码")
    realname = models.CharField(max_length=50, verbose_name="作者姓名")
    header_img = models.ImageField(upload_to="static/images/headers/", default="static/images/headers/default.jpg")
    age = models.IntegerField(default=0, verbose_name="作者年龄", null=True, blank=True)
    gender = models.CharField(max_length=5, verbose_name="作者性别", null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name="联系方式", null=True, blank=True)
    email = models.CharField(max_length=20, verbose_name="电子邮箱", null=True, blank=True)
    join_time = models.DateTimeField(auto_now_add=True, verbose_name="注册时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后修改时间")
    intro = models.TextField(verbose_name="个人介绍", null=True, blank=True)

    def natural_key(self):

        return (self.id, self.username, self.realname, self.header_img)
