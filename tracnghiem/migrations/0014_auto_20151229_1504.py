# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0013_auto_20151229_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loggeduser',
            name='id',
        ),
        migrations.RemoveField(
            model_name='loggeduser',
            name='user',
        ),
        migrations.AddField(
            model_name='loggeduser',
            name='username',
            field=models.CharField(default=b'10', max_length=30, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
