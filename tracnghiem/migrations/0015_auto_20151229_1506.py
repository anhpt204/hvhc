# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0014_auto_20151229_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loggeduser',
            name='username',
            field=models.CharField(default=b'10', max_length=30, serialize=False, primary_key=True),
        ),
    ]
