# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-24 07:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tld', '0002_auto_20180224_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cheapest',
            name='test',
        ),
        migrations.RemoveField(
            model_name='price',
            name='test',
        ),
    ]
