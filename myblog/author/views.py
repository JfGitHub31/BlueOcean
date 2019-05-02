from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from . import models


def author_index(request, author_id):
    """
    个人首页路由视图处理函数
    :param request:
    :param author_id:
    :return:
    """
    # 查询得到的用户
    author = models.Author.objects.get(pk=author_id)
    # 返回展示用户首页
    return render(request, 'author/main_index.html', {'author': author})


def author_register(request):
    """
    用户注册视图处理函数
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "author/register.html", {})

    elif request.method == "POST":
        # 获取数据
        username = request.POST.get('username')
        userpass = request.POST.get('userpass')
        re_userpass = request.POST.get('re_userpass')
        realname = request.POST.get('realname')

        # 判断账号是否可用
        try:
            author = models.Author.objects.get(username=username)

            return render(request, 'author/register.html', {'error_msg': '账号已存在,请重新注册'})

        except:
            # 判断两次密码输入是否一致
            if userpass != re_userpass:
                return render(request, 'author/register.html', {'error_msg': '两次密码不一致,请重新输入'})


            # 注册账号
            author = models.Author(username=username, userpass=userpass, realname=realname)
            author.save()

            # 跳转到登录界面
            return render(request, 'author/login.html', {'error_msg': '账号注册成功,请登录'})


def author_login(request):
    """
    博客用户登录视图处理函数
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'author/login.html', {})

    elif request.method == "POST":
        # 获取数据
        username = request.POST.get('username')
        userpass = request.POST.get('userpass')

        # 验证账号和密码是否正确
        try:
            pass
            author = models.Author.objects.get(username=username, userpass=userpass)

            # 账号和密码正确存入session中
            request.session['login_user'] = author
            # 浏览器关闭时session过期销毁此时用户退出
            request.session.set_expiry(0)
            # 跳转到首页去
            return redirect('/')

        except:
            return render(request, 'author/login.html', {'error_msg': '账号或密码有误请重新登录'})


def author_logout(request):
    """
    用户安全退出系统功能
    :param request:
    :return:
    """
    request.session.clear()

    return redirect('/')


def author_password(request):
    """
    修改登录密码
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'author/password.html', {})

    elif request.method == "POST":
        # 获取密码,修改数据
        old_passwd = request.POST.get('old_passwd')
        new_passwd = request.POST.get('new_passwd')
        re_passwd = request.POST.get('re_passwd')

        # 判断原密码是否正确
        if old_passwd != request.session['login_user'].userpass:
            return render(request, 'author/password.html', {'error_msg': '原密码错误，请重新输入'})

        # 判断两次密码输入是否一致
        if new_passwd != re_passwd:
            return render(request, 'author/password.html', {'error_msg': '两次密码不一致请重新输入'})

        # 修改密码
        author = request.session['login_user']
        author.userpass = new_passwd

        author.save()

        # 清空session数据
        request.session.clear()

        # 跳转到登录页面
        return render(request, 'author/login.html', {'error_msg': '密码修改成功,请重新登录'})


def author_update(request):
    """
    修改个人资料
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'author/author_update.html', {})

    elif request.method == "POST":
        # 获取数据并修改
        realname = request.POST.get('realname')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        intro = request.POST.get('intro')
        header_img = request.FILES.get('header_img')

        # 获取当前用户
        author = request.session['login_user']
        author.realname = realname
        author.age = age
        author.gender = gender
        author.email = email
        author.phone = phone
        author.intro = intro
        author.header_img = header_img

        author.save()
        request.session['login_user'] = author

        # 返回个人资料页面
        return redirect(reverse('author_info', kwargs={'author_id': author.id}))


def author_info(request, author_id):
    """
    查看个人资料视图处理函数
    :param request:
    :param author_id:
    :return:
    """
    # 查询用户信息
    author = models.Author.objects.get(pk=author_id)
    return render(request, 'author/author_info.html', {'author': author})