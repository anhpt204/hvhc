# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0031_auto_20160117_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='khthi',
            name='tg_thi_batdau',
            field=models.TimeField(default=timezone.now),
        ),
    ]
