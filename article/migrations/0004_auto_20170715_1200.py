# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-15 06:30
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20170715_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='picture',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='article/media/photos'), upload_to=''),
        ),
    ]
