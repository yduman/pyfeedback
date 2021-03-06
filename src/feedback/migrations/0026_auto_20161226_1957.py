# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 19:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0025_auto_20161226_1924'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fachgebiet',
            options={'verbose_name': 'Fachgebiet', 'verbose_name_plural': 'Fachgebiete'},
        ),
        migrations.AlterModelOptions(
            name='fachgebietemail',
            options={'verbose_name': 'Fachgebiet Email', 'verbose_name_plural': 'Fachgebiet Emails'},
        ),
        migrations.AlterField(
            model_name='fachgebiet',
            name='name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='fachgebietemail',
            name='email_sekretaerin',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='fachgebietemail',
            name='suffix',
            field=models.EmailField(default='fachgebiet@', help_text='Vor dem @-Symbol kann beliebiges stehen. Wichtig ist nur der Domainname dahinter.', max_length=254),
        ),
        migrations.AlterField(
            model_name='person',
            name='fachgebiet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.Fachgebiet'),
        ),
    ]
