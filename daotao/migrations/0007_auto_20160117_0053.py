# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daotao', '0006_importsinhvien'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sinhvien',
            name='ho_ten',
        ),
        migrations.AddField(
            model_name='sinhvien',
            name='ho_dem',
            field=models.CharField(default='a', max_length=50, verbose_name=b'H\xe1\xbb\x8d \xc4\x91\xe1\xbb\x87m'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sinhvien',
            name='ten',
            field=models.CharField(default='b', max_length=10, verbose_name=b'T\xc3\xaan'),
            preserve_default=False,
        ),
    ]
