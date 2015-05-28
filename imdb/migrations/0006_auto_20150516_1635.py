# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0005_auto_20150516_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='movie_rating',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
