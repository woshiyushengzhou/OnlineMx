# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models

from datetime import datetime


# Create your models here.

choices_in_model = (
    ('gender_choices',(('man',u'男性'),('woman',u'女性'))),
    ('email_send_type',(('register',u'注册'),('forget',u'忘记密码'))),
)
class UserPorfile(AbstractUser):
    nickname = models.CharField(max_length=30,verbose_name=u'昵称',null=True,blank=True)
    barth_day = models.DateField(verbose_name=u'生日',null=True,blank=True)
    gender = models.CharField(verbose_name=u'性别',choices=choices_in_model[0][1],max_length=5)
    address = models.CharField(max_length=200,verbose_name=u'地址',null=True,blank=True)
    phone_num = models.CharField(max_length=11,verbose_name=u"手机号")
    head_portrait = models.ImageField(upload_to='image/%Y/%m',default=u'image/default.png',max_length=100,verbose_name=u'用户头像')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name


    def __unicode__(self):
        return self.username


#邮箱验证码模型
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name=u'验证码')
    email = models.EmailField(verbose_name=u'用户邮箱',max_length=60)
    send_type = models.CharField(verbose_name=u'发送类型',choices=choices_in_model[1][1],max_length=20)
    send_time = models.DateTimeField(verbose_name=u'发送时间',default=datetime.now)

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.code

#轮播图模型
class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name=u'标题')
    image = models.ImageField(max_length=100,verbose_name=u'轮播图',upload_to="banner/%Y/%m")
    url = models.URLField(max_length=200,verbose_name=u'访问地址')
    index = models.IntegerField(default=100,verbose_name=u'顺序')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title