# _*_ encoding:utf8 _*_
from django.views.generic import View,ListView
from django.http import HttpResponse


import json
from organization.models import CityDict, CourseOrg, Teacher
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from organization.forms import UserAskForm
from django.shortcuts import get_object_or_404, render
from operation.models import UserFavorite
from course.models import Course
# from course.models import Course
# from operation.models import UserAsk
# Create your views here.
class OrgView(ListView):
    queryset = CourseOrg.objects.all()
    template_name = "org-list.html"
    def get_context_data(self,**kwargs):
        all_org = self.queryset
        #根据机构类别筛选
        category_i = self.request.GET.get("ct","")
        if category_i:
            all_org = all_org.filter(category=category_i)
        #根据城市筛选
        city_id = self.request.GET.get("city","")
        if city_id:
            all_org = all_org.filter(city_id=int(city_id))
        page = self.request.GET.get("page",1)
        p = Paginator(all_org,1,request=self.request)
        page_list = p.page(page)

        context1 = {
            "all_org":all_org,
            "page_list":page_list,
            "all_city":CityDict.objects.all(),
            "city_id":city_id,
            "category_i":category_i,
            "org_order":CourseOrg.objects.all().order_by('-click_nums')[:3]
        }
        context = super(OrgView,self).get_context_data(**kwargs)
        context.update(context1)
        return context

class UserAskView(View):
    def post(self,request):
        data_temp = UserAskForm(request.POST)
        if data_temp.is_valid():
            data_temp.save()
            return HttpResponse(json.dumps({'status':'success'}),content_type='application/json')
        else:
            return HttpResponse(json.dumps({'status':'fail','msg':"咨询失败请重新输入"}),content_type='application/json')

class OrgDetail(View):
    def get(self, request, orgid):
        currentpage = "Home"
        org_temp = get_object_or_404(CourseOrg,id=int(orgid))
        org_course_list = org_temp.course_set.all()[0:3]
        org_teacher_list = org_temp.teacher_set.all().order_by("click_nums")[0:3]
        # teacher_one = org_teacher_list.course_set.all().order_by("click_nums")[0]
        if request.user.is_authenticated():
            try:
                is_record = UserFavorite.objects.get(user=request.user, fav_id=org_temp.id, fav_type=1)
            except (UserFavorite.DoesNotExist, UserFavorite.MultipleObjectsReturned):
                is_record = ''
            if is_record:
                is_fav = True
            else:
                is_fav = False
        else:
            is_fav = False
        return render(request, 'org-detail-homepage.html',{
            'org_course_list':org_course_list,
            'org_teacher_list':org_teacher_list,
            'org_temp':org_temp,
            'currentpage':currentpage,
            'is_fav':is_fav,
        })


class AllCourse(View):
    def get(self, request, page, org_id):
        currentpage = "OrgCourse"
        org = CourseOrg.objects.get(id=org_id)
        object_list = org.course_set.all()
        p = Paginator(object_list, 3)
        # print p.count
        try:
            per_page = p.page(page)
        except PageNotAnInteger:
            per_page = p.page(1)
        except EmptyPage:
            per_page = p.page(p.num_pages)
        # print per_page.next_page_number()
        if request.user.is_authenticated():
            try:
                is_record = UserFavorite.objects.get(user=request.user, fav_id=org.id, fav_type=1)
            except (UserFavorite.DoesNotExist, UserFavorite.MultipleObjectsReturned):
                is_record = ''
            if is_record:
                is_fav = True
            else:
                is_fav = False
        else:
            is_fav = False
        return render(request, "org-detail-course.html", {'per_page':per_page,
                                                          'org_temp':org,
                                                          'currentpage':currentpage,
                                                          'is_fav':is_fav,
                                                    })


class OrgDteailDesc(View):
    def get(self,request,org_id):
        currentpage = 'OrgDetailDesc'
        org = get_object_or_404(CourseOrg,id=org_id)
        if request.user.is_authenticated():
            try:
                is_record = UserFavorite.objects.get(user=request.user, fav_id=org.id, fav_type=1)
            except (UserFavorite.DoesNotExist, UserFavorite.MultipleObjectsReturned):
                is_record = ''
            if is_record:
                is_fav = True
            else:
                is_fav = False
        else:
            is_fav = False
        return render(request, 'org-detail-desc.html', {'org_temp':org,
                                                        'currentpage':currentpage,
                                                        'is_fav':is_fav,
                                                    })


class OrgTeachers(View):
    def get(self,request,org_id,page):
        currentpage = 'OrgTeacher'
        org = get_object_or_404(CourseOrg,id=org_id)
        #获取机构下所有老师,分页显示
        org_teachers_list = org.teacher_set.all()
        teacher_p = Paginator(org_teachers_list,1)
        try:
            p = teacher_p.page(page)
        except (PageNotAnInteger, EmptyPage):
            p = teacher_p.page(1)
        if request.user.is_authenticated():
            try:
                is_record = UserFavorite.objects.get(user=request.user, fav_id=org.id, fav_type=1)
            except (UserFavorite.DoesNotExist, UserFavorite.MultipleObjectsReturned):
                is_record = ''
            if is_record:
                is_fav = True
            else:
                is_fav = False
        else:
            is_fav = False
        return render(request, 'org-detail-teachers.html', {'org_temp':org,
                                                            'currentpage':currentpage,
                                                            'per_page':p,
                                                            'is_fav':is_fav,
                                                        })


class AddFav(View):
    def post(self, request):
        if request.user.is_authenticated():
            fav_id = request.POST.get("fav_id", -1)
            fav_type = request.POST.get("fav_type", -1)
            try:
                is_record = UserFavorite.objects.get(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
            except (UserFavorite.DoesNotExist, UserFavorite.MultipleObjectsReturned):
                is_record = ''
            if is_record:
                is_record.delete()
                return HttpResponse(json.dumps({'status':'fail','msg':"收藏"}),content_type='application/json')
            else:
                user_tmep = UserFavorite()
                user_tmep.user = request.user
                user_tmep.fav_type = int(fav_type)
                user_tmep.fav_id = int(fav_id)
                user_tmep.save()
                return HttpResponse(json.dumps({'status':'success', 'msg':'已收藏'}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'status':'fail', 'msg':'用户未登录'}), content_type='application/json')


class TeacherList(View):
    def get(self, request):
        getsort = request.GET.get('sort',"all")
        if getsort == "hot":
            renqi = "hot"
            teacher_list = Teacher.objects.all().order_by("-click_nums")
        else:
            renqi = "all"
            teacher_list = Teacher.objects.all()
        try:
            page = request.GET.get("page", 1)
        except (EmptyPage, PageNotAnInteger):
            page = 1
        p = Paginator(teacher_list, 1, request=request)
        teachers = p.page(page)

        return render(request, 'teachers-list.html', {
            'teachers':teachers,
            'teahcernumber':teacher_list.count(),
            'renqi':renqi,
            'teachersort':Teacher.objects.order_by("-click_nums")[0:3],
        })


class TeacherDetailList(View):
    def get(self, request, teacherid):
        try:
            teacher = Teacher.objects.get(id=int(teacherid))
        except (Teacher.DoesNotExist, Teacher.MultipleObjectsReturned):
            return HttpResponse("page not found")
        teacher_all_course = Course.objects.filter(teacher=teacher)
        try:
            page = request.GET.get("page", 1)
        except (PageNotAnInteger, EmptyPage):
            page = 1
        p = Paginator(teacher_all_course, 2 ,request=request)
        teachercourses = p.page(page)
        return render(request, 'teacher-detail.html', {
            "teacher":teacher,
            "teachercourses":teachercourses,
        })
