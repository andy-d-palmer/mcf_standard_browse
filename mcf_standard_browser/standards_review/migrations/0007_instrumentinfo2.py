# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-14 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standards_review', '0006_instrumentinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstrumentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='dataset',
            name='instrument_info',
            field=models.ManyToManyField(to='standards_review.InstrumentInfo'),
        ),
    ]
