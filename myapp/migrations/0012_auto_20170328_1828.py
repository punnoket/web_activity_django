# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-28 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20170315_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='user',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
