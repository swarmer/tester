# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150616_1926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='is_public',
            new_name='is_listed',
        ),
    ]
