# -*- coding:utf-8 -*-
from django import forms
import os,models
from django.core.exceptions import ValidationError

def Article_validate(value):
    print('\033[40;1m----passed the permission--\033[0m')

    if not models.Article.objects.filter(title=value):
        raise ValidationError('标题已存在')


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=20,min_length=2,error_messages={'required':'标题不能为空','min_length': u'标题最少为2个字符','max_length': u'标题最多为20个字符'})
    content = forms.CharField(min_length=10)
    head_img = forms.ImageField(error_messages={'required':u'不能为空'})
    category_id = forms.CharField()


def handle_upload_file(request,f):#自定义上传的目录
    base_img_upload_path = 'statics/imgs'
    users_path = "%s/%s" %(base_img_upload_path,request.user.userprofile.id)
    if not os.path.exists(users_path):
        os.mkdir(users_path)
    with open('%s/%s' %(users_path,f.name),'wb+') as DEST:   #建立并打开一个以上传文件名加文件路径的文件
        for chunk in f.chunks():                             #chunks方法，就是把文件分块的写入到已经打开的目录中
            DEST.write(chunk)
    Front_path = '/static/imgs/%s/%s' %(request.user.userprofile.id,f.name)
    print "aaaaaaaaaaaa",Front_path
    return Front_path