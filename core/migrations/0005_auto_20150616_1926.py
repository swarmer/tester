# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_question_index'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['index']},
        ),
    ]
