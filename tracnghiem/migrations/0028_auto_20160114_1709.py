# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0027_auto_20160114_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importmcquestion',
            name='khoa',
        ),
        migrations.AlterField(
            model_name='question',
            name='maCauHoi',
            field=models.CharField(unique=True, max_length=20, verbose_name=b'M\xc3\xa3 c\xc3\xa2u h\xe1\xbb\x8fi'),
        ),
    ]
