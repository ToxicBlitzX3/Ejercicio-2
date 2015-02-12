# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misDatos', '0002_social'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='facebook',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='social',
            name='twitter',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='social',
            name='youtube',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
