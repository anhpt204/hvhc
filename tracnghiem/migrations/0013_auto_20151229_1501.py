# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0012_loggeduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='loggeduser',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=b'10', serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='loggeduser',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
