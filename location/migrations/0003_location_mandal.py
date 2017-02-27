# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20170217_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='mandal',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
