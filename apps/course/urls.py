# _*_ encoding:utf8 _*_

from django.conf.urls import url

from course.views import CourseList, CourseDetail, CourseViedo, CourseComment
urlpatterns = [
    url(r'course_list/$', CourseList.as_view(), name="course_list"),
    url(r'course_detail/(?P<course_id>\d{1,5})$', CourseDetail.as_view(), name="course_detail"),
    url(r'course_viedo/(?P<course_id>\d{1,5})/$', CourseViedo.as_view(), name="course_viedo"),
    url(r'course_comment/$', CourseComment.as_view(), name="course_comment"),
]
