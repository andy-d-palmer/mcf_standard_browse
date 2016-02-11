# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-12 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standards_review', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
            ],
        ),
        migrations.AddField(
            model_name='standard',
            name='datasets_present_in',
            field=models.ManyToManyField(to='standards_review.Dataset'),
        ),
    ]
