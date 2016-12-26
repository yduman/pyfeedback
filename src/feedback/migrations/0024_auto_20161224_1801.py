# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0023_auto_20161224_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSuffix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_suffix', models.CharField(max_length=50)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person', to='feedback.Person')),
            ],
        ),
        migrations.RemoveField(
            model_name='emailendung',
            name='fachgebiet',
        ),
        migrations.RemoveField(
            model_name='emailendung',
            name='person',
        ),
        migrations.RemoveField(
            model_name='emailsekretaerin',
            name='fachgebiet',
        ),
        migrations.AddField(
            model_name='fachgebiet',
            name='email_sek',
            field=models.ManyToManyField(blank=True, to='feedback.EmailSekretaerin'),
        ),
        migrations.DeleteModel(
            name='EmailEndung',
        ),
        migrations.AddField(
            model_name='fachgebiet',
            name='email_suffix',
            field=models.ManyToManyField(to='feedback.EmailSuffix'),
        ),
    ]
