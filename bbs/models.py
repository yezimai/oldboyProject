# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models




# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255,unique=True)
    category = models.ForeignKey('Category')
    priority = models.IntegerField(default=1000)
    author = models.ForeignKey("UserProfile")
    content = models.TextField(max_length=100000)
    breif = models.TextField(max_length=512,default='none.....')
    head_img = models.ImageField(upload_to="upload/")
    publish_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey('Article')
    parent_comment = models.ForeignKey('Comment', blank=True, null=True, related_name='p_comment')
    user = models.ForeignKey('UserProfile')
    comment = models.TextField(max_length=1024)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.comment

class ThumbUp(models.Model):
    article = models.ForeignKey('Article')
    user = models.ForeignKey('UserProfile')

    def __unicode__(self):
        return self.user

class Category(models.Model): #板块
    name = models.CharField(max_length=64,unique=True)
    admin = models.ManyToManyField('UserProfile')

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    groups = models.ManyToManyField('UserGroup')
    friends = models.ManyToManyField('self',related_name='my_friends')

    def __unicode__(self):
        return self.name

###########一对多的实验题
class UserGroup(models.Model):
    name = models.CharField(max_length=64,unique=True)

    def __unicode__(self):
        return self.name

################################分页功能

class user_list(models.Model):
    user_name=models.CharField(max_length=22)
    age=models.IntegerField()