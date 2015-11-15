# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0012_iternary_main_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='themes',
            name='iternaries',
            field=models.ManyToManyField(to='places.Iternary'),
        ),
        migrations.AddField(
            model_name='themes',
            name='url_property',
            field=models.CharField(default=1, max_length=512),
        ),
        migrations.AlterField(
            model_name='themes',
            name='main_image',
            field=models.ImageField(default=b'None', upload_to=b'static/themes/%Y/%m/%d/%H/%M/%S/'),
        ),
    ]
