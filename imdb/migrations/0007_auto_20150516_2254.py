# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0006_auto_20150516_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='cast',
            name='movie_rating',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='storyline',
            name='movie_rating',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
