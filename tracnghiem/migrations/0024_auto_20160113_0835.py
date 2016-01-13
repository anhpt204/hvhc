# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0023_auto_20160113_0802'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='khthi',
            options={'verbose_name': 'K\u1ebf ho\u1ea1ch thi - b\u1ed1c \u0111\u1ec1', 'verbose_name_plural': 'K\u1ebf ho\u1ea1ch thi - b\u1ed1c \u0111\u1ec1', 'permissions': (('duoc_phep_boc_de', 'Ng\u01b0\u1eddi d\xf9ng \u0111\u01b0\u1ee3c ph\xe9p b\u1ed1c \u0111\u1ec1'), ('duoc_phep_xem_va_in_de', 'Ng\u01b0\u1eddi d\xf9ng \u0111\u01b0\u1ee3c ph\xe9p xem v\xe0 in \u0111\u1ec1'))},
        ),
        migrations.AlterField(
            model_name='khthi',
            name='tg_thi',
            field=models.PositiveIntegerField(default=30, help_text=b'Nh\xe1\xba\xadp th\xe1\xbb\x9di gian thi t\xc3\xadnh b\xe1\xba\xb1ng \xc4\x91\xc6\xa1n v\xe1\xbb\x8b ph\xc3\xbat', verbose_name=b'Th\xe1\xbb\x9di gian thi (ph\xc3\xbat)'),
        ),
    ]
