# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0015_auto_20160422_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sliderimages',
            name='text',
        ),
    ]
