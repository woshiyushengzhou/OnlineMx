__author__ = 'sz.yu'
from django.conf.urls import url

# from django.views.generic.base import TemplateView
from users.views import UserCenterInfo, UserImageUpdate, UserPwdUpdate, UserEmailUpdateSendEmail, UserEmailUpdate
from users.views import UserFavTeacherView, UserFavOrgView, UserFavCourseView,UserMessageView
urlpatterns = [
    url(r'^info/$', UserCenterInfo.as_view(), name='userinfo'),
    url(r'userimageupdate/$', UserImageUpdate.as_view(), name='userimageupdate'),
    url(r'userpwdupdate/$', UserPwdUpdate.as_view(), name='userpwdupdate'),
    url(r'ueuse/$', UserEmailUpdateSendEmail.as_view(), name='ueuse'),
    url(r'useremailupdate/$', UserEmailUpdate.as_view(), name='useremailupdate'),
    url(r'userfav/teacher/$', UserFavTeacherView.as_view(), name="userfavteacher"),
    url(r'userfav/org/$', UserFavOrgView.as_view(), name="userfavorg"),
    url(r'userfav/course/$', UserFavCourseView.as_view(), name="userfavcourse"),
    url(r'message/$', UserMessageView.as_view(), name="usermessage"),
]