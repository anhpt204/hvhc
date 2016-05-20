# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0004_auto_20160113_0744'),
        ('daotao', '0004_auto_20160113_0835'),
        ('tracnghiem', '0026_auto_20160113_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportMCQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('import_file', models.FileField(upload_to=b'tmp', null=True, verbose_name=b'Ch\xe1\xbb\x8dn file d\xe1\xbb\xaf li\xe1\xbb\x87u', blank=True)),
                ('doi_tuong', models.ForeignKey(verbose_name=b'\xc4\x90\xe1\xbb\x91i t\xc6\xb0\xe1\xbb\xa3ng', to='daotao.DoiTuong')),
                ('khoa', models.ForeignKey(verbose_name=b'Khoa', to='hrm.DonVi')),
                ('mon_thi', models.ForeignKey(verbose_name=b'M\xc3\xb4n thi', to='daotao.MonThi')),
            ],
            options={
                'verbose_name': 'Nh\u1eadp danh s\xe1ch c\xe2u h\u1ecfi Multiple Choice t\u1eeb file',
                'verbose_name_plural': 'Nh\u1eadp danh s\xe1ch c\xe2u h\u1ecfi Multiple Choice t\u1eeb file',
            },
        ),
        migrations.CreateModel(
            name='ImportSinhVien',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('import_file', models.FileField(upload_to=b'tmp', null=True, verbose_name=b'Ch\xe1\xbb\x8dn file d\xe1\xbb\xaf li\xe1\xbb\x87u', blank=True)),
                ('lop', models.ForeignKey(verbose_name=b'L\xe1\xbb\x9bp', to='daotao.Lop')),
            ],
            options={
                'verbose_name': 'Nh\u1eadp danh s\xe1ch sinh vi\xean t\u1eeb file',
                'verbose_name_plural': 'Nh\u1eadp danh s\xe1ch sinh vi\xean t\u1eeb file',
            },
        ),
        migrations.AlterModelOptions(
            name='khthi',
            options={'verbose_name': 'K\u1ebf ho\u1ea1ch thi - b\u1ed1c \u0111\u1ec1', 'verbose_name_plural': 'K\u1ebf ho\u1ea1ch thi - b\u1ed1c \u0111\u1ec1', 'permissions': (('duoc_phep_boc_de', 'Ng\u01b0\u1eddi d\xf9ng \u0111\u01b0\u1ee3c ph\xe9p b\u1ed1c \u0111\u1ec1'), ('duoc_phep_xem_va_in_de', 'Ng\u01b0\u1eddi d\xf9ng \u0111\u01b0\u1ee3c ph\xe9p xem v\xe0 in \u0111\u1ec1'))},
        ),
    ]
