# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_iternary_introduction'),
    ]

    operations = [
        migrations.AddField(
            model_name='iternary',
            name='main_image',
            field=models.ImageField(default='', upload_to=b'static/iternaryimage/%Y/%m/%d/%H/%M/%S/'),
            preserve_default=False,
        ),
    ]
