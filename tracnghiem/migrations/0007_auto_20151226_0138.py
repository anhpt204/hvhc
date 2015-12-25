# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daotao', '0001_initial'),
        ('hrm', '0003_sinhvien_lop'),
        ('tracnghiem', '0006_question_macauhoi'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaiThi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ds_cauhoi', models.TextField(default={})),
                ('tra_loi', models.TextField(default={})),
                ('diem', models.PositiveIntegerField(verbose_name=b'\xc4\x90i\xe1\xbb\x83m')),
            ],
        ),
        migrations.CreateModel(
            name='KHThi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ten', models.CharField(max_length=200, verbose_name=b'T\xc3\xaan')),
                ('nam_hoc', models.CharField(help_text=b'Nh\xe1\xba\xadp n\xc4\x83m h\xe1\xbb\x8dc theo \xc4\x91\xe1\xbb\x8bnh d\xe1\xba\xa1ng XXXX-XXXX. V\xc3\xad d\xe1\xbb\xa5 2015-2016', max_length=9, verbose_name=b'N\xc4\x83m h\xe1\xbb\x8dc')),
                ('hoc_ky', models.CharField(default=b'HK1', max_length=3, verbose_name=b'H\xe1\xbb\x8dc k\xe1\xbb\xb3', choices=[(b'HK1', b'H\xe1\xbb\x8dc k\xe1\xbb\xb3 1'), (b'HK2', b'H\xe1\xbb\x8dc k\xe1\xbb\xb3 2')])),
                ('ngay_thi', models.DateField(verbose_name=b'Ng\xc3\xa0y thi')),
                ('tg_bat_dau', models.TimeField(verbose_name=b'Th\xe1\xbb\x9di gian b\xe1\xba\xaft \xc4\x91\xe1\xba\xa7u')),
                ('tg_ket_thuc', models.TimeField(verbose_name=b'Th\xe1\xbb\x9di gian k\xe1\xba\xbft th\xc3\xbac')),
                ('de_thi', models.TextField(default={})),
                ('dap_an', models.TextField(default={})),
                ('tao_moi_de_thi', models.BooleanField(default=True, verbose_name=b'T\xe1\xba\xa1o m\xe1\xbb\x9bi \xc4\x91\xe1\xbb\x81 thi cho c\xc3\xa1c sinh vi\xc3\xaan')),
                ('so_luong_de', models.PositiveIntegerField(default=0, help_text=b'Nh\xe1\xba\xadp gi\xc3\xa1 tr\xe1\xbb\x8b >= 0, nh\xe1\xba\xadp 0 s\xe1\xba\xbd sinh m\xe1\xbb\x97i sinh vi\xc3\xaan m\xe1\xbb\x99t \xc4\x91\xe1\xbb\x81', verbose_name=b'S\xe1\xbb\x91 l\xc6\xb0\xe1\xbb\xa3ng \xc4\x91\xe1\xbb\x81 thi t\xe1\xba\xa1o ra')),
                ('ghichu', models.TextField(null=True, verbose_name=b'Ghi ch\xc3\xba', blank=True)),
                ('doi_tuong', models.ForeignKey(verbose_name=b'\xc4\x90\xe1\xbb\x91i t\xc6\xb0\xe1\xbb\xa3ng', to='daotao.DoiTuong')),
                ('ds_giamthi', models.ManyToManyField(related_name='khthi_giamthi_cathi', verbose_name='Danh s\xe1ch gi\xe1m th\u1ecb coi thi', to='hrm.GiaoVien')),
                ('ds_thisinh', models.ManyToManyField(help_text=b'T\xc3\xacm ki\xe1\xba\xbfm theo h\xe1\xbb\x8d t\xc3\xaan sinh vi\xc3\xaan ho\xe1\xba\xb7c m\xc3\xa3 l\xe1\xbb\x9bp.', to='hrm.SinhVien', verbose_name='Danh s\xe1ch th\xed sinh')),
                ('mon_thi', models.ForeignKey(related_name='khthi_monthi_cathi', verbose_name=b'M\xc3\xb4n thi', to='daotao.MonThi')),
            ],
            options={
                'verbose_name': 'K\u1ebf ho\u1ea1ch thi - b\u1ed1c \u0111\u1ec1',
                'verbose_name_plural': 'K\u1ebf ho\u1ea1ch thi - b\u1ed1c \u0111\u1ec1',
            },
        ),
        migrations.RemoveField(
            model_name='cathi',
            name='ds_giamthi',
        ),
        migrations.RemoveField(
            model_name='cathi',
            name='ds_thisinh',
        ),
        migrations.RemoveField(
            model_name='cathi',
            name='monHoc',
        ),
        migrations.RemoveField(
            model_name='chapter_setting',
            name='ca_thi',
        ),
        migrations.RemoveField(
            model_name='dethi',
            name='ca_thi',
        ),
        migrations.RemoveField(
            model_name='dethi',
            name='sinh_vien',
        ),
        migrations.RemoveField(
            model_name='questiongroup_setting',
            name='ca_thi',
        ),
        migrations.RemoveField(
            model_name='questiongroup_setting',
            name='level',
        ),
        migrations.AlterField(
            model_name='nganhangde',
            name='logSinhDe',
            field=models.ForeignKey(verbose_name=b'C\xe1\xba\xa5u h\xc3\xacnh sinh \xc4\x91\xe1\xbb\x81', to='tracnghiem.LogSinhDe'),
        ),
        migrations.AlterField(
            model_name='sinhdeconf',
            name='logSinhDe',
            field=models.ForeignKey(verbose_name=b'C\xe1\xba\xa5u h\xc3\xacnh sinh \xc4\x91\xe1\xbb\x81', to='tracnghiem.LogSinhDe'),
        ),
        migrations.DeleteModel(
            name='CaThi',
        ),
        migrations.DeleteModel(
            name='Chapter_Setting',
        ),
        migrations.DeleteModel(
            name='DeThi',
        ),
        migrations.DeleteModel(
            name='QuestionGroup_Setting',
        ),
        migrations.AddField(
            model_name='baithi',
            name='khthi',
            field=models.ForeignKey(to='tracnghiem.KHThi'),
        ),
        migrations.AddField(
            model_name='baithi',
            name='thi_sinh',
            field=models.ForeignKey(verbose_name=b'Sinh vi\xc3\xaan', to='hrm.SinhVien'),
        ),
    ]
