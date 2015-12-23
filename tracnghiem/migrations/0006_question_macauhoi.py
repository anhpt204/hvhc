# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0005_auto_20151202_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='maCauHoi',
            field=models.CharField(default='default', max_length=20, verbose_name=b'M\xc3\xa3 c\xc3\xa2u h\xe1\xbb\x8fi'),
            preserve_default=False,
        ),
    ]
