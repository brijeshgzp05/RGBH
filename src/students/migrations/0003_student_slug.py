# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-30 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20180930_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]