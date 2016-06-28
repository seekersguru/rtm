# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0016_remove_sliderimages_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliderimages',
            name='text',
            field=models.CharField(default=b'', max_length=100, null=True, blank=True),
        ),
    ]
