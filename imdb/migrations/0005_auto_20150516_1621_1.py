# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0004_auto_20150516_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='movie_rating',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=4),
        ),
    ]
