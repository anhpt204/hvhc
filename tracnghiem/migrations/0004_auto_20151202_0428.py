# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0003_auto_20151031_0243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='audio',
        ),
        migrations.RemoveField(
            model_name='question',
            name='clip',
        ),
        migrations.AddField(
            model_name='nganhangde',
            name='maDeThi',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='thuocChuong',
            field=models.CommaSeparatedIntegerField(default=1, max_length=50, verbose_name=b'Ph\xe1\xbb\xa7 c\xc3\xa1c ch\xc6\xb0\xc6\xa1ng'),
        ),
    ]
