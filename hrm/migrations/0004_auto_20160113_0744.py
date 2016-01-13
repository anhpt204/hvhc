# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0021_auto_20160113_0744'),
        ('daotao', '0002_auto_20160113_0744'),
        ('hrm', '0003_sinhvien_lop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sinhvien',
            name='lop',
        ),
        migrations.RemoveField(
            model_name='sinhvien',
            name='user',
        ),
        migrations.DeleteModel(
            name='SinhVien',
        ),
    ]
