# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-28 06:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20170716_1548'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cost',
        ),
    ]