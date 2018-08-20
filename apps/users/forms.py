# _*_ encoding:utf8 _*_
from django import forms
from captcha.fields import CaptchaField

from models import UserPorfile

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


class UserImageUpdateForm(forms.ModelForm):
    class Meta:
        model = UserPorfile
        fields = ['head_portrait']


class UserPwdUpdateForms(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)


class UserEmailUpdateSendEmailForm(forms.Form):
    email = forms.EmailField(required=True)
    code = forms.CharField(required=True, max_length=4, min_length=4)


class UserInfoUpdateForm(forms.ModelForm):
    class Meta:
        model = UserPorfile
        fields = ["nickname","barth_day","gender","address","phone_num"]
