from django.conf.urls import url
from .import views

from django.conf import settings
from django.contrib.auth import views as auth_views #引入内置视图文件并重新命名为

urlpatterns = [
    #url(r'^login/$', views.user_login, name='user_login'),   #自定义的登陆
    url(r'^login/$', auth_views.login, name='user_login'),  #django内置登陆
    #url(r'^new-login/$', auth_views.login, {"template_name": 'account/login.html'}),    #传值 跳转至自定义登陆模板
    #url(r'^logout/$', auth_views.logout, name='user_logout')，    #django内置退出模板
    url(r'^logout/$', auth_views.logout, {"template_name": 'account/logout.html/'}, name='user_logout'),
    url(r'^register/$', views.register, name='user_register'),
    url(r'^password-change/$', auth_views.password_change, name='password_change'),
    url(r'^password-change-done/$', auth_views.password_change_done, name='password_change_done'),
    url(r'^my-information/$', views.myself, name='my_information'),
]