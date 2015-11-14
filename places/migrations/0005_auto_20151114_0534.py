# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_places_main_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Themes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('introduction', tinymce.models.HTMLField()),
                ('main_image', models.ImageField(default=b'None', upload_to=b'static/placehome/%Y/%m/%d/%H/%M/%S/')),
            ],
        ),
        migrations.AddField(
            model_name='iternary',
            name='meta_description',
            field=models.CharField(default=1, unique=True, max_length=160),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iternary',
            name='meta_keywords',
            field=models.CharField(default=1, unique=True, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iternary',
            name='meta_title',
            field=models.CharField(default=1, unique=True, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iternary',
            name='place',
            field=models.ForeignKey(default=1, to='places.Places'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='iternaryimages',
            name='image',
            field=models.ImageField(upload_to=b'static/placeimages/%Y/%m/%d/%H/%M/%S/'),
        ),
        migrations.AlterField(
            model_name='placeimages',
            name='image',
            field=models.ImageField(upload_to=b'static/placeimages/%Y/%m/%d/%H/%M/%S/'),
        ),
        migrations.AlterField(
            model_name='places',
            name='main_image',
            field=models.ImageField(default=b'None', upload_to=b'static/placehome/%Y/%m/%d/%H/%M/%S/'),
        ),
    ]
