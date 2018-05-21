from django.shortcuts import render
from django.views.generic import View,ListView

from organization.models import CityDict,CourseOrg
# Create your views here.
class OrgView(ListView):
    # model = CourseOrg
    def get(self,request):
        all_city = CityDict.objects.all()
        obj_list = CourseOrg.objects.all()
        return render(request,"org-list.html",{"all_city":all_city,"obj_list":obj_list})
