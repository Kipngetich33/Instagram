# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-03 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
