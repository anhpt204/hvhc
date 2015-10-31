# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('daotao', '0001_initial'),
        ('hrm', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoDe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ma_so', models.CharField(max_length=20, null=True, verbose_name=b'M\xc3\xa3 b\xe1\xbb\x99 \xc4\x91\xe1\xbb\x81', blank=True)),
                ('ngay_tao', models.DateField(default=django.utils.timezone.now, verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o')),
                ('doi_tuong', models.ForeignKey(verbose_name=b'\xc4\x90\xe1\xbb\x91i t\xc6\xb0\xe1\xbb\xa3ng thi', to='daotao.DoiTuong')),
                ('mon_thi', models.ForeignKey(verbose_name=b'M\xc3\xb4n thi', to='daotao.MonThi')),
            ],
            options={
                'verbose_name': 'B\u1ed9 \u0111\u1ec1 thi t\u1ef1 lu\u1eadn',
                'verbose_name_plural': 'B\u1ed9 \u0111\u1ec1 thi t\u1ef1 lu\u1eadn',
            },
        ),
        migrations.CreateModel(
            name='CaThi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ten_ca_thi', models.CharField(max_length=100, verbose_name=b'T\xc3\xaan ca thi')),
                ('nam_hoc', models.CharField(help_text=b'Nh\xe1\xba\xadp n\xc4\x83m h\xe1\xbb\x8dc theo \xc4\x91\xe1\xbb\x8bnh d\xe1\xba\xa1ng XXXX-XXXX. V\xc3\xad d\xe1\xbb\xa5 2015-2016', max_length=9, verbose_name=b'N\xc4\x83m h\xe1\xbb\x8dc')),
                ('hoc_ky', models.CharField(default=b'HK1', max_length=3, verbose_name=b'H\xe1\xbb\x8dc k\xe1\xbb\xb3', choices=[(b'HK1', b'H\xe1\xbb\x8dc k\xe1\xbb\xb3 1'), (b'HK2', b'H\xe1\xbb\x8dc k\xe1\xbb\xb3 2')])),
                ('ngay_thi', models.DateField(verbose_name=b'Ng\xc3\xa0y thi')),
                ('so_de_thi', models.PositiveIntegerField(default=1, help_text='S\u1ed1 \u0111\u1ec1 thi l\xe0 s\u1ed1 nguy\xean d\u01b0\u01a1ng, l\u1edbn h\u01a1n 0', verbose_name=b'S\xe1\xbb\x91 \xc4\x91\xe1\xbb\x81 thi')),
                ('doi_tuong', models.ForeignKey(verbose_name=b'\xc4\x90\xe1\xbb\x91i t\xc6\xb0\xe1\xbb\xa3ng', to='daotao.DoiTuong')),
            ],
            options={
                'verbose_name': 'K\u1ebf ho\u1ea1ch thi - b\u1ed1c \u0111\u1ec1',
                'verbose_name_plural': 'K\u1ebf ho\u1ea1ch thi - b\u1ed1c \u0111\u1ec1',
            },
        ),
        migrations.CreateModel(
            name='DeThi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ma_de_thi', models.CharField(max_length=10, verbose_name=b'M\xc3\xa3 \xc4\x91\xe1\xbb\x81 thi')),
                ('de_thi', models.FileField(upload_to=b'uploads/essay/%Y/%m/%d', null=True, verbose_name=b'\xc4\x90\xe1\xbb\x81 thi', blank=True)),
                ('dap_an', models.FileField(upload_to=b'uploads/essay/%Y/%m/%d', null=True, verbose_name=b'\xc4\x90\xc3\xa1p \xc3\xa1n', blank=True)),
                ('ngan_hang', models.ForeignKey(verbose_name=b'Ng\xc3\xa2n h\xc3\xa0ng', to='tuluan.BoDe')),
            ],
            options={
                'verbose_name': '\u0110\u1ec1 thi t\u1ef1 lu\u1eadn',
                'verbose_name_plural': 'Danh s\xe1ch \u0111\u1ec1 thi t\u1ef1 lu\u1eadn',
            },
        ),
        migrations.AddField(
            model_name='cathi',
            name='ds_de_thi',
            field=models.ManyToManyField(to='tuluan.DeThi', verbose_name='DT', blank=True),
        ),
        migrations.AddField(
            model_name='cathi',
            name='giam_thi',
            field=models.ManyToManyField(to='hrm.GiaoVien', verbose_name='Danh s\xe1ch gi\xe1m th\u1ecb coi thi'),
        ),
        migrations.AddField(
            model_name='cathi',
            name='lop',
            field=models.ForeignKey(verbose_name=b'L\xe1\xbb\x9bp', to='daotao.Lop'),
        ),
        migrations.AddField(
            model_name='cathi',
            name='mon_thi',
            field=models.ForeignKey(verbose_name=b'M\xc3\xb4n thi', to='daotao.MonThi'),
        ),
    ]
