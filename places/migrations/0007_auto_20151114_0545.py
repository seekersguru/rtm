# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20151114_0543'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='order',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='places',
            name='show',
            field=models.CharField(default=1, max_length=1),
        ),
    ]
