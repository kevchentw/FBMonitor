# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('FBData', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fbdata',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 14, 15, 49, 32, 526533), auto_now_add=True),
            preserve_default=True,
        ),
    ]
