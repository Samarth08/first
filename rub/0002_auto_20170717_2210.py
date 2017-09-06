# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-17 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contribute', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='full_name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='email',
        ),
        migrations.AddField(
            model_name='signup',
            name='body',
            field=models.CharField(blank=True, max_length=1200, null=True),
        ),
    ]
