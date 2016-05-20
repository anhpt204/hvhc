# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0032_khthi_tg_thi_batdau'),
    ]

    operations = [
        migrations.AlterField(
            model_name='khthi',
            name='tg_thi_batdau',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
