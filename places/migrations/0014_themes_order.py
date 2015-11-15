# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0013_auto_20151115_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='themes',
            name='order',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
