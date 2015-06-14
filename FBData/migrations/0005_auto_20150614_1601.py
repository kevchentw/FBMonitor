# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('FBData', '0004_auto_20150614_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbdata',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 6, 14, 16, 1, 0, 409317)),
            preserve_default=True,
        ),
    ]
