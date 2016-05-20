# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daotao', '0004_auto_20160113_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinhvien',
            name='ma_sv',
            field=models.CharField(unique=True, max_length=15, verbose_name=b'M\xc3\xa3 sinh vi\xc3\xaan'),
        ),
    ]
