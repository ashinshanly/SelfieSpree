# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-26 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_userprofile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(default=b'', max_length=1000),
        ),
    ]
