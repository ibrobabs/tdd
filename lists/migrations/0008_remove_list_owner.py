# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 17:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0007_list_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='owner',
        ),
    ]