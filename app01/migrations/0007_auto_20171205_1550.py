# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 07:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20171205_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='_type',
            new_name='person_type',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='_class',
            new_name='student_class',
        ),
    ]
