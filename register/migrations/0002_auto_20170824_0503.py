# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='microservice',
            name='id',
        ),
        migrations.AlterField(
            model_name='microservice',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
