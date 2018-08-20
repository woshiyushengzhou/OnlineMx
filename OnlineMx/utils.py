# _*_ encoding:utf8 _*_
from django.contrib.auth.mixins import LoginRequiredMixin

#封装需要登录混合类
class NeedLogin(LoginRequiredMixin):
    login_url = '/login/'