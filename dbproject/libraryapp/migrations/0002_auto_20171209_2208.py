# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]