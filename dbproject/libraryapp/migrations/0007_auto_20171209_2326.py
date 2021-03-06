# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 23:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0006_auto_20171209_2324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='copy',
            old_name='docId',
            new_name='doc',
        ),
        migrations.RenameField(
            model_name='copy',
            old_name='libId',
            new_name='lib',
        ),
        migrations.RenameField(
            model_name='journalissue',
            old_name='volId',
            new_name='vol',
        ),
        migrations.RenameField(
            model_name='writes',
            old_name='authorId',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='writes',
            old_name='bookId',
            new_name='book',
        ),
        migrations.AlterUniqueTogether(
            name='writes',
            unique_together=set([('author', 'book')]),
        ),
    ]
