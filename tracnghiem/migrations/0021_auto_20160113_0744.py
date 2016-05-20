# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0020_baithi_is_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baithi',
            name='thi_sinh',
            field=models.ForeignKey(to='daotao.SinhVien', to_field=b'ma_sv', verbose_name=b'Sinh vi\xc3\xaan'),
        ),
        migrations.AlterField(
            model_name='khthi',
            name='ds_thisinh',
            field=models.ManyToManyField(related_name='khthi_sinhvien_khthi', verbose_name='Danh s\xe1ch th\xed sinh', to='daotao.SinhVien'),
        ),
        migrations.AlterField(
            model_name='lop_cathi',
            name='ds_sinhvien',
            field=models.ManyToManyField(to='daotao.SinhVien'),
        ),
    ]
