# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_vtuurl_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vtuurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]