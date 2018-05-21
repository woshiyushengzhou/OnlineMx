# _*_ encoding:utf-8 _*_

from __future__ import unicode_literals

from django.db import models

from datetime import datetime

from users.models import UserPorfile
from course.models import Course
# Create your models here.

class UserAsk(models.Model):
    name = models.CharField(max_length=20,verbose_name=u"名字")
    mobile = models.CharField(max_length=11,verbose_name=u"手机号")
    course_name = models.CharField(max_length=50,verbose_name=u"课程名称")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name=u"用户咨询"
        verbose_name_plural=verbose_name


class CourseComments(models.Model):
    user = models.ForeignKey(UserPorfile,verbose_name=u"用户名称")
    course = models.ForeignKey(Course,verbose_name=u"课程名称")
    comment_message = models.TextField(verbose_name=u"评论详情")
    comment_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name=u"评论"
        verbose_name_plural=verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserPorfile,verbose_name=u"用户名称")
    fav_id = models.IntegerField(default=0,verbose_name=u"数据id")
    fav_type = models.SmallIntegerField(choices=((1,u"课程机构"),(2,u"授课教师"),(3,u"公开课程")))
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name=u"用户收藏"
        verbose_name_plural=verbose_name


class UserMessage(models.Model):
    #0 所以用户都接受  非0 指定用户接受
    user = models.IntegerField(default=0,verbose_name=u"接受用户")
    message = models.CharField(max_length=500,verbose_name=u"消息内容")
    # 用户是否读过
    has_read = models.BooleanField(default=False,verbose_name=u"消息是否读过")
    send_time = models.DateTimeField(default=datetime.now,verbose_name=u"消息发送时间")

    class Meta:
        verbose_name=u"用户消息"
        verbose_name_plural=verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserPorfile,verbose_name=u"用户名称")
    course = models.ForeignKey(Course,)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name=u"用户课程"
        verbose_name_plural=verbose_name