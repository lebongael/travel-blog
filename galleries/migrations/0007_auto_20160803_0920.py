# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-03 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0006_auto_20160802_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='base_height',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AddField(
            model_name='photo',
            name='base_width',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Titre de la Galerie'),
        ),
    ]
