# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150819_0050'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='test',
            unique_together=set([('owner', 'name')]),
        ),
    ]
