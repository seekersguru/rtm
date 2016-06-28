# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0014_themes_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestSelling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('order', models.IntegerField(unique=True, null=True, blank=True)),
                ('best', models.ForeignKey(to='places.Iternary')),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=512)),
                ('mobile', models.IntegerField()),
                ('date', models.DateField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GalleryImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'static/galary/')),
                ('place', models.ForeignKey(to='places.Iternary')),
            ],
        ),
        migrations.CreateModel(
            name='PlanMyTrip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=512)),
                ('to', models.CharField(max_length=128)),
                ('fr', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('mode_of_transport', models.CharField(max_length=128)),
                ('no_of_passenger', models.CharField(max_length=128)),
                ('discount_criteria', models.CharField(max_length=128)),
                ('mobile', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ReviewVerified',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('trip_name', models.CharField(max_length=128)),
                ('rating', models.CharField(max_length=128)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SliderImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'static/slider/')),
                ('text', models.CharField(default=b'', max_length=100, null=True, blank=True)),
                ('url_property', models.CharField(default=b'', max_length=150, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='VipAccess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=512)),
                ('mobile', models.IntegerField()),
                ('date', models.DateField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='iternaryenquiry',
            old_name='subject',
            new_name='comment',
        ),
        migrations.AddField(
            model_name='iternaryenquiry',
            name='iternaryenquiry',
            field=models.EmailField(max_length=512, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='themes',
            name='meta_description',
            field=models.CharField(default=b'', max_length=160),
        ),
        migrations.AddField(
            model_name='themes',
            name='meta_keywords',
            field=models.CharField(default=b'', max_length=256),
        ),
        migrations.AddField(
            model_name='themes',
            name='meta_title',
            field=models.CharField(default=b'', max_length=60),
        ),
        migrations.AlterField(
            model_name='places',
            name='order',
            field=models.IntegerField(unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='themes',
            name='order',
            field=models.IntegerField(unique=True, null=True, blank=True),
        ),
    ]
