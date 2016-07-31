# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import re
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150821_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='test',
            name='description',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z', 32), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')]),
        ),
    ]
