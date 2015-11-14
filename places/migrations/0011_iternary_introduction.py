# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_iternary_url_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='iternary',
            name='introduction',
            field=tinymce.models.HTMLField(default='not val'),
            preserve_default=False,
        ),
    ]
