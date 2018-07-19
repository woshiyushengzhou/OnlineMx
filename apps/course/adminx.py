# _*_ encoding:utf-8 _*_
import xadmin
from xadmin import views

from course.models import Course,Chapter,Viedo,CourseResource


class CourseAdmin(object):
    list_display = ['courseName','courseIntroduction','courseDegree','courseTime','students','category','click_nums','courseCover','collect_nums']
    search_fields = ['courseName','courseIntroduction','courseDegree','courseTime','students','category','click_nums','courseCover','collect_nums']
    list_filter = ['courseName','courseIntroduction','courseDegree','courseTime','students','category','click_nums','courseCover','collect_nums','add_time']


class ChapterAdmin(object):
    list_display = ['name','course']
    search_fields = ['name','course']
    list_filter = ['name','course','add_time']


class ViedoAdmin(object):
    list_display = ['name','chapter']
    search_fields = ['name','chapter']
    list_filter = ['name','chapter','add_time']


class CourseResourceAdmin(object):
    list_display = ['course','name','download']
    search_fields = ['course','name','download']
    list_filter = ['course','name','download','add_time']


class GlobalSettings(object):
    #修改左上角Django Xadmin 网站主题
    site_title = u"菜鸟在线教育网"
    #修改底部页脚
    site_footer = u"菜鸟信息科技"
    #左侧app收起来
    menu_style = "accordion"


class BaseSettings(object):
    enable_themes = True
    # use_bootswatch = True



xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Chapter,ChapterAdmin)
xadmin.site.register(Viedo,ViedoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)


#注册 页脚 网站主题
xadmin.site.register(views.CommAdminView,GlobalSettings)

#网站页面主题风格，
xadmin.site.register(views.BaseAdminView,BaseSettings)