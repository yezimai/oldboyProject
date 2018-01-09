# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(related_name='_userprofile_friends_+', to='bbs.UserProfile'),
        ),
        migrations.AlterField(
            model_name='article',
            name='head_img',
            field=models.ImageField(upload_to='upload/'),
        ),
    ]
