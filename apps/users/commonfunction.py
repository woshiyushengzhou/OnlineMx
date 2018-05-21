# _*_ encoding:utf8 _*_

from django.core.mail import send_mail
import random

from OnlineMx.settings import EMAIL_HOST_USER
from users.models import EmailVerifyRecord

def crateRandomSeq():
    stdseq = "abcdefghijklmnopqrxtuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    usercode = ""
    for i in range(20):
        usercode += random.choice(stdseq)
    return usercode

def sendEmailToUser(emailaccount,sendtype):
    '''type 0 注册，type 1 忘记密码'''
    code = crateRandomSeq()
    email = emailaccount
    send_type = sendtype
    emailrecord = EmailVerifyRecord()
    emailrecord.code = code
    emailrecord.email = email
    emailrecord.send_type = send_type
    emailrecord.save()
    mailtitle = u"菜鸟在线教育注册激活链接"
    mailbody = u"请访问下面的地址激活您的账号: http://127.0.0.1:8000/activate/{0}".format(code)
    if sendtype == 0:
        send_status = send_mail(mailtitle,mailbody,EMAIL_HOST_USER,[email])
        return send_status
    if sendtype == 1:
        mailtitle = u"菜鸟在线教育修改密码链接"
        mailbody = u"请访问下面的地址修改您的密码: http://127.0.0.1:8000/resetpwd/{0}".format(code)
        send_status = send_mail(mailtitle,mailbody,EMAIL_HOST_USER,[email])
        return send_status
