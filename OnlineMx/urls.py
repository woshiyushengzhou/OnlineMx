# _*_ encoding:utf8 _*_
"""OnlineMx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url,include
from django.views.generic import TemplateView
#配置后台上传文件处理url
from django.views.static import serve

from users.views import LoginView,RegisterView,UserAccountActivate,ForgetPwdView,ResetPwdView,ModifyPwdView, LogoutView, IndexView
from organization.views import OrgView
from OnlineMx.settings import MEDIA_ROOT
import xadmin
urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^index/$', IndexView.as_view(), name="index"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^login/$',LoginView.as_view(),name="userlogin"),
    url(r'^logout/$',LogoutView.as_view(),name="userlogout"),
    url(r'^register/$',RegisterView.as_view(),name="register"),
    url(r'^activate/(?P<code>.+)/$',UserAccountActivate.as_view(),name="activate"),
    url(r'^forget/$',ForgetPwdView.as_view(),name="forget"),
    url(r'^resetpwd/(?P<code>.+)/$',ResetPwdView.as_view(),name="resetpwd"),
    url(r'^modifypwd/$',ModifyPwdView.as_view(),name="modifypwd"),
    url(r'^org-list/$',OrgView.as_view(),name="orglist"),
#配置后台上传文件处理url,上下文渲染（可以在Template的html文件中使用静态文件路径）
# [14/Aug/2018 21:15:36] "GET /uploadimage/courses/2018/06/02.jpg HTTP/1.1" 200 63229
# [14/Aug/2018 21:15:36] "GET /uploadimage/courses/2018/06/bank3_5bUIRy1.jpg HTTP/1.1" 200 4057
    url(r'^uploadimage/(?P<path>.+)$',serve,{"document_root":MEDIA_ROOT}),
    # url(r'^static/(?P<path>.+)$',serve,{"document_root":STATIC_ROOT}),
    url(r'^org/',include("organization.urls",namespace="org")),
    url(r'^course/', include("course.urls", namespace="course")),
    url(r'^user/', include("users.urls", namespace="user")),
]
handler404 = "users.views.page_not_found"
handler500 = "users.views.page_error"