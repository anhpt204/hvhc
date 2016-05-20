# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0029_remove_question_taoboi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importsinhvien',
            name='lop',
        ),
        migrations.DeleteModel(
            name='ImportSinhVien',
        ),
    ]
