__author__ = "jianfeng777"


from django.shortcuts import render
from author.models import Author


def index(request):
    # 查询用户
    pass

    author_list = Author.objects.all().order_by('-join_time')[:4]

    return render(request, 'index.html', {'author_list': author_list})