# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0015_auto_20151229_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='loggeduser',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='loggeduser',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
