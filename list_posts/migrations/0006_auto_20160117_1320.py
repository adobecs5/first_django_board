# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 13:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('list_posts', '0005_auto_20160116_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 17, 13, 20, 40, 487062, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 17, 13, 20, 47, 707038, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
