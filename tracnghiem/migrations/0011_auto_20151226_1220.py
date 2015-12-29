# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0010_auto_20151226_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='khthi',
            name='de_thi_goc',
        ),
        migrations.AddField(
            model_name='khthi',
            name='de_thi_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
