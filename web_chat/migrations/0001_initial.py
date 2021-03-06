# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bbs', '0002_auto_20170609_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='QQGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.CharField(default='nothing..', max_length=255)),
                ('max_member_nums', models.IntegerField(default=200)),
                ('admin', models.ManyToManyField(related_name='Group_Admin', to='bbs.UserProfile')),
                ('members', models.ManyToManyField(blank=True, related_name='QQ_Members', to='bbs.UserProfile')),
            ],
        ),
    ]
