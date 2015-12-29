# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracnghiem', '0007_auto_20151226_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baithi',
            name='thi_sinh',
            field=models.ForeignKey(to='hrm.SinhVien', to_field=b'ma_sv', verbose_name=b'Sinh vi\xc3\xaan'),
        ),
        migrations.AlterField(
            model_name='khthi',
            name='dap_an',
            field=models.TextField(default=b'{}'),
        ),
        migrations.AlterField(
            model_name='khthi',
            name='de_thi',
            field=models.TextField(default=b'{}'),
        ),
        migrations.AlterField(
            model_name='khthi',
            name='doi_tuong',
            field=models.ForeignKey(verbose_name='\u0110\u1ed1i t\u01b0\u1ee3ng', to='daotao.DoiTuong'),
        ),
        migrations.AlterField(
            model_name='khthi',
            name='ds_giamthi',
            field=models.ManyToManyField(related_name='khthi_giamthi_khthi', verbose_name='Danh s\xe1ch gi\xe1m th\u1ecb coi thi', to='hrm.GiaoVien'),
        ),
        migrations.AlterField(
            model_name='khthi',
            name='ds_thisinh',
            field=models.ManyToManyField(related_name='khthi_sinhvien_khthi', verbose_name='Danh s\xe1ch th\xed sinh', to='hrm.SinhVien'),
        ),
        migrations.AlterField(
            model_name='khthi',
            name='hoc_ky',
            field=models.CharField(default=b'HK1', max_length=3, verbose_name='H\u1ecdc k\u1ef3', choices=[(b'HK1', b'H\xe1\xbb\x8dc k\xe1\xbb\xb3 1'), (b'HK2', b'H\xe1\xbb\x8dc k\xe1\xbb\xb3 2')]),
        ),
        migrations.AlterField(
            model_name='khthi',
            name='nam_hoc',
            field=models.CharField(help_text='Nh\u1eadp n\u0103m h\u1ecdc theo \u0111\u1ecbnh d\u1ea1ng XXXX-XXXX. V\xed d\u1ee5 2015-2016', max_length=9, verbose_name='N\u0103m h\u1ecdc'),
        ),
        migrations.AlterField(
            model_name='khthi',
            name='so_luong_de',
            field=models.PositiveIntegerField(default=0, help_text='Nh\u1eadp gi\xe1 tr\u1ecb >= 0, nh\u1eadp 0 s\u1ebd sinh m\u1ed7i sinh vi\xean m\u1ed9t \u0111\u1ec1', verbose_name=b'S\xe1\xbb\x91 l\xc6\xb0\xe1\xbb\xa3ng \xc4\x91\xe1\xbb\x81 thi t\xe1\xba\xa1o ra'),
        ),
        migrations.AlterField(
            model_name='khthi',
            name='ten',
            field=models.CharField(max_length=200, verbose_name='T\xean'),
        ),
    ]
