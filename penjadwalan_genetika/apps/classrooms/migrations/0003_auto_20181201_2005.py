# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-01 13:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0002_classroom_is_active'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='classroom',
            unique_together=set([('name',)]),
        ),
    ]
