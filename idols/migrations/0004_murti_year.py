# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2017-06-04 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idols', '0003_auto_20160726_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='murti',
            name='year',
            field=models.IntegerField(choices=[('2017', '2017')], default=2017),
        ),
    ]