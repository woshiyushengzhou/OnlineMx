# _*_ encoding:utf8 _*_
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.db.models import Q

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from course.models import Course
from operation.models import UserFavorite, CourseComments

import json

class CourseList(View):
    def get(self, request):
        sort = request.GET.get('sort', 'hot')
        hot_course = Course.objects.filter().order_by("-click_nums")[0:3]
        if sort=='new':
            all_course = Course.objects.all().order_by('-add_time')
        elif sort=='hot':
            all_course = Course.objects.all().order_by('-click_nums')
        elif sort=='student':
            all_course =  Course.objects.all().order_by('-students')
        else:
            all_course = Course.objects.all().order_by('-add_time')
        keyword = request.GET.get('keywords', "")
        if keyword:
            all_course = all_course.filter(Q(courseName__icontains=keyword)|Q(courseIntroduction__icontains=keyword))
        p_temp = Paginator(all_course,3, request=self.request)
        try:
            p = p_temp.page(request.GET.get('page', ''))
        except (PageNotAnInteger, EmptyPage):
            p = p_temp.page(1)

        return render(request, "course-list.html", {
            'all_course':p,
            'sort':sort,
            'hot_course':hot_course,
        })


class CourseDetail(View):
    def get(self, request, course_id):
        left_has_fav = False
        right_has_fav = False
        if request.user.is_authenticated():
            try:
                left = UserFavorite.objects.get(user=request.user, fav_id=course_id, fav_type=3)
            except (UserFavorite.DoesNotExist, UserFavorite.MultipleObjectsReturned):
                left = ""
            try:
                temp = Course.objects.get(id=course_id)
                right = UserFavorite.objects.get(user=request.user, fav_id=temp.course_org.id, fav_type=1)
            except (UserFavorite.DoesNotExist, UserFavorite.MultipleObjectsReturned):
                right = ""
        else:
            left = ""
            right = ""
        left_has_fav = True if left else False
        right_has_fav = True if right else False
        try:
            course_temp = Course.objects.get(id=course_id)
        except (Course.DoesNotExist, Course.MultipleObjectsReturned):
            return HttpResponse("404")
        return render(request, "course-detail.html", {
            "course":course_temp,
            "left_has_fav":left_has_fav,
            "right_has_fav":right_has_fav,
        })


class CourseViedo(View):
    def get(self, request, course_id):
        try:
            course_temp = Course.objects.get(id=course_id)
        except (Course.DoesNotExist, Course.MultipleObjectsReturned):
            return HttpResponse("404")
        return render(request, "course-video.html", {
            'course_temp':course_temp,
        })

class CourseComment(View):
    def get(self, request):
        try:
            course_id = request.GET.get("course_id")
        except:
            return HttpResponse("404")
        try:
            course_temp = Course.objects.get(id=course_id)
        except (Course.DoesNotExist, Course.MultipleObjectsReturned):
            return HttpResponse("404")
        all_comment = CourseComments.objects.filter(course=course_temp)
        return render(request, "course-comment.html", {
            "course_temp":course_temp,
            "all_comment":all_comment,
        })

    def post(self, request):
        if request.user.is_authenticated():
            try:
                course_id = request.POST.get("course_id")
            except:
                return HttpResponse("404")
            try:
                course_temp = Course.objects.get(id=int(course_id))
            except (Course.DoesNotExist, Course.MultipleObjectsReturned):
                return HttpResponse("404")
            user_comment = CourseComments()
            user_comment.user =  request.user
            user_comment.course = course_temp
            user_comment.comment_message = request.POST.get("comments")
            user_comment.save()
            return HttpResponse(json.dumps({'status':'success'}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'status':'fail','msg':"用户未登录"}), content_type='application/json')