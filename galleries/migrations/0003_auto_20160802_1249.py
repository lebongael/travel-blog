# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 10:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0002_gallery_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Gallerie', 'verbose_name_plural': 'Galleries'},
        ),
        migrations.AddField(
            model_name='gallery',
            name='date',
            field=models.DateField(default=datetime.date(2016, 8, 2), verbose_name='Date'),
        ),
    ]
