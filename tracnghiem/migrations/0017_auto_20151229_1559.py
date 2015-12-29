# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0016_auto_20151229_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loggeduser',
            name='id',
        ),
        migrations.AddField(
            model_name='loggeduser',
            name='login_time',
            field=models.DateTimeField(default=timezone.now()),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='loggeduser',
            name='username',
            field=models.CharField(max_length=30, serialize=False, primary_key=True),
        ),
    ]
