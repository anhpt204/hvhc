# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0009_auto_20151226_0300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baithi',
            options={'verbose_name': 'B\xe0i thi', 'verbose_name_plural': 'B\xe0i thi'},
        ),
        migrations.AddField(
            model_name='khthi',
            name='de_thi_goc',
            field=models.ForeignKey(default=1, verbose_name=b'\xc4\x90\xe1\xbb\x81 thi', to='tracnghiem.NganHangDe'),
            preserve_default=False,
        ),
    ]
