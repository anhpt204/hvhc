# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0004_auto_20160113_0744'),
        ('tracnghiem', '0021_auto_20160113_0744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='khthi',
            name='tg_ket_thuc',
        ),
        migrations.AddField(
            model_name='khthi',
            name='nguoi_boc_de',
            field=models.ForeignKey(default=1, verbose_name=b'Ng\xc6\xb0\xe1\xbb\x9di b\xe1\xbb\x91c \xc4\x91\xe1\xbb\x81', to='hrm.GiaoVien'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='khthi',
            name='tg_thi',
            field=models.PositiveIntegerField(default=30, verbose_name=b'Th\xe1\xbb\x9di gian thi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='diem',
            field=models.FloatField(default=1.0, verbose_name=b'\xc4\x90i\xe1\xbb\x83m'),
        ),
        migrations.AlterField(
            model_name='khthi',
            name='ngay_thi',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Ng\xc3\xa0y thi'),
        ),
        migrations.AlterField(
            model_name='khthi',
            name='tg_bat_dau',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name=b'Th\xe1\xbb\x9di gian b\xe1\xba\xaft \xc4\x91\xe1\xba\xa7u'),
        ),
    ]
