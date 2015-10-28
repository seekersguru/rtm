# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_infoiternary_iternary_iternaryenquiry_iternaryimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='main_image',
            field=models.ImageField(default=b'None', upload_to=b'placehome/%Y/%m/%d/%H/%M/%S/'),
        ),
    ]
