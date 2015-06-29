# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('FBData', '0003_auto_20150614_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbdata',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 14, 15, 52, 10, 528387), auto_now_add=True),
            preserve_default=True,
        ),
    ]
