# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_places_url_property'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iternary',
            name='duration',
            field=models.CharField(max_length=256),
        ),
    ]
