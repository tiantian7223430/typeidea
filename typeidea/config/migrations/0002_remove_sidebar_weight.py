# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-09 02:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sidebar',
            name='weight',
        ),
    ]
