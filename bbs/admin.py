# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
from web_chat import models as MODELS
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id",'name')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','publish_date')

admin.site.register(models.Article,ArticleAdmin)
admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Comment)
admin.site.register(models.ThumbUp)
admin.site.register(models.UserGroup)
admin.site.register(models.UserProfile)
admin.site.register(MODELS.MyUser)
admin.site.register(MODELS.News)
admin.site.register(MODELS.Favor)
