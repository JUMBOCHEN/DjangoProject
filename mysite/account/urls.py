from django.conf.urls import url
from .import views

from django.conf import settings
from django.contrib.auth import views as auth_views #引入内置视图文件并重新命名为
urlpatterns = [
    #url(r'^login/$', views.user_login, name='user_login')   #自定义的登陆
    url(r'^login/$', auth_views.login, name='user_login')auth_views
]