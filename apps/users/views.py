# _*_ encoding:utf-8 _*_
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from users.models import UserPorfile, EmailVerifyRecord
from operation.models import UserFavorite, UserMessage
from organization.models import Teacher, CourseOrg
from course.models import Course
from users.forms import RegisterForms,ForgetPwdForms,ResetPwdForms, UserImageUpdateForm, UserPwdUpdateForms, UserEmailUpdateSendEmailForm, UserInfoUpdateForm
from users.commonfunction import sendEmailToUser
# Create your views here.

import json
from OnlineMx.utils import NeedLogin


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


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("userlogin"))


class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        getnext = request.GET.get('next', '')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                # return render(request,'index.html',{"user":user},context_instance=RequestContext(request))
                if not getnext:
                    return render(request,'index.html',{"user":user})
                else:
                    return HttpResponseRedirect(getnext)
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


# class UserCenterInfo(LoginRequiredMixin, View):
class UserCenterInfo(NeedLogin, View):
    # login_url = '/login/'
    # redirect_field_name = '/user/info'
    def get(self, request):
        return render(request, 'usercenter-info.html',{
            'userinfo':request.user,
        })

    def post(self, request):
        print request.POST
        userinfo_form = UserInfoUpdateForm(request.POST, instance=request.user)
        if userinfo_form.is_valid():
            print "xxxxxxxxxxxxxxxxxx"
            print userinfo_form.cleaned_data
            userinfo_form.save()
            return HttpResponse(json.dumps({"status":"success"}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"status":"failure"}), content_type="application/json")

class UserImageUpdate(NeedLogin, View):
    def post(self, request):
        user_image = UserImageUpdateForm(request.POST, request.FILES, instance=request.user)
        if user_image.is_valid():
            # a = user_image.cleaned_data["head_portrait"]
            # print a.name
            user_image.save()
            return HttpResponse({'status':'success'}, content_type='application/json')
        else:
            return HttpResponse({'status':'fail'}, content_type='application/json')


#此时用户已经是一种登录的状态，所有可以不需要验证
class UserPwdUpdate(NeedLogin, View):
    def post(self, request):
        pwd_form = UserPwdUpdateForms(request.POST)
        if pwd_form.is_valid():
            if pwd_form.cleaned_data['password1'] == pwd_form.cleaned_data['password2']:
                user = request.user
                user.password = make_password(pwd_form.cleaned_data['password2'])
                user.save()
                return HttpResponse({"status":"success"}, content_type="application/json")
            else:
                return HttpResponse({"status":"fail","msg":u"密码不一致"}, content_type="application/json")
        else:
            return HttpResponse(json.dumps(pwd_form.errors), content_type="application/json")


class UserEmailUpdateSendEmail(NeedLogin, View):
    def get(self, request):
        email = request.GET.get("email", "")
        if UserPorfile.objects.filter(email=email):
            return HttpResponse({"status":"failure"}, content_type="application/json")
        sendEmailToUser(email, 2)
        return HttpResponse({"status":"success"}, content_type="application/json")


class UserEmailUpdate(NeedLogin, View):
    def post(self, request):
        email_update_form = UserEmailUpdateSendEmailForm(request.POST)
        if email_update_form.is_valid():
            email = email_update_form.cleaned_data["email"]
            code = email_update_form.cleaned_data["code"]
            try:
                has_record = EmailVerifyRecord.objects.get(email=email, code=code)
            except:
                has_record = 0
            if has_record:
                user = request.user
                user.email = email
                user.save()
                return HttpResponse({"status":"success"}, content_type="application/json")
            else:
                return HttpResponse({"status":"fail"}, content_type="application/json")
        else:
            return HttpResponse({"status":"fail"}, content_type="application/json")


class UserFavTeacherView(NeedLogin, View):
    def get(self, request):
        teachers = list()
        user_fav_teacher = UserFavorite.objects.filter(user=request.user, fav_type=2)
        for i in user_fav_teacher:
            teacher = Teacher.objects.get(id=i.fav_id)
            teachers.append(teacher)
        return render(request, "usercenter-fav-teacher.html", {
            'user_fav_teacher':teachers,
        })


class UserFavOrgView(NeedLogin, View):
    def get(self, request):
        orgs = list()
        user_fav_org = UserFavorite.objects.filter(user=request.user, fav_type=1)
        for i in user_fav_org:
            org = CourseOrg.objects.get(id=i.fav_id)
            orgs.append(org)
        return render(request, "usercenter-fav-org.html", {
            'user_fav_orgs':orgs,
        })


class UserFavCourseView(NeedLogin, View):
    def get(self, request):
        courses = list()
        user_fav_course = UserFavorite.objects.filter(user=request.user, fav_type=3)
        for i in user_fav_course:
            course = Course.objects.get(id=i.fav_id)
            courses.append(course)
        return render(request, "usercenter-fav-course.html", {
            'user_fav_courses':courses,
        })


class UserMessageView(NeedLogin, View):
    def get(self, request):
        all_message = UserMessage.objects.filter(user=request.user.id)
        page = request.GET.get("page", 1)
        pageObjects = Paginator(all_message, 5, request=self.request)
        try:
            currentPage = pageObjects.page(int(page))
        except (PageNotAnInteger, EmptyPage):
            currentPage = pageObjects.page(1)
        return render(request, 'usercenter-message.html',{
            'currentPage':currentPage,
        })


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html',{})

#404
def page_not_found(request):
    response = render_to_response('404.html')
    response.status_code = 404
    return response

def page_error(request):
    response = render_to_response('500.html')
    response.status_code = 500
    return response