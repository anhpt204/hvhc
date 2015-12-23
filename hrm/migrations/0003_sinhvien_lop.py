# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daotao', '0001_initial'),
        ('hrm', '0002_remove_sinhvien_lop'),
    ]

    operations = [
        migrations.AddField(
            model_name='sinhvien',
            name='lop',
            field=models.ForeignKey(default=1, verbose_name=b'L\xe1\xbb\x9bp', to='daotao.Lop'),
            preserve_default=False,
        ),
    ]
