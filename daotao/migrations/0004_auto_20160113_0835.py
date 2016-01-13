# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daotao', '0003_monthi_khoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthi',
            name='khoa',
            field=models.ForeignKey(verbose_name=b'Khoa', to='hrm.DonVi'),
        ),
    ]
