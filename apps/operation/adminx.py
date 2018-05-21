import xadmin

from operation.models import UserAsk,CourseComments,UserFavorite,UserMessage,UserCourse


class UserAskAdmin(object):
    list_display = ['name','mobile','course_name']
    search_fields = ['name','mobile','course_name']
    list_filter = ['name','mobile','course_name','add_time']

class CourseCommentsAdmin(object):
    list_display = ['user','course','comment_message']
    search_fields = ['user','course','comment_message']
    list_filter = ['user','course','comment_message','comment_time']

class UserFavoriteAdmin(object):
    list_display = ['user','fav_id','fav_type']
    search_fields = ['user','fav_id','fav_type']
    list_filter = ['user','fav_id','fav_type','add_time']

class UserMessageAdmin(object):
    list_display = ['user','message','has_read']
    search_fields = ['user','message','has_read']
    list_filter = ['user','message','has_read','send_time']

class UserCourseAdmin(object):
    list_display = ['user','course']
    search_fields = ['user','course']
    list_filter = ['user','course','add_time']

xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)