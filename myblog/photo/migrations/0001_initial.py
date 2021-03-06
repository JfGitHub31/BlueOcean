# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-05-01 09:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='照片主键')),
                ('name', models.CharField(max_length=50, verbose_name='照片名称')),
                ('path', models.ImageField(upload_to='static/images/photo/', verbose_name='照片路径')),
                ('upload_time', models.DateTimeField(auto_now_add=True, verbose_name='上传时间')),
                ('read_count', models.IntegerField(default=0, verbose_name='查看次数')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='照片描述')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album.Album', verbose_name='所属相册')),
            ],
        ),
    ]
