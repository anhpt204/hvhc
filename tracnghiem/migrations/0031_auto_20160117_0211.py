# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0030_auto_20160117_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='khthi',
            name='nguoi_boc_de',
            field=models.ForeignKey(verbose_name=b'Ng\xc6\xb0\xe1\xbb\x9di b\xe1\xbb\x91c \xc4\x91\xe1\xbb\x81', blank=True, to='hrm.GiaoVien', null=True),
        ),
    ]
