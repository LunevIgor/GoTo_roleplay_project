# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp1', '0005_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
