# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from bbs.models import UserProfile
# Create your models here.

class QQGroup(models.Model):
    name = models.CharField(max_length=64,unique=True)
    description = models.CharField(max_length=255,default="nothing..")
    members = models.ManyToManyField(UserProfile,blank=True)
    admin = models.ManyToManyField(UserProfile,related_name='Group_Admin')
    max_member_nums = models.IntegerField(default=200)
    def __unicode__(self):
        return self.name



class MyUser(models.Model):
    username = models.CharField(max_length=22)
    password = models.CharField(max_length=33)
    def __unicode__(self):
        return self.username

class News(models.Model):
    title = models.CharField(max_length=22)
    content = models.CharField(max_length=33)
    def __unicode__(self):
        return self.title

class Favor(models.Model):
    user_obj = models.ForeignKey(MyUser)
    new_obj = models.ForeignKey(News)
    def __unicode__(self):
        return "%s--->%s"%(self.user_obj.username,self.new_obj.title)
