# -*- coding:utf-8 -*-
from django.utils.safestring import  mark_safe


def tree_search(d_dic,comment_obj):
     for k,v in d_dic.items():
         if  k == comment_obj.parent_comment:
             d_dic[k][comment_obj] = {}
             return
         else:
             tree_search(d_dic[k],comment_obj)

def subcomment(sub_comment,margin_left_val):
    html = ""

    for k,v in sub_comment.items():
        html += ("<div style=margin-left:%spx class='comment-node'>")%margin_left_val + k.comment+"<span style='margin-left:30px'>" +k.user.name+ "</span></div>"
        if v:
            html += subcomment(v,margin_left_val+15)
    return html

def content_tag(commnet_list):
    # print("comment_list",commnet_list)
    comment_dic = {}
    for comment_obj in commnet_list:
        print('000000',comment_obj)
        # print comment_obj.parent_comment
        if comment_obj.parent_comment is None:
            comment_dic[comment_obj]={}
        else:
            tree_search(comment_dic,comment_obj)

    html = "<div class='comment-class'>"
    for k,v in comment_dic.items():
        print('------->',comment_dic)
        # print k,v
        margin_left_val = 0
        html += "<div class='comment-node'>" + k.comment + "<span class='pull-right'>"+k.user.name+"</span></div>"
        html += subcomment(v,margin_left_val+10)
    html +="</div>"
    #print html,type(html)


    return mark_safe(html)