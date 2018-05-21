# _*_ encoding:utf-8 _*_
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.template import RequestContext
from django.views.generic import View
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib.auth.hashers import make_password

from users.models import UserPorfile,EmailVerifyRecord
from users.forms import RegisterForms,ForgetPwdForms,ResetPwdForms
from users.commonfunction import sendEmailToUser
# Create your views here.

#自定义登陆
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            userobject = UserPorfile.objects.get(Q(username=username) | Q(email=username))
            #密码是加密后存储的
            if userobject.check_password(password):
                return userobject
        except Exception as e:
            return None


#账户激活
class UserAccountActivate(View):
    def get(self,request,code):
        mailtemp = EmailVerifyRecord.objects.filter(code=code)[0]
        if mailtemp:
            usertemp = UserPorfile.objects.get(email=mailtemp.email)
            usertemp.is_active = True
            usertemp.save()
            return render(request,"activesuccess.html")
        else:
            return render(request,"activefail.html")

class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                # return render(request,'index.html',{"user":user},context_instance=RequestContext(request))
                return render(request,'index.html',{"user":user})
            else:
                return render(request,'login.html',{"err_msg":u"用户未激活"})
        else:
            return render(request,'login.html',{"err_msg":u"用户名或密码错误"})


class RegisterView(View):
    def get(self,request):
        register_form = RegisterForms()
        return render(request,"register.html",{"register_form":register_form})
    def post(self,request):
        register_form = RegisterForms(request.POST)
        if register_form.is_valid():
            username = request.POST['email']
            password = request.POST['password']
            user_profile = UserPorfile()
            user_profile.username = username
            user_profile.email = username
            #必须对密码加密 否则无法登录
            user_profile.password = make_password(password)
            user_profile.is_active = False
            user_profile.save()
            # return render(request,'login.html')
            sendEmailToUser(request.POST['email'],0)
            return redirect(reverse('userlogin'))
        else:
            return render(request,"register.html",{"register_form":register_form})


class ForgetPwdView(View):
    def get(self,request):
        forget_pwd = ForgetPwdForms()
        return render(request,"forgetpwd.html",{"forget_pwd":forget_pwd})
    def post(self,request):
        forget_pwd = ForgetPwdForms(request.POST)
        if forget_pwd.is_valid():
            tempuser = UserPorfile.objects.filter(email=request.POST.get('email'))
            if tempuser:
                sendEmailToUser(request.POST['email'],1)
                return render(request,'forgetLinkHasSend.html')
            else:
                return render(request,"forgetpwd.html",{"errmess":u"账号不存在"})
        else:
            return render(request,"forgetpwd.html",{"errmess":u"邮箱或验证码错误"})


class ResetPwdView(View):
    def get(self,request,code):
        has = EmailVerifyRecord.objects.filter(code=code)
        if has:
            emailvalue = has[0].email
            return render(request,"password_reset.html",{"emailvalue":emailvalue})
        else:
            return render(request,"errorlink.html")


class ModifyPwdView(View):
    def post(self,request):
        resetform = ResetPwdForms(request.POST)
        if resetform.is_valid():
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            email = request.POST.get("email")
            if password1 == password2:
                user = UserPorfile.objects.filter(email=email)[0]
                user.password = make_password(password2)
                user.save()
                return render(request,'login.html')
            else:
                return render(request,"password_reset.html",{"emailvalue":u"您输入的密码不一致"})
        else:
            emailvalue = request.POST.get("email")
            return render(request,"password_reset.html",{"emailvalue":emailvalue})