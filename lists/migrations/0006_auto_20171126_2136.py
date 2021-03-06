# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_list_item_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('id',)},
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([('list', 'text')]),
        ),
    ]
