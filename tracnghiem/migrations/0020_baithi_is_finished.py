# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0019_loggeduser_login_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='baithi',
            name='is_finished',
            field=models.BooleanField(default=False, verbose_name=b'Ho\xc3\xa0n th\xc3\xa0nh'),
        ),
    ]
