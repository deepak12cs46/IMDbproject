# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0002_auto_20150516_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='cast1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cast',
            name='cast2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cast',
            name='cast3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cast',
            name='cast4',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cast',
            name='cast5',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cast',
            name='cast6',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cast',
            name='cast7',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie_rating',
            field=models.DecimalField(decimal_places=1, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='storyline',
            name='movie_story',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]
