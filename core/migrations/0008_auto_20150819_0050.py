# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import re
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_userquestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z', 32), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')], max_length=30),
        ),
    ]
