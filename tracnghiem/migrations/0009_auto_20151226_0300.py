# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0008_auto_20151226_0233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baithi',
            options={'verbose_name': 'B\xe0i thi', 'verbose_name_plural': 'K\u1ebf ho\u1ea1ch thi - b\u1ed1c \u0111\u1ec1'},
        ),
        migrations.AlterUniqueTogether(
            name='baithi',
            unique_together=set([('khthi', 'thi_sinh')]),
        ),
    ]
