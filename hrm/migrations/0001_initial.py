# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
#         ('daotao', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DonVi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ma_dv', models.CharField(help_text=b'M\xc3\xa3 \xc4\x91\xc6\xa1n v\xe1\xbb\x8b kh\xc3\xb4ng qu\xc3\xa1 5 k\xc3\xbd t\xe1\xbb\xb1', unique=True, max_length=5, verbose_name=b'M\xc3\xa3 \xc4\x91\xc6\xa1n v\xe1\xbb\x8b')),
                ('ten_dv', models.CharField(unique=True, max_length=200, verbose_name=b'T\xc3\xaan \xc4\x91\xc6\xa1n v\xe1\xbb\x8b')),
                ('cha_dv', models.ForeignKey(blank=True, to='hrm.DonVi', help_text=b'\xc4\x90\xc6\xa1n v\xe1\xbb\x8b c\xe1\xba\xa5p tr\xc3\xaan tr\xe1\xbb\xb1c ti\xe1\xba\xbfp', null=True, verbose_name=b'\xc4\x90\xc6\xa1n v\xe1\xbb\x8b c\xe1\xba\xa5p tr\xc3\xaan')),
            ],
            options={
                'verbose_name': '\u0110\u01a1n v\u1ecb',
                'verbose_name_plural': 'Danh s\xe1ch \u0111\u01a1n v\u1ecb',
            },
        ),
        migrations.CreateModel(
            name='GiaoVien',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ma_so', models.PositiveIntegerField(unique=True, verbose_name=b'M\xc3\xa3 s\xe1\xbb\x91')),
                ('ho_ten', models.CharField(max_length=50, verbose_name=b'H\xe1\xbb\x8d v\xc3\xa0 t\xc3\xaan')),
                ('don_vi', models.ForeignKey(verbose_name=b'\xc4\x90\xc6\xa1n v\xe1\xbb\x8b', to='hrm.DonVi', help_text=b'\xc4\x90\xc6\xa1n v\xe1\xbb\x8b qu\xe1\xba\xa3n l\xc3\xbd tr\xe1\xbb\xb1c ti\xe1\xba\xbfp')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Gi\xe1o vi\xean',
                'verbose_name_plural': 'Danh s\xe1ch gi\xe1o vi\xean',
            },
        ),
        migrations.CreateModel(
            name='SinhVien',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ma_sv', models.PositiveIntegerField(unique=True, verbose_name=b'M\xc3\xa3 sinh vi\xc3\xaan')),
                ('ho_ten', models.CharField(max_length=50, verbose_name=b'H\xe1\xbb\x8d v\xc3\xa0 t\xc3\xaan')),
                ('lop', models.ForeignKey(verbose_name=b'L\xe1\xbb\x9bp', to='daotao.Lop')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sinh vi\xean',
                'verbose_name_plural': 'Danh s\xe1ch sinh vi\xean',
            },
        ),
    ]
