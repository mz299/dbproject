# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 21:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0008_auto_20171210_0418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bortransaction',
            old_name='copyNo',
            new_name='copy',
        ),
        migrations.RenameField(
            model_name='bortransaction',
            old_name='readerId',
            new_name='reader',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='copyNo',
            new_name='copy',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='readerId',
            new_name='reader',
        ),
    ]
