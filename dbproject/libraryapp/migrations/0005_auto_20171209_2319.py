# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 23:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0004_auto_20171209_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Writes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.Author')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='writes',
            name='bookId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.Book'),
        ),
    ]
