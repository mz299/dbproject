# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0010_auto_20171210_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bortransaction',
            name='retDate',
            field=models.DateField(null=True),
        ),
    ]
