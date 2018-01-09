# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from forms import ArticleForm,handle_upload_file
import json
# Create your views here.
import models
from web_chat import models as Models
import custom_comments,techer

def index(request):
    #print('HHHH',request.GET.items())
    articles = models.Article.objects.all()
    return render(request,'index.html',{'articles':articles})

def category(request,category_id):
    print category_id

    articles = models.Article.objects.filter(category_id=category_id)
    return render(request,'index.html',{'articles':articles})

def test(request):
    # new_list = Models.News.objects.all()
    new = Models.Favor.objects.filter(user_obj__username='jiang')
    for i in new:
        print i.new_obj.title

    # for i in new_list:
    #     print i.title
    #     print
    #     print i.favor_set.all().count()

    return HttpResponse('ok')


def articl_detail(request,articl_detail_id):
    try:
        print('HHHH', request.GET.items())
        articles = models.Article.objects.get(id=articl_detail_id)
        return render(request,'article_detail.html',{'articles':articles})
    except ObjectDoesNotExist as e:
        return render(request,'404.html',{'error_msg':"not exits"})

def acc_logout(request):
    print('/////',request.session)
    logout(request)
    return HttpResponseRedirect('/')

def acc_login(request):
    if request.method == 'POST':
        print(request.POST)
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            print('hehehe',user,type(user))
            #pass authentication
            login(request,user)  #这个才是真正登录生成session
            return HttpResponseRedirect(request.GET.get('next') or '/')
        else:
            login_err = "Wrong username or password!"
            return render(request,'login.html',{'login_err':login_err})
    return render(request,'login.html')


def new_article(request):
    if request.method == "POST":
        print request.POST
        # print request.POST,request.FILES,type(request.FILES)
        # print request.FILES['head_img'].name,type(request.FILES['head_img'].name)
        # print "----->>>",request.FILES['head_img'],type(request.FILES['head_img'])
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            print ("----clean data",form.cleaned_data)
            form_data = form.cleaned_data
            form_data['author_id'] = request.user.userprofile.id
            form_img_path = handle_upload_file(request,request.FILES['head_img'])
            form_data['head_img'] = form_img_path
            #print ('!!!!!!!!',request.user.userprofile.id)
            new_article_obj = models.Article(**form_data)
            new_article_obj.save()
            return render(request,'new_article.html',{'new_article_obj':new_article_obj})

        else:

            print form.errors
            return render(request,'404.html')



    category_list = models.Category.objects.all()
    return render(request,'new_article.html',{'category_list':category_list})

##自定义分页

def user_list(request):
    # for i in range(100):
    #     temp={'user_name':'james %s'%i,'age':i}
    # # models.user_list.objects.all().delete()
    #     models.user_list.objects.create(**temp)
    PAGE = request.GET.get('page',1)
    print models.user_list.objects.count()
    print PAGE
    start = (int(PAGE)-1)*10
    end = int(PAGE)*10
    Userlist=models.user_list.objects.all()[start:end]
    return render(request,'user_list.html',{'user_list':Userlist})

def post_comment(request):
    # print(request.POST)
    if request.method == 'POST':
        new_comment_obj = models.Comment(
            article_id = request.POST.get('article_id'),
            user_id = request.user.userprofile.id,
            comment = request.POST.get('comment')
        )
        new_comment_obj.save()

    return HttpResponse('009')
def get_comments(request,articles_id):
    articles = models.Article.objects.get(id=articles_id)
    comments_list = articles.comment_set.select_related().order_by('-date')
    # print comments_list
    # comments = custom_comments.content_tag(comments_list)
    comment_tree = techer.build_tree(comments_list)
    comments = techer.render_comment_tree(comment_tree)
    # print comments
    return HttpResponse(comments)
#
# def get_latest_article_count(request):
#     latest_article_id = request.GET.get('latest_id')
#     new_article_count = models.Article.objects.filter(id__gt = latest_article_id).count()
#     print('new_ article count',new_article_count)
#     return HttpResponse(json.dumps({'new_article_count':new_article_count}))