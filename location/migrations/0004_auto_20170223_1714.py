# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_location_mandal'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='location',
            unique_together=set([]),
        ),
    ]
