# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trang_thai_thi', models.CharField(default=b'DA_THI', max_length=20, verbose_name=b'Tr\xe1\xba\xa1ng th\xc3\xa1i thi', choices=[(b'DA_THI', b'\xc4\x90\xc3\xa3 thi'), (b'VANG_CO_LD', b'V\xe1\xba\xafng c\xc3\xb3 l\xc3\xbd do'), (b'VANG_KO_LD', b'V\xe1\xba\xafng kh\xc3\xb4ng l\xc3\xbd do')])),
                ('diem', models.CommaSeparatedIntegerField(max_length=5, null=True, verbose_name=b'\xc4\x90i\xe1\xbb\x83m', blank=True)),
            ],
            options={
                'verbose_name': '\u0110i\u1ec3m',
                'verbose_name_plural': 'B\u1ea3ng \u0111i\u1ec3m',
            },
        ),
        migrations.CreateModel(
            name='DoiTuong',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ma_dt', models.CharField(help_text=b'M\xc3\xa3 kh\xc3\xb4ng qu\xc3\xa1 10 k\xc3\xbd t\xe1\xbb\xb1', unique=True, max_length=10, verbose_name=b'M\xc3\xa3 \xc4\x91\xe1\xbb\x91i t\xc6\xb0\xe1\xbb\xa3ng')),
                ('ten_dt', models.CharField(unique=True, max_length=50, verbose_name=b'T\xc3\xaan \xc4\x91\xe1\xbb\x91i t\xc6\xb0\xe1\xbb\xa3ng')),
            ],
            options={
                'verbose_name': '\u0110\u1ed1i t\u01b0\u1ee3ng',
                'verbose_name_plural': 'Danh s\xe1ch \u0111\u1ed1i t\u01b0\u1ee3ng',
            },
        ),
        migrations.CreateModel(
            name='Lop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ma_lop', models.CharField(unique=True, max_length=5, verbose_name=b'M\xc3\xa3 l\xe1\xbb\x9bp')),
                ('ten_lop', models.CharField(unique=True, max_length=200, verbose_name=b'L\xe1\xbb\x9bp')),
                ('si_so', models.PositiveIntegerField(null=True, verbose_name=b'S\xc4\xa9 s\xe1\xbb\x91', blank=True)),
                ('doi_tuong', models.ForeignKey(verbose_name=b'\xc4\x90\xe1\xbb\x91i t\xc6\xb0\xe1\xbb\xa3ng', to='daotao.DoiTuong')),
            ],
            options={
                'verbose_name': 'L\u1edbp',
                'verbose_name_plural': 'Danh s\xe1ch l\u1edbp',
            },
        ),
        migrations.CreateModel(
            name='MonThi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ma_mon_thi', models.CharField(unique=True, max_length=10, verbose_name=b'M\xc3\xa3 m\xc3\xb4n thi')),
                ('ten_mon_thi', models.CharField(unique=True, max_length=200, verbose_name=b'M\xc3\xb4n thi')),
                ('so_chuong', models.PositiveIntegerField(default=5, verbose_name=b'S\xe1\xbb\x91 ch\xc6\xb0\xc6\xa1ng')),
            ],
            options={
                'verbose_name': 'M\xf4n thi',
                'verbose_name_plural': 'Danh s\xe1ch m\xf4n thi',
            },
        ),
        migrations.AddField(
            model_name='diem',
            name='mon_thi',
            field=models.ForeignKey(verbose_name=b'M\xc3\xb4n thi', to='daotao.MonThi'),
        ),
        migrations.AddField(
            model_name='diem',
            name='sinh_vien',
            field=models.ForeignKey(verbose_name=b'Sinh vi\xc3\xaan', to='hrm.SinhVien'),
        ),
        migrations.AlterUniqueTogether(
            name='diem',
            unique_together=set([('sinh_vien', 'mon_thi')]),
        ),
    ]
