# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0022_auto_20160113_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='khthi',
            name='tg_thi',
            field=models.PositiveIntegerField(default=30, verbose_name=b'Th\xe1\xbb\x9di gian thi'),
        ),
    ]
