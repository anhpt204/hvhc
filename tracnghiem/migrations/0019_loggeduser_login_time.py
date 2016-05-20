# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0018_remove_loggeduser_login_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='loggeduser',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 29, 9, 1, 45, 108888, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
