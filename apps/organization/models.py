# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.

class CityDict(models.Model):
    name = models.CharField(max_length=20,verbose_name=u"城市名称")
    desc = models.CharField(max_length=200,verbose_name=u"城市描述")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"加入时间")

    class Meta:
        verbose_name=u"城市"
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name


#课程机构
class CourseOrg(models.Model):
    name = models.CharField(verbose_name=u'机构名称',max_length=50)
    category = models.CharField(max_length=10,verbose_name=u"机构类别",choices=(("pxjg","培训机构"),("gx","高校"),("gr","个人")),default="pxjg")
    desc = models.TextField(verbose_name=u"机构描述")
    click_nums = models.IntegerField(default=0,verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0,verbose_name=u"收藏数")
    image = models.ImageField(upload_to="org/%Y/%m",verbose_name=u"机构封面图")
    address = models.CharField(max_length=200,verbose_name=u"机构地址")
    city = models.ForeignKey(CityDict,verbose_name=u"所在城市")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"加入时间")

    class Meta:
        verbose_name = u"课程机构"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class  Teacher(models.Model):
    name = models.CharField(max_length=20,verbose_name=u"教师名称")
    work_years = models.SmallIntegerField(default=0,verbose_name=u"工作年限")
    work_company = models.CharField(max_length=100,verbose_name=u"就职公司")
    position = models.CharField(max_length=50,verbose_name=u"职位")
    points = models.CharField(max_length=200,verbose_name=u"教学特点")
    click_nums = models.IntegerField(default=0,verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0,verbose_name=u"收藏数")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"加入时间")

    class Meta:
        verbose_name = u"课程教师"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

