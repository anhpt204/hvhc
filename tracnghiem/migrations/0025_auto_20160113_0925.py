# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0024_auto_20160113_0835'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='khthi',
            options={'verbose_name': 'K\u1ebf ho\u1ea1ch thi - b\u1ed1c \u0111\u1ec1', 'verbose_name_plural': 'K\u1ebf ho\u1ea1ch thi - b\u1ed1c \u0111\u1ec1'},
        ),
        migrations.AddField(
            model_name='khthi',
            name='trang_thai',
            field=models.CharField(default=b'CHUA_THI', max_length=30, null=True, blank=True, choices=[(b'CHUA_THI', b'Ch\xc6\xb0a thi'), (b'DANG_THI', b'\xc4\x90ang thi'), (b'DA_THI', b'\xc4\x90\xc3\xa3 thi')]),
        ),
    ]
