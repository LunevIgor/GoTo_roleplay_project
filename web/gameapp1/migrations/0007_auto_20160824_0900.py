# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 09:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp1', '0006_game_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='gameapp1.Game'),
        ),
    ]