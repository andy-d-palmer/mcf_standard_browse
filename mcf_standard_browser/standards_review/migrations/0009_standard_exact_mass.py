# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-16 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standards_review', '0008_auto_20160116_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='standard',
            name='exact_mass',
            field=models.FloatField(default=0.0),
        ),
    ]
