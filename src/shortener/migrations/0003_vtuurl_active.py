# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20161122_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='vtuurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
