# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150615_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='index',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]
