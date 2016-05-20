# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0025_auto_20160113_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='khthi',
            name='trang_thai',
            field=models.CharField(default=b'CHUA_THI', choices=[(b'CHUA_THI', b'Ch\xc6\xb0a thi'), (b'DANG_THI', b'\xc4\x90ang thi'), (b'DA_THI', b'\xc4\x90\xc3\xa3 thi')], max_length=30, blank=True, null=True, verbose_name=b'Tr\xe1\xba\xa1ng th\xc3\xa1i'),
        ),
    ]
