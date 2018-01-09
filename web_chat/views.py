# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json,os
from django.shortcuts import render,HttpResponse
import models
# Create your views here.
from django.contrib.auth.decorators import login_required
import Queue,time
from django.core.cache import cache
GLOBAL_MQ={}

@login_required
def dashboard(request):
    return render(request,'web_chat/dash_board.html')

@login_required
def load_contact_list(request):
    ContactDic={}
    contacts = request.user.userprofile.friends.select_related().values('id','name')
    contacts = list(contacts)
    groups = request.user.userprofile.qqgroup_set.select_related().values('id','name','max_member_nums')
    groups = list(groups)
    ContactDic['single_contact'] = contacts
    ContactDic['group_contact'] = groups
    return HttpResponse(json.dumps(ContactDic))

@login_required
def send_msg(request):
    if request.method=="POST":                  #如果是发送消息
        print(request.POST.get('data'))
        data = json.loads(request.POST.get('data'))
        contact_type = data["contact_type"]
        print('????',contact_type)
        data['timestamp'] = time.strftime("%H:%M:%S", time.localtime())
        if contact_type == "group_contact":   #data格式为{u'msg': u'\u5bf9\u65b9\u7b54\u590d', u'to': u'1', u'from_name': u'YEYE', u'from': u'1', u'contact_type': u'group_contact'}
            group_id = int(data["to"])
            print('grrrrrrpid',group_id)
            msg_from = data["from"]
            group_obj = models.QQGroup.objects.get(id=group_id)

            for member in group_obj.members.select_related():

                if str(member.id) not in GLOBAL_MQ:
                    GLOBAL_MQ[str(member.id)] = Queue.Queue()
                if str(member.id) != msg_from:
                    GLOBAL_MQ[str(member.id)].put(data)
            #return HttpResponse('0')

        else:
            send_to = data['to']
            if send_to not in GLOBAL_MQ:
                GLOBAL_MQ[send_to] = Queue.Queue()

            #data['timestamp'] = time.strftime("%H:%M:%S",time.localtime())     #按照用户可以读的格式来显示时间
            GLOBAL_MQ[send_to].put(data)
        return HttpResponse('0')
    else:
        request_id = str(request.user.userprofile.id)
        msg_list=[]
        if request_id in GLOBAL_MQ:
            print "NEWNEWNEW..."
            if GLOBAL_MQ[request_id].qsize() == 0:
                try:    #这里如果超时后会有一个报错，所以用try
                    print("no more msg,wait 15s...............")
                    msg_list.append(GLOBAL_MQ[request_id].get(timeout=15))      #queue的get方法自带一种阻塞时
                except Exception as e:
                    print("err:",e)
                    print "timeout!!!!!"
            for i in range(GLOBAL_MQ[request_id].qsize()):
                msg_list.append(GLOBAL_MQ[request_id].get())


        else: #如果队列里没有这个queue就建立一个
            GLOBAL_MQ[request_id]=Queue.Queue()
        return HttpResponse(json.dumps(msg_list))
def file_upload(request):
    #print(request.FILES)
    file_obj = request.FILES.get('file') #获取文件
    new_file_dir = 'upload/%s'%(request.user.userprofile.id)
    if not os.path.isdir(new_file_dir):
        os.mkdir(new_file_dir)
    new_file_name = '%s/%s'%(new_file_dir,file_obj.name)
    recv_size = 0
    with open(new_file_name,'wb') as new_file_obj:
        for chunk in file_obj.chunks():
            new_file_obj.write(chunk)
            recv_size += len(chunk)
            cache.set(file_obj.name,recv_size)

    return HttpResponse('---upload success--')

def file_upload_progess(request):
    filename = request.GET.get('filename')
    progess = cache.get(filename)
    print("file[%s] uploading progress [%s]"%(filename,progess))
    return HttpResponse(json.dumps({"recv_size":progess}))

def DelFileCache(request):
    cache_name=request.GET.get('cache_name')
    cache.delete(cache_name)
    return HttpResponse("cache delete")