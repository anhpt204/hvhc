# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0017_auto_20151229_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loggeduser',
            name='login_time',
        ),
    ]
