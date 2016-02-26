# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-16 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standards_review', '0006_fragmentationspectrum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adduct',
            name='datasets_present_in',
            field=models.ManyToManyField(blank=True, null=True, to='standards_review.Dataset'),
        ),
    ]