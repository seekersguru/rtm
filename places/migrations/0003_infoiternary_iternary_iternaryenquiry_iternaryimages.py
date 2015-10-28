# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20151014_0701'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoIternary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_person', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=512)),
                ('website', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Iternary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('duration', models.IntegerField()),
                ('price', models.IntegerField()),
                ('overview', tinymce.models.HTMLField()),
                ('pricing_and_schedule', tinymce.models.HTMLField()),
                ('iternary', tinymce.models.HTMLField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='IternaryEnquiry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=512)),
                ('mobile', models.IntegerField()),
                ('date', models.DateField()),
                ('subject', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='IternaryImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'placeimages/%Y/%m/%d/%H/%M/%S/')),
                ('iternary', models.ForeignKey(to='places.Iternary')),
            ],
        ),
    ]
