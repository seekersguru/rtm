# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0018_sitemap'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewverified',
            name='pics',
            field=models.ImageField(default=b'static/userimg/test-monail-img.jpg', upload_to=b'static/userimg/'),
        ),
    ]
