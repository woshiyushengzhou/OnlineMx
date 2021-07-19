# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

from datetime import datetime
from organization.models import CourseOrg, Teacher

# Create your models here.
class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程所属机构",blank=True,null=True)
    teacher = models.ForeignKey(Teacher, verbose_name=u"授课老师", blank=True, null=True)
    courseName = models.CharField(max_length=40,verbose_name=u'课程名称')
    courseIntroduction = models.TextField(verbose_name=u'课程简介')
    courseDegree = models.CharField(verbose_name=u'课程难度',choices=(('chuji',u'初级'),('zhongji',u'中级'),('gaoji',u'高级')),max_length=10)
    courseTime = models.IntegerField(verbose_name=u'课程时长',default=0)
    students = models.IntegerField(verbose_name=u'学习人数',default=0)
    #chapters = models.SmallIntegerField(verbose_name=u'课程章节数',default=0)
    category = models.CharField(verbose_name=u'课程类别',max_length=30)
    click_nums = models.IntegerField(verbose_name=u'课程点击数',default=0)
    courseCover = models.ImageField(verbose_name=u'课程封面',upload_to='courses/%Y/%m')
    collect_nums = models.IntegerField(verbose_name=u'收藏人数',default=0)
    need_know = models.CharField(verbose_name=u"课程须知", max_length=300, default="xxx")
    teacher_will_tell = models.CharField(verbose_name=u"老师将告诉你", max_length=300, default="xxx")
    add_time = models.DateTimeField(verbose_name=u'课程加入时间',default=datetime.now)
    #获取该课程章节数
    def get_chapters_number(self):
        return self.chapter_set.count()

    def get_user(self):
        return self.usercourse_set.all()[0:5]

    #获取所有章节对象
    def get_chapters(self):
        return self.chapter_set.all()

    def get_resoure(self):
        return self.courseresource_set.all()

    class Meta:
        verbose_name=u'课程'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.courseName

    def tt(self):
        return "aaa"


#章节表
class Chapter(models.Model):
    name = models.CharField(verbose_name=u'章节名称',max_length=50)
    course = models.ForeignKey(Course,verbose_name=u'课程名称')
    add_time = models.DateTimeField(verbose_name=u'添加时间',default=datetime.now)
    #获取该章节下所有视频
    def get_viedo(self):
        return self.viedo_set.all()

    class Meta:
        verbose_name=u'章节'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

#视频表
class Viedo(models.Model):
    name = models.CharField(verbose_name=u'视频名称',max_length=50)
    chapter = models.ForeignKey(Chapter,verbose_name=u'章节')
    url = models.URLField(verbose_name=u"视频地址", default="www.baidu.com")
    viedo_time = models.CharField(verbose_name=u"视频时长", max_length=20, default="0:0")
    add_time = models.DateTimeField(verbose_name=u"添加时间",default=datetime.now)

    class Meta:
        verbose_name=u'视频'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

class CourseResource(models.Model):
    course = models.ForeignKey(Course,verbose_name=u'课程')
    name = models.CharField(max_length=50,verbose_name=u'资源名称')
    download = models.FileField(upload_to='course/resource/%Y/%m',verbose_name=u'下载')
    add_time = models.DateTimeField(verbose_name=u'添加时间',default=datetime.now)

    class Meta:
        verbose_name=u'资源'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
