"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index, name='index'),
    # 用户app
    url(r'^author/', include('author.urls')),

    # 文章app
    url(r'^article/', include('article.urls')),

    # 说说app
    url(r'^authorsay/', include('authorsay.urls')),

    # 留言板app
    url(r'^message/', include('message.urls')),

    # 相册app
    url(r'^album/', include('album.urls')),

    # 相片app
    url(r'^photo/', include('photo.urls')),
]
