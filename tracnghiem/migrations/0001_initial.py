# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('daotao', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hrm', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dapAn', models.CharField(max_length=1000, verbose_name=b'Ph\xc6\xb0\xc6\xa1ng \xc3\xa1n tr\xe1\xba\xa3 l\xe1\xbb\x9di')),
                ('isCorrect', models.BooleanField(default=False, help_text=b'Ph\xc6\xb0\xc6\xa1ng \xc3\xa1n \xc4\x91\xc3\xbang?', verbose_name=b'L\xc3\xa0 ph\xc6\xb0\xc6\xa1ng \xc3\xa1n \xc4\x91\xc3\xbang')),
            ],
            options={
                'verbose_name': 'Ph\u01b0\u01a1ng \xe1n tr\u1ea3 l\u1eddi',
                'verbose_name_plural': 'Danh s\xe1ch ph\u01b0\u01a1ng \xe1n tr\u1ea3 l\u1eddi',
            },
        ),
        migrations.CreateModel(
            name='CaThi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'Ca thi')),
                ('description', models.TextField(null=True, verbose_name=b'Ghi ch\xc3\xba', blank=True)),
                ('ngay_thi', models.DateField(verbose_name=b'Ng\xc3\xa0y thi')),
                ('tg_bat_dau', models.TimeField(verbose_name=b'Th\xe1\xbb\x9di gian b\xe1\xba\xaft \xc4\x91\xe1\xba\xa7u')),
                ('tg_ket_thuc', models.TimeField(verbose_name=b'Th\xe1\xbb\x9di gian k\xe1\xba\xbft th\xc3\xbac')),
                ('ds_cau_hoi', models.CommaSeparatedIntegerField(max_length=1024, verbose_name=b'Danh sach cau hoi (ids)')),
                ('tao_moi_de_thi', models.BooleanField(default=True, verbose_name=b'T\xe1\xba\xa1o m\xe1\xbb\x9bi \xc4\x91\xe1\xbb\x81 thi cho c\xc3\xa1c sinh vi\xc3\xaan')),
                ('random_order', models.BooleanField(default=True, verbose_name=b'Hi\xe1\xbb\x83n th\xe1\xbb\x8b c\xc3\xa2u h\xe1\xbb\x8fi ng\xe1\xba\xabu nhi\xc3\xaan')),
                ('answers_at_end', models.BooleanField(default=False, verbose_name=b'Hi\xe1\xbb\x83n th\xe1\xbb\x8b c\xc3\xa2u tr\xe1\xba\xa3 l\xe1\xbb\x9di khi k\xe1\xba\xbft th\xc3\xbac')),
                ('result_at_end', models.BooleanField(default=True, verbose_name=b'Hi\xe1\xbb\x83n th\xe1\xbb\x8b k\xe1\xba\xbft qu\xe1\xba\xa3 khi k\xe1\xba\xbft th\xc3\xbac')),
                ('exam_paper', models.BooleanField(default=True, verbose_name=b'L\xc6\xb0u b\xc3\xa0i thi')),
                ('single_attempt', models.BooleanField(default=True, verbose_name=b'M\xe1\xbb\x97i ng\xc6\xb0\xe1\xbb\x9di m\xe1\xbb\x99t \xc4\x91\xe1\xbb\x81 thi')),
                ('pass_mark', models.PositiveIntegerField(verbose_name=b'\xc4\x90i\xe1\xbb\x83m \xc4\x91\xe1\xba\xa1t y\xc3\xaau c\xe1\xba\xa7u')),
                ('success_text', models.TextField(verbose_name=b'Th\xc3\xb4ng b\xc3\xa1o \xc4\x91\xc6\xb0\xe1\xbb\xa3c hi\xe1\xbb\x83n th\xe1\xbb\x8b n\xe1\xba\xbfu th\xc3\xad sinh v\xc6\xb0\xe1\xbb\xa3t qua', blank=True)),
                ('fail_text', models.TextField(verbose_name=b'Th\xc3\xb4ng b\xc3\xa1o \xc4\x91\xc6\xb0\xe1\xbb\xa3c hi\xe1\xbb\x83n th\xe1\xbb\x8b n\xe1\xba\xbfu th\xc3\xad sinh kh\xc3\xb4ng v\xc6\xb0\xe1\xbb\xa3t qua', blank=True)),
                ('draft', models.BooleanField(default=False, verbose_name=b'B\xe1\xba\xa3n nh\xc3\xa1p')),
                ('ds_giamthi', models.ManyToManyField(related_name='cathi_giamthi_cathi', verbose_name='Danh s\xe1ch gi\xe1m th\u1ecb coi thi', to='hrm.GiaoVien')),
                ('ds_thisinh', models.ManyToManyField(help_text=b'T\xc3\xacm ki\xe1\xba\xbfm theo h\xe1\xbb\x8d t\xc3\xaan sinh vi\xc3\xaan ho\xe1\xba\xb7c m\xc3\xa3 l\xe1\xbb\x9bp.', to='hrm.SinhVien', verbose_name='Danh s\xe1ch th\xed sinh')),
                ('monHoc', models.ForeignKey(related_name='cathi_monthi_cathi', verbose_name=b'M\xc3\xb4n thi', to='daotao.MonThi')),
            ],
            options={
                'verbose_name': 'Ca thi',
                'verbose_name_plural': 'Danh s\xe1ch ca thi',
            },
        ),
        migrations.CreateModel(
            name='Chapter_Setting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chapter', models.PositiveIntegerField(default=1, help_text=b'v\xc3\xad d\xe1\xbb\xa5: 1,2,...', verbose_name=b'Ch\xc6\xb0\xc6\xa1ng')),
                ('num_of_questions', models.PositiveIntegerField(default=1, verbose_name=b's\xe1\xbb\x91 c\xc3\xa2u h\xe1\xbb\x8fi')),
                ('ca_thi', models.ForeignKey(verbose_name=b'Ca thi', to='tracnghiem.CaThi')),
            ],
            options={
                'verbose_name': 'Thi\u1ebft l\u1eadp s\u1ed1 c\xe2u h\u1ecfi cho t\u1eebng ch\u01b0\u01a1ng',
                'verbose_name_plural': 'Thi\u1ebft l\u1eadp s\u1ed1 c\xe2u h\u1ecfi cho t\u1eebng ch\u01b0\u01a1ng',
            },
        ),
        migrations.CreateModel(
            name='DeThi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ds_cau_hoi', models.TextField(default={}, verbose_name=b'Danh sach cau hoi')),
                ('user_answers', models.TextField(default={}, verbose_name=b'Danh sach cau tra loi cua thi sinh', blank=True)),
                ('complete', models.BooleanField(default=False, verbose_name=b'Da hoan thanh bai thi chua?')),
                ('start', models.DateTimeField(auto_now_add=True, verbose_name=b'Bat dau luc')),
                ('end', models.DateTimeField(null=True, verbose_name=b'Ket thuc luc', blank=True)),
                ('diem', models.PositiveIntegerField(default=0, verbose_name=b'Diem thi')),
                ('ca_thi', models.ForeignKey(verbose_name=b'Ca thi', to='tracnghiem.CaThi')),
                ('sinh_vien', models.ForeignKey(verbose_name=b'Sinh Vi\xc3\xaan', to='hrm.SinhVien')),
            ],
        ),
        migrations.CreateModel(
            name='LogSinhDe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('soLuong', models.PositiveIntegerField(default=20, verbose_name=b'S\xe1\xbb\x91 l\xc6\xb0\xe1\xbb\xa3ng')),
                ('ngayTao', models.DateField(verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o')),
                ('doiTuong', models.ForeignKey(verbose_name=b'\xc4\x90\xe1\xbb\x91i t\xc6\xb0\xe1\xbb\xa3ng', to='daotao.DoiTuong')),
                ('monHoc', models.ForeignKey(verbose_name=b'M\xc3\xb4n thi', to='daotao.MonThi')),
                ('nguoiTao', models.ForeignKey(verbose_name=b'Ng\xc6\xb0\xe1\xbb\x9di t\xe1\xba\xa1o', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sinh \u0111\u1ec1 thi',
                'verbose_name_plural': 'Sinh \u0111\u1ec1 thi',
            },
        ),
        migrations.CreateModel(
            name='Lop_CaThi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ds_sinhvien', models.ManyToManyField(to='hrm.SinhVien')),
                ('lop', models.ForeignKey(verbose_name=b'L\xe1\xbb\x9bp thi', to='daotao.Lop')),
            ],
        ),
        migrations.CreateModel(
            name='NganHangDe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('questions', models.CommaSeparatedIntegerField(default=1, max_length=50, verbose_name=b'Danh s\xc3\xa1ch c\xc3\xa2u h\xe1\xbb\x8fi')),
                ('daDuyet', models.BooleanField(default=False, verbose_name=b'\xc4\x90\xc3\xa3 duy\xe1\xbb\x87t')),
                ('logSinhDe', models.ForeignKey(to='tracnghiem.LogSinhDe')),
            ],
            options={
                'verbose_name': 'Ng\xe2n h\xe0ng \u0111\u1ec1 thi',
                'verbose_name_plural': 'Ng\xe2n h\xe0ng \u0111\u1ec1 thi',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('loaiCauHoi', models.CharField(default=b'MC', max_length=5, verbose_name=b'Lo\xe1\xba\xa1i c\xc3\xa2u h\xe1\xbb\x8fi', choices=[(b'TF', b'C\xc3\xa2u h\xe1\xbb\x8fi \xc4\x90\xc3\xbang - Sai'), (b'MC', b'C\xc3\xa2u h\xe1\xbb\x8fi Multiple Choice'), (b'ESSAY', b'C\xc3\xa2u h\xe1\xbb\x8fi t\xe1\xbb\xb1 lu\xe1\xba\xadn')])),
                ('thuocChuong', models.CommaSeparatedIntegerField(default=1, max_length=50, verbose_name=b'Thu\xe1\xbb\x99c c\xc3\xa1c ch\xc6\xb0\xc6\xa1ng')),
                ('noiDung', models.TextField(max_length=1000, verbose_name=b'C\xc3\xa2u h\xe1\xbb\x8fi')),
                ('figure', models.ImageField(upload_to=b'uploads/figs/%Y/%m/%d', null=True, verbose_name=b'\xe1\xba\xa2nh', blank=True)),
                ('audio', models.ImageField(upload_to=b'uploads/audios/%Y/%m/%d', null=True, verbose_name=b'\xe1\xba\xa2nh', blank=True)),
                ('clip', models.ImageField(upload_to=b'uploads/clips/%Y/%m/%d', null=True, verbose_name=b'\xe1\xba\xa2nh', blank=True)),
            ],
            options={
                'verbose_name': 'C\xe2u h\u1ecfi',
                'verbose_name_plural': 'Danh s\xe1ch c\xe2u h\u1ecfi',
            },
        ),
        migrations.CreateModel(
            name='QuestionGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name=b'Nh\xc3\xb3m c\xc3\xa2u h\xe1\xbb\x8fi')),
                ('description', models.TextField(null=True, verbose_name=b'Ghi ch\xc3\xba', blank=True)),
            ],
            options={
                'verbose_name': 'Nh\xf3m c\xe2u h\u1ecfi',
                'verbose_name_plural': 'Danh s\xe1ch nh\xf3m c\xe2u h\u1ecfi',
            },
        ),
        migrations.CreateModel(
            name='QuestionGroup_Setting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('loaiCauHoi', models.CharField(default=b'MC', max_length=5, verbose_name=b'Lo\xe1\xba\xa1i c\xc3\xa2u h\xe1\xbb\x8fi', choices=[(b'TF', b'C\xc3\xa2u h\xe1\xbb\x8fi \xc4\x90\xc3\xbang - Sai'), (b'MC', b'C\xc3\xa2u h\xe1\xbb\x8fi Multiple Choice'), (b'ESSAY', b'C\xc3\xa2u h\xe1\xbb\x8fi t\xe1\xbb\xb1 lu\xe1\xba\xadn')])),
                ('mark_per_question', models.PositiveIntegerField(default=1, verbose_name=b'\xc4\x90i\xe1\xbb\x83m cho m\xe1\xbb\x97i c\xc3\xa2u h\xe1\xbb\x8fi')),
                ('num_of_questions', models.PositiveIntegerField(default=1, verbose_name=b's\xe1\xbb\x91 c\xc3\xa2u h\xe1\xbb\x8fi')),
                ('ca_thi', models.ForeignKey(verbose_name=b'Ca thi', to='tracnghiem.CaThi')),
                ('level', models.ForeignKey(verbose_name=b'Nh\xc3\xb3m c\xc3\xa2u h\xe1\xbb\x8fi', to='tracnghiem.QuestionGroup')),
            ],
            options={
                'verbose_name': 'C\u1ea5u h\xecnh ca thi',
                'verbose_name_plural': 'C\u1ea5u h\xecnh ca thi',
            },
        ),
        migrations.CreateModel(
            name='SinhDeConf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('loaiCauHoi', models.CharField(default=b'MC', max_length=5, verbose_name=b'Lo\xe1\xba\xa1i c\xc3\xa2u h\xe1\xbb\x8fi', choices=[(b'TF', b'C\xc3\xa2u h\xe1\xbb\x8fi \xc4\x90\xc3\xbang - Sai'), (b'MC', b'C\xc3\xa2u h\xe1\xbb\x8fi Multiple Choice'), (b'ESSAY', b'C\xc3\xa2u h\xe1\xbb\x8fi t\xe1\xbb\xb1 lu\xe1\xba\xadn')])),
                ('soLuong', models.PositiveIntegerField(default=1, verbose_name=b's\xe1\xbb\x91 c\xc3\xa2u h\xe1\xbb\x8fi')),
                ('level', models.ForeignKey(verbose_name=b'Nh\xc3\xb3m c\xc3\xa2u h\xe1\xbb\x8fi', to='tracnghiem.QuestionGroup')),
                ('logSinhDe', models.ForeignKey(to='tracnghiem.LogSinhDe')),
            ],
            options={
                'verbose_name': 'C\u1ea5u h\xecnh ca thi',
                'verbose_name_plural': 'C\u1ea5u h\xecnh ca thi',
            },
        ),
        migrations.CreateModel(
            name='MCQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='tracnghiem.Question')),
                ('answerOrder', models.CharField(blank=True, max_length=30, null=True, verbose_name=b'Th\xe1\xbb\xa9 t\xe1\xbb\xb1 hi\xe1\xbb\x83n th\xe1\xbb\x8b c\xc3\xa2u tr\xe1\xba\xa3 l\xe1\xbb\x9di', choices=[(b'CONTENT', b'N\xe1\xbb\x99i dung'), (b'RANDOM', b'Ng\xe1\xba\xabu nhi\xc3\xaan'), (b'NONE', b'None')])),
            ],
            options={
                'verbose_name': 'C\xe2u h\u1ecfi lo\u1ea1i Multiple choice',
                'verbose_name_plural': 'Danh s\xe1ch c\xe2u h\u1ecfi lo\u1ea1i Multiple choice',
            },
            bases=('tracnghiem.question',),
        ),
        migrations.CreateModel(
            name='TFQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='tracnghiem.Question')),
                ('isTrue', models.BooleanField(default=False, verbose_name=b'L\xc3\xa0 \xc4\x91\xc3\xa1p \xc3\xa1n \xc4\x91\xc3\xbang?')),
            ],
            options={
                'ordering': ['monHoc'],
                'verbose_name': 'C\xe2u h\u1ecfi \u0110\xfang/Sai',
                'verbose_name_plural': 'Danh s\xe1ch c\xe2u h\u1ecfi \u0110\xfang/Sai',
            },
            bases=('tracnghiem.question',),
        ),
        migrations.AddField(
            model_name='question',
            name='doiTuong',
            field=models.ForeignKey(verbose_name=b'\xc4\x90\xe1\xbb\x91i t\xc6\xb0\xe1\xbb\xa3ng', to='daotao.DoiTuong'),
        ),
        migrations.AddField(
            model_name='question',
            name='level',
            field=models.ForeignKey(related_name='real_level', to='tracnghiem.QuestionGroup'),
        ),
        migrations.AddField(
            model_name='question',
            name='monHoc',
            field=models.ForeignKey(verbose_name=b'M\xc3\xb4n thi', to='daotao.MonThi'),
        ),
        migrations.AddField(
            model_name='question',
            name='prior',
            field=models.ForeignKey(related_name='prior_knowledge', verbose_name=b'Nh\xc3\xb3m c\xc3\xa2u h\xe1\xbb\x8fi', to='tracnghiem.QuestionGroup'),
        ),
        migrations.AddField(
            model_name='question',
            name='taoBoi',
            field=models.ForeignKey(verbose_name=b'T\xe1\xba\xa1o b\xe1\xbb\x9fi', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(verbose_name=b'C\xc3\xa2u h\xe1\xbb\x8fi', to='tracnghiem.MCQuestion'),
        ),
    ]
