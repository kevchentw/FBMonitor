# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FBData', '0005_auto_20150614_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbdata',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
