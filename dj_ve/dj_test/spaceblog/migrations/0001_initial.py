# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='SpaceTitle')),
                ('text', models.TextField(verbose_name='SpaceText')),
                ('create_date', models.DateTimeField(verbose_name='SpaceTime Sol#')),
            ],
        ),
    ]
