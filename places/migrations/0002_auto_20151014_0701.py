# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'placeimages/%Y/%m/%d/%H/%M/%S/')),
            ],
        ),
        migrations.AddField(
            model_name='places',
            name='activity',
            field=tinymce.models.HTMLField(default=datetime.datetime(2015, 10, 14, 7, 1, 23, 539275, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='placeimages',
            name='place',
            field=models.ForeignKey(to='places.Places'),
        ),
    ]
