# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0002_auto_20151031_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='taoBoi',
            field=models.ForeignKey(verbose_name=b'Ng\xc6\xb0\xe1\xbb\x9di t\xe1\xba\xa1o', to='hrm.GiaoVien'),
        ),
    ]
