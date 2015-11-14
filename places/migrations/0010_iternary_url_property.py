# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_auto_20151114_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='iternary',
            name='url_property',
            field=models.CharField(default=1, max_length=512),
        ),
    ]
