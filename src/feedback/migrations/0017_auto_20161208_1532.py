# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-08 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0016_merge_20161208_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='name',
        ),
        migrations.AddField(
            model_name='log',
            name='veranstaltung',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feedback.Veranstaltung'),
        ),
    ]
