# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-10 21:05
from __future__ import unicode_literals

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20171010_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='url',
            field=models.CharField(max_length=220, validators=[shortener.validators.validate_url, shortener.validators.validate_dot_com]),
        ),
    ]
