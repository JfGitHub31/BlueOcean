# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-05-01 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='作者年龄'),
        ),
    ]
