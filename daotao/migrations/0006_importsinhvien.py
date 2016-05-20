# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daotao', '0005_auto_20160116_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportSinhVien',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('import_file', models.FileField(upload_to=b'tmp', null=True, verbose_name=b'Ch\xe1\xbb\x8dn file (.xlsx) d\xe1\xbb\xaf li\xe1\xbb\x87u', blank=True)),
                ('lop', models.ForeignKey(verbose_name=b'L\xe1\xbb\x9bp', to='daotao.Lop')),
            ],
            options={
                'verbose_name': 'Nh\u1eadp danh s\xe1ch sinh vi\xean t\u1eeb file .xlsx',
                'verbose_name_plural': 'Nh\u1eadp danh s\xe1ch sinh vi\xean t\u1eeb file .xlsx',
            },
        ),
    ]
