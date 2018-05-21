from django.contrib.auth.models import AbstractUser
import xadmin

from users.models import UserPorfile,EmailVerifyRecord,Banner


class UserPorfileAdmin(object):
    list_display = ['username','nickname','barth_day','gender','address','phone_num','head_portrait']
    search_fields = ['username','gender','phone_num']
    list_filter = ['username','nickname','barth_day','gender','address','phone_num','head_portrait']

class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type']
    search_fields = ['code','email','send_type']
    list_filter = ['code','email','send_type','send_time']

class BannerAdmin(object):
    list_display = ['title','image','url','index']
    search_fields  = ['title','image','url','index']
    list_filter = ['title','image','url','index','add_time']

xadmin.site.unregister(UserPorfile)
xadmin.site.register(UserPorfile,UserPorfileAdmin)
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)