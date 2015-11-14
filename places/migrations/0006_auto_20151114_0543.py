# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20151114_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='meta_description',
            field=models.CharField(default=1, unique=True, max_length=160),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='places',
            name='meta_keywords',
            field=models.CharField(default=1, unique=True, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='places',
            name='meta_title',
            field=models.CharField(default=1, unique=True, max_length=60),
            preserve_default=False,
        ),
    ]
