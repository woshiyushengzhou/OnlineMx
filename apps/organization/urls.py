# _*_ encoding:utf8 _*_
__author__ = 'sz.yu'

from django.conf.urls import url
from organization.views import UserAskView, OrgDetail, AllCourse, OrgDteailDesc, OrgTeachers, AddFav, TeacherList, TeacherDetailList
urlpatterns = [
    url(r'userask/$',UserAskView.as_view(),name="userask"),
    url(r'orghome/(?P<orgid>\d{1,4})/$',OrgDetail.as_view(),name='orgdetail'),
    url(r'org-detail-course/(?P<org_id>\d{1,4})/(?P<page>\d{1,4})/$',AllCourse.as_view(),name='orgdeatilcourse'),
    url(r'org-detail-desc/(?P<org_id>\d{1,4})/$',OrgDteailDesc.as_view(), name='orgdetaildesc'),
    url(r'org-detail-teachers/(?P<org_id>\d{1,4})/(?P<page>\d{1,4})/$',OrgTeachers.as_view(), name='orgteachers'),
    #用户收藏
    url(r'add_fav/$', AddFav.as_view(), name='add_fav'),
    url(r'teacher-list/$', TeacherList.as_view(), name='teahcerlist'),
    url(r'teacher-detail/(?P<teacherid>\d{1,4})/$',TeacherDetailList.as_view(), name='teacherdetail')
]
