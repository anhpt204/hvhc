# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0004_auto_20160113_0744'),
        ('daotao', '0002_auto_20160113_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthi',
            name='khoa',
            field=models.ForeignKey(default=1, verbose_name=b'\xc4\x90\xc6\xa1n v\xe1\xbb\x8b', to='hrm.DonVi'),
            preserve_default=False,
        ),
    ]
