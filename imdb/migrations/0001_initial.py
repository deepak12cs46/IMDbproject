# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('movie_name', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('cast1', models.CharField(max_length=100)),
                ('cast2', models.CharField(max_length=100)),
                ('cast3', models.CharField(max_length=100)),
                ('cast4', models.CharField(max_length=100)),
                ('cast5', models.CharField(max_length=100)),
                ('cast6', models.CharField(max_length=100)),
                ('cast7', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('movie_name', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('movie_rating', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Storyline',
            fields=[
                ('movie_name', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('movie_story', models.CharField(max_length=5000)),
            ],
        ),
    ]
