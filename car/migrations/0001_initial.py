# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('types', models.CharField(max_length=50)),
                ('car_time', models.CharField(max_length=30)),
                ('mileage', models.CharField(max_length=30)),
                ('car_price', models.CharField(max_length=30)),
                ('image_url', models.CharField(max_length=200)),
                ('car_url', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=300)),
                ('transmission_mode', models.CharField(max_length=50)),
                ('have_accident', models.CharField(max_length=10)),
            ],
        ),
    ]
