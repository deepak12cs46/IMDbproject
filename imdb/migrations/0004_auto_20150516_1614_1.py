# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0003_auto_20150516_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='movie_name',
            field=models.CharField(primary_key=True, serialize=False, max_length=300),
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie_name',
            field=models.CharField(primary_key=True, serialize=False, max_length=300),
        ),
        migrations.AlterField(
            model_name='storyline',
            name='movie_name',
            field=models.CharField(primary_key=True, serialize=False, max_length=300),
        ),
    ]
