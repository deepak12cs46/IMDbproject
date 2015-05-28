# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='movie_name',
            field=models.CharField(default='Ghost Name', max_length=300, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie_name',
            field=models.CharField(default='Ghost Name', max_length=300, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='storyline',
            name='movie_name',
            field=models.CharField(default='Ghost Name', max_length=300, primary_key=True, serialize=False),
        ),
    ]
