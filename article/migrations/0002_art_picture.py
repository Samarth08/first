# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-14 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
