# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 20:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Contact',
        ),
    ]
