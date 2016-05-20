# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0028_auto_20160114_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='taoBoi',
        ),
    ]
