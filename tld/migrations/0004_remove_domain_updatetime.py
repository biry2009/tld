# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-24 07:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tld', '0003_auto_20180224_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domain',
            name='updatetime',
        ),
    ]
