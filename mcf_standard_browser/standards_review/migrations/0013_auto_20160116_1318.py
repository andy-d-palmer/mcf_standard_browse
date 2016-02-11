# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-16 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standards_review', '0012_auto_20160116_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='standard',
            name='datasets_present_in',
        ),
        migrations.AddField(
            model_name='dataset',
            name='adducts_present',
            field=models.ManyToManyField(to='standards_review.Adduct'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='standards_present',
            field=models.ManyToManyField(blank=True, null=True, to='standards_review.Standard'),
        ),
    ]
