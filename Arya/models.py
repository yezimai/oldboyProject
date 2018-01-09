# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Host(models.Model):
    hostname = models.CharField(max_length=64,unique=True)
    key = models.TextField()
    status_choices =((0,'Waiting'),
                     (1,'Accepted'),
                     (2,'Rejected'))
    status = models.SmallIntegerField(choices=status_choices,default=0)
    os_type_chioces = (
        ('redhat','Redhat\CentOS'),
        ('ubuntu','Ubuntu'),
        ('suse','Suse'),
        ('windows','Windows'),
                       )
    os_type = models.CharField(max_length=32,choices=os_type_chioces,default='redhat')

    def __str__(self):
        return self.hostname

class Group(models.Model):
    name = models.CharField(max_length=64,unique=True)
    hosts = models.ManyToManyField(Host,blank=True)

    def __str__(self):
        return self.name