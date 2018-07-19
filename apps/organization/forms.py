# _*_ encoding:utf8 _*_
__author__ = 'sz.yu'

from django import forms

import re
from operation.models import UserAsk

# class UserAskForm(forms.Form):
#     name = forms.CharField(required=True,min_length=2,max_length=20)
#     mobile = forms.CharField(required=True,max_length=11,min_length=11)
#     course_name = forms.CharField(required=True,min_length=2,max_length=50)

phone_number = re.compile(r'^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        exclude = ["add_time"]
    def clean_mobile(self):
        if re.match(phone_number,self.cleaned_data['mobile']):
            return self.cleaned_data['mobile']
        else:
            raise forms.ValidationError(u"手机号格式错误")
