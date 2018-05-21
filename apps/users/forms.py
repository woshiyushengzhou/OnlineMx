# _*_ encoding:utf8 _*_
from django import forms
from captcha.fields import CaptchaField

class LoginForms(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


#邮箱注册
#验证码功能 GitHub captcha 查看使用文档
class RegisterForms(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    captcha = CaptchaField()


class ForgetPwdForms(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField()


class ResetPwdForms(forms.Form):
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)
    email = forms.EmailField(required=True)