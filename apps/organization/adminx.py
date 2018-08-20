import xadmin

from organization.models import CityDict,CourseOrg,Teacher

class CityDictAdmin(object):
    list_display = ['name','desc']
    search_fields = ['name','desc']
    list_filter = ['name','desc','add_time']

class CourseOrgAdmin(object):
    list_display = ['name','desc','click_nums','fav_nums','image','address','city','category']
    search_fields = ['name','desc','click_nums','fav_nums','image','address','city','category']
    list_filter = ['name','desc','click_nums','fav_nums','image','address','city','add_time','category']

class TeacherAdmin(object):
    list_display = ['teacher_org','name','work_years','work_company','position','points','click_nums','fav_nums']
    search_fields = ['teacher_org','name','work_years','work_company','position','points','click_nums','fav_nums']
    list_filter = ['teacher_org','name','work_years','work_company','position','points','click_nums','fav_nums','add_time']


xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)