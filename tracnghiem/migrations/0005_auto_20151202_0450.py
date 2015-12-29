# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0004_auto_20151202_0428'),
    ]

    operations = [
        migrations.AddField(
            model_name='nganhangde',
            name='ngay_tao',
            field=models.DateField(default=datetime.datetime(2015, 12, 1, 21, 50, 25, 720392, tzinfo=utc), verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nganhangde',
            name='maDeThi',
            field=models.CharField(max_length=10, null=True, verbose_name=b'M\xc3\xa3 \xc4\x91\xe1\xbb\x81 thi', blank=True),
        ),
    ]
