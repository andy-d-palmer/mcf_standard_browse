# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-17 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standards_review', '0016_xic__rt'),
    ]

    operations = [
        migrations.AddField(
            model_name='fragmentationspectrum',
            name='rt',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fragmentationspectrum',
            name='spec_num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
